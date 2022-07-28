import time
from fastapi import HTTPException

from util.wordTranslateUtil import googleTransMulti
from util.comUtil import get_networkGraph_forward_dict, get_networkGraph_backward_dict, ThreadWithReturnValue


# attach main translation to node
def attachTranslation(fromLang, toLang, ssmRespond):
    """
    Attach quick translation result to each pair
    :param fromLang: translate from language
    :param toLang: translate to language
    :param ssmRespond: the nodes get from ssm project api
    :return: the response attaching with translation result
    """
    wordList = []
    for i in range(len(ssmRespond['nodes'])):
        ssmRespond['nodes'][i]['toLanguage'] = toLang
        ssmRespond['nodes'][i]['fromLanguage'] = fromLang
        word = ssmRespond['nodes'][i]['label']
        wordList.append(word)

    # adopt Google Translate with multi words
    wordTransList = googleTransMulti(toLang, wordList)
    for i in range(len(ssmRespond['nodes'])):
        ssmRespond['nodes'][i]['mainTranslation'] = wordTransList[i]

    return ssmRespond


def attachWordsSimilarity(enNodes, jpNodes):
    """
    extract similarity links from ja pais and en pairs
    :param enNodes: the input node from en side
    :param jpNodes: the input node from jp side
    :return: attach similarity level to the ori nodes
    """
    for i in range(1, len(jpNodes)):
        jpNodes[i]["simPair"] = []
    for i, unitEn in enumerate(enNodes[1:]):
        word1 = unitEn['label']
        id1 = unitEn['id']

        # set similarity area
        enNodes[i]['simPair'] = []
        for j, unitJP in enumerate(jpNodes[1:]):
            # in case some word has no id
            try:
                word2 = unitJP['mainTranslation']
                id2 = unitJP['id']
                if word1 != "" and word2 != "":
                    # res.append({"en_id": id1, "jp_id": id2, "s_value": wordsSimilarity(word1, word2)})
                    if word1 == word2:
                        enNodes[i]['simPair'].append({"id": id2, "simValue": 1})
                        jpNodes[j]['simPair'].append({"id": id1, "simValue": 1})
                    else:
                        sim = wordsSpacyGeneralSimilarity(word1, word2)
                        if sim >= 0.5:
                            enNodes[i]['simPair'].append({"id": id2, "simValue": sim})
                            jpNodes[j]['simPair'].append({"id": id1, "simValue": sim})
            except:
                pass

    return enNodes, jpNodes


def attachVirtualLink(smmRespondFrom, smmRespondTo):
    """
    This function add the link across the bilingual node, which share the same meaning
    :param smmRespondFrom: the nodes over input word
    :param smmRespondTo: the nodes over translate side node
    :return: the nodes after operated
    """
    virtualLinks = []
    # append type to all links
    for i, linkF in enumerate(smmRespondFrom['links']):
        smmRespondFrom['links'][i]["type"] = "real"
    for i, linkT in enumerate(smmRespondTo['links']):
        smmRespondTo['links'][i]["type"] = "real"
    # append repeated to all nodes
    for i, nodeF in enumerate(smmRespondFrom['nodes']):
        smmRespondFrom['nodes'][i]["repeated"] = False
    for i, nodeT in enumerate(smmRespondTo['nodes']):
        smmRespondTo['nodes'][i]["repeated"] = False

    # check if nodes repeated, and generate virtual link
    for i, nodeF in enumerate(smmRespondFrom['nodes']):
        for j, nodeT in enumerate(smmRespondTo['nodes']):
            # force connect two core node
            if nodeF['label'] == nodeT['mainTranslation'] or (i == 0 and j == 0):
                smmRespondFrom['nodes'][i]['repeated'] = True
                smmRespondTo['nodes'][j]['repeated'] = True
                # virtual link always from source language to target language
                virtualLinks.append({"source": nodeF['id'],
                                     "target": nodeT['id'],
                                     "similarity": 1,
                                     "type": "simulated"})

    return smmRespondFrom, smmRespondTo, virtualLinks


def monolingualNodesBuild(word, fromLang, toLang, direction):
    """
    This function add the bilingual translate pairs to ori node, add japanese node. The direction is boolean, true stand
    for forward, backward vice versa. support language A - - -> B
    :param word: base word
    :param fromLang: From language
    :param toLang: to language translation
    :param direction: forward relation or backward relation
    :return: node after modified
    """
    method = get_networkGraph_forward_dict if direction else get_networkGraph_backward_dict
    # get nodes from api
    try:
        smmRespond = method(fromLang, word)
    except:
        raise HTTPException(status_code=404,
                            detail="word not found from lib, wordInput: " + word)
    # attach translation result to respond
    attachTranslation(fromLang, toLang, smmRespond)
    # attach tag on line and nodes
    # append type to all links
    for i, linkF in enumerate(smmRespond['links']):
        smmRespond['links'][i]["type"] = "real"
    # append repeated to all nodes
    for i, nodeF in enumerate(smmRespond['nodes']):
        smmRespond['nodes'][i]["repeated"] = False

    return smmRespond


def bilingualNodesBuild(fromWord, toWord, fromLang, toLang, direction):
    """
    This function add the bilingual translate pairs to ori node, add japanese node. The direction is boolean, true stand
    for forward, backward vice versa. support language A - - -> B
    :param fromWord: translate from word
    :param toWord: to word
    :param fromLang: From language
    :param toLang: to language translation
    :param direction: forward relation or backward relation
    :return: node after modified
    """
    # apply request base on "direction" and "language"

    threadSmmRespondFrom = ThreadWithReturnValue(target=monolingualNodesBuild,
                                                 args=[fromWord, fromLang, toLang, direction])
    threadSmmRespondTo = ThreadWithReturnValue(target=monolingualNodesBuild,
                                               args=[toWord, toLang, fromLang, direction])
    threadSmmRespondFrom.start()
    threadSmmRespondTo.start()

    # exception handle
    smmRespondFrom = threadSmmRespondFrom.join()
    smmRespondTo = threadSmmRespondTo.join()

    # attach virtual link and mark the node
    smmRespondFrom, smmRespondTo, virtualLinks = attachVirtualLink(smmRespondFrom, smmRespondTo)
    # attach virtual link
    res = {"nodes": smmRespondFrom['nodes'] + smmRespondTo['nodes'],
           "links": smmRespondFrom['links'] + smmRespondTo['links'] + virtualLinks}
    return res
