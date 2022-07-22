
from word2word import Word2word
from googletrans import Translator

## quick translation model
en2jaModel = Word2word("en", "ja")
ja2enModel = Word2word("ja", "en")

# load google translate model
googleTranslatorModel = Translator()


# word 2 word func(get 5 best translation pairs, in most japanese case, it does not have response)
def w2wsTranslation(toLang, word):
    if toLang == 'en':
        return en2jaModel(word)
    elif toLang == 'jp':
        return ja2enModel(word)


# use google translate lib, to get response
def googleTransMulti(toLang, words):
    wJ = "\n".join(words)
    if toLang == "en":
        res = googleTranslatorModel.translate(wJ, src='ja', dest='en').text.split()
        return res
    elif toLang == "jp":
        res = googleTranslatorModel.translate(wJ, src='en', dest='ja').text.split()
        return res
    # if not included the language then return ori
    return words


def googleTranslation(toLang, word):
    res = None
    returnFormat = None
    if toLang == "en":
        res = googleTranslatorModel.translate(word, src='ja', dest='en')
        returnFormat = {"src": "jp",
                        "dest": "en",
                        "text": res.text,
                        "pronunciation": res.pronunciation,
                        "definitions": [],
                        "examples": [],
                        "translations": []}
    elif toLang == "jp":
        res = googleTranslatorModel.translate(word, src='en', dest='ja')
        returnFormat = {"src": "en",
                        "dest": "jp",
                        "text": res.text,
                        "pronunciation": res.pronunciation,
                        "definitions": [],
                        "examples": [],
                        "translations": []}
        # definition part
        definitionsList = res.extra_data['parsed'][-1][1][0]
        for definition in definitionsList:
            # pos
            definitionExplains = {definition[0]: []}
            explainList = definition[1][0]
            dictGet = {"explainSentence": "",
                       "exampleSentence": "",
                       "synonyms": []}
            try:
                dictGet["explainSentence"] = explainList[0]
                dictGet["exampleSentence"] = explainList[1]
                dictGet["synonyms"] = [synonym[0] for synonym in explainList[5][0][0]]
            except:
                pass
            definitionExplains[definition[0]].append(dictGet)
            returnFormat["definitions"].append(definitionExplains)

        # examples part
        exampleList = res.extra_data['parsed'][-1][2][0]
        for example in exampleList:
            exampleSentence = example[1]
            returnFormat["examples"].append(exampleSentence)
    if res:
        # translations part
        transList = res.extra_data['parsed'][-1][5][0]
        for tran in transList:
            # pos
            transPairs = {tran[0]: []}
            for pairs in tran[1]:
                transPairs[tran[0]].append(
                    {"transResult": pairs[0], "reflectTrans": pairs[2], "frequency": 4 - pairs[3]})
            returnFormat["translations"].append(transPairs)
    return returnFormat

# # # jisho search func
# from jisho_api.word import Word
# def getTopJiTrans(wordGet):
#     respond = Word.request(wordGet)
#     respond = respond.data[:5 if len(respond.data) >= 5 else len(respond.data)]
#     respond = [r.dict() for r in respond]
#     return respond

# # jisho multithread func
# request_methods = {
#     'get': get
# }
#
#
# # create search api
# def async_request(method, *args, callback=None, timeout=15, **kwargs):
#     """Makes request on a different thread, and optionally passes response to a
#     `callback` function when request returns.
#     """
#     method = request_methods[method.lower()]
#     if callback:
#         def callback_with_args(response, *args, **kwargs):
#             try:
#                 callback(response)
#             except:
#                 callback("error")
#
#         kwargs['hooks'] = {'response': callback_with_args}
#     kwargs['timeout'] = timeout
#     thread = Thread(target=method, args=args, kwargs=kwargs)
#     thread.start()
#     return thread


# # multi call
# def enToJpConvertCall(wordGet):
#     # get the word written in other language
#     apiSearchR = Word.request(wordGet)
#     # extract the words from request response
#     wordList = []
#     for word in apiSearchR.data:
#         wordD = word.dict()
#         wordExtract = wordD['slug']
#         wordList.append(wordExtract)
#
#     # generate the thread to call url
#     threads = []
#     resJsonResponse = []
#     for i, word in enumerate(wordList):
#         threadGet = async_request('get', get_networkGraph_forward_dict('jp', word),
#                                   callback=lambda r: resJsonResponse.append((r.json()['nodes'])))
#         threads.append(threadGet)
#     # join result
#     for threadGet in threads:
#         threadGet.join()
#     # get dictionary for relation explanation
#     apiDictList = [data.dict() for data in apiSearchR.data]
#     for apiDict in apiDictList:
#         print(apiDict)
#     # return response from third party (en->jp relation) and node(en node connection)
#
#     # # short
#     # resJsonResponse = sorted(resJsonResponse, key=lambda x: x[0]['label'])
#     # # long
#     # apiDictList = sorted(apiDictList, key=lambda x: x['slug'])
#     return resJsonResponse
#
#
# def jpToEnConvertCall(wordGet):
#     """
#     using multi-thread request from jisho, and get the word explanation dict.
#     :param wordGet: the japanese word
#     :return:
#     """
#     apiSearchR = Kanji.request(wordGet)
#     wordList = apiSearchR.data.dict()['main_meanings']
#     # multithread request
#     threads = []
#     resJsonResponse = []
#     for word in wordList:
#         threadGet = async_request('get', get_networkGraph_forward_dict('en', word),
#                                   callback=lambda res: resJsonResponse.append((res.json()['nodes'])))
#         threads.append(threadGet)
#     # join result
#     for t in threads:
#         t.join()
#
#     # test output
#     print(apiSearchR.data.dict())
#     return resJsonResponse
