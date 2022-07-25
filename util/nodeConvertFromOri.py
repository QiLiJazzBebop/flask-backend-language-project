import time
from fastapi import HTTPException

from util.wordSimilarity import wordsSpacyGeneralSimilarity
from util.wordTranslateUtil import googleTransMulti, googleTranslation
from util.comUtil import get_networkGraph_forward_dict, get_networkGraph_backward_dict, ThreadWithReturnValue


# attach main translation to node
def attachTranslation(fromLang, toLang, ssmRespond):
    """
    Attach quick translation result to each pairs
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


def bilingualNodes(fromLang, toLang, wordGet, direction):
    """
    This function add the bilingual translate pairs to ori node, add japanese node. The direction is boolean, true stand
    for forward, backward vice versa. support language A - - -> B
    :param fromLang: From language
    :param toLang: to language translation
    :param direction: forward relation or backward relation
    :param wordGet: the word input
    :return: node after modified
    """
    # translate, get nodes from smm can be parallel
    # get the translation pair over input word
    try:
        corePair = googleTranslation(toLang, wordGet)
    except:
        raise HTTPException(status_code=404, detail="word input not a legal word: " + wordGet)
    bilingualBestPair = corePair["text"]

    # apply request base on "direction" and "language"

    method = get_networkGraph_forward_dict if direction else get_networkGraph_backward_dict
    threadSmmRespondFrom = ThreadWithReturnValue(target=method, args=[fromLang, wordGet])
    threadSmmRespondTo = ThreadWithReturnValue(target=method, args=[toLang, bilingualBestPair])

    threadSmmRespondFrom.start()
    threadSmmRespondTo.start()

    # exception handle
    try:
        smmRespondFrom = threadSmmRespondFrom.join()
    except:
        raise HTTPException(status_code=404,
                            detail="word not found from lib, wordInput: " + wordGet)
    try:
        smmRespondTo = threadSmmRespondTo.join()
    except:
        raise HTTPException(status_code=404,
                            detail="word not found from lib, wordTransPair: " + bilingualBestPair)

    # attach translation result to respond
    attachTranslation(fromLang, toLang, smmRespondFrom)
    attachTranslation(toLang, fromLang, smmRespondTo)

    # build respond format
    otherTranslations = []
    for posTrans in corePair['translations']:
        for trans in list(posTrans.values()):
            for tran in trans:
                otherTranslations.append(tran['transResult'])

    coreLink = {'source': smmRespondFrom['nodes'][0]["id"],
                "target": smmRespondTo['nodes'][0]["id"],
                "weight": list(corePair['translations'][0].values())[0][0]["frequency"]}
    res = {fromLang: {"nodes": smmRespondFrom['nodes'],
                      "links": smmRespondFrom['links']},
           toLang: {"nodes": smmRespondTo['nodes'],
                    "links": smmRespondTo['links']},
           "coreLink": coreLink,
           "otherTranslations": otherTranslations
           }
    return res
