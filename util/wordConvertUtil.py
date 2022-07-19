import json
import threading

from flask import jsonify
from util.wordTranslateUtil import w2wsTranslation, googleTranslator, wordsSimilarity
from util.comUtil import get_networkGraph_forward_dict, get_bubleGraph_forward_dict, get_networkGraph_backward_dict


def attachTranslation(fromLang, toLang, ssmRespond):
    """
    Attach quick translation result to each pairs
    :param fromLang: translate from language
    :param toLang: translate to language
    :param ssmRespond: the nodes get from ssm project api
    :return: the response attaching with translation result
    """
    for i in range(len(ssmRespond['nodes'])):
        ssmRespond['nodes'][i]['toLanguage'] = toLang
        ssmRespond['nodes'][i]['fromLanguage'] = fromLang
        word = ssmRespond['nodes'][i]['label']
        try:
            transList = w2wsTranslation(fromLang, word)
            ssmRespond['nodes'][i]['mainTranslation'] = transList[0]
            ssmRespond['nodes'][i]['otherTranslation'] = transList[1:]

        except:
            ssmRespond['nodes'][i]['mainTranslation'] = ''
            ssmRespond['nodes'][i]['otherTranslation'] = []
            # try:
            #     ssmRespond['nodes'][i]['mainTranslation'] = googleTranslator(toLang, word).text.split()[0]
            # except:
            #     pass

    return ssmRespond


def attachWordsSimilarity(enNodes, jpNodes):
    """
    extract similarity links from ja pais and en pairs
    :param enNodes: the input node from en side
    :param jpNodes: the input node from jp side
    :return: attach similarity level to the ori nodes
    """
    for i, unitEn in enumerate(enNodes[1:]):
        word1 = unitEn['label']
        id1 = unitEn['id']

        # set similarity area
        enNodes[i]['simPair'] = []
        for j, unitJP in enumerate(jpNodes[1:]):
            if i == 1:
                jpNodes[j]["simPair"] = []
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
                        sim = wordsSimilarity(word1, word2)
                        enNodes[i]['simPair'].append({"id": id2, "simValue": sim})
                        jpNodes[j]['simPair'].append({"id": id1, "simValue": sim})
            except:
                pass
    return enNodes, jpNodes


def bilingualNodes(lang, wordGet, direction):
    """
    This function add the bilingual translate pairs to ori node, add japanese node. The direction is boolean, true stand
    for forward, backward vice versa. support language A - - -> B
    :param direction: forward relation or backward relation
    :param lang: then language specified
    :param wordGet: the word input
    :return: node after modified
    """

    # define from and to language
    langA = lang
    if lang == 'en':
        langB = 'jp'
    else:
        langB = 'en'
    print(langA, langB)
    # translate, get nodes from smm can be parallel
    try:
        # get the translation pair over input word
        bilingualBestPair = googleTranslator(langB, wordGet).text.split()[0]
        print(bilingualBestPair)

        # only get response while have such data
        method = get_networkGraph_forward_dict if direction else get_networkGraph_backward_dict
        # simple multi thread
        smmRespondA = method(langA, wordGet)
        smmRespondB = method(langB, bilingualBestPair)
    except Exception:
        return jsonify({"message": "word request failed, probably not found japanese version"}), 404

    # attach translation result to respond
    attachTranslation(langA, langB, smmRespondA)
    attachTranslation(langB, langA, smmRespondB)
    # basic idea: link  bilingual node using core node
    # first step: get core word id and en word
    sourceAID = smmRespondA['nodes'][0]['id']
    sourceBID = smmRespondB['nodes'][0]['id']
    # sourceEnWord = bilingualBestPair if lang == 'en' else smmRespondA['nodes'][0]['lang']

    # second step: link en/jp nodes
    smmRespondB['nodes'][0] = smmRespondA['nodes'][0]
    for i in range(len(smmRespondB['links'])):
        sourceID = smmRespondB['links'][i]['source']
        targetID = smmRespondB['links'][i]['target']
        if sourceID == sourceBID:
            smmRespondB['links'][i]['source'] = sourceAID
        if targetID == sourceBID:
            smmRespondB['links'][i]['target'] = sourceAID

    # third step: assign similarity
    if lang == 'en':
        smmRespondA['nodes'], smmRespondB['nodes'] = attachWordsSimilarity(smmRespondA['nodes'], smmRespondB['nodes'])
    else:
        smmRespondB['nodes'], smmRespondA['nodes'] = attachWordsSimilarity(smmRespondB['nodes'], smmRespondA['nodes'])
    res = {langA: {"links": smmRespondA['links'], "nodes": smmRespondA['nodes']},
           langB: {"links": smmRespondB['links'], "nodes": smmRespondB['nodes']}}
    # third step: assign similarity

    return json.dumps(res)
