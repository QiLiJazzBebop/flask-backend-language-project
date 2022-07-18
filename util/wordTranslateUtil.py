import gensim.downloader
import spacy
from word2word import Word2word
from jisho_api.word import Word
from jisho_api.kanji import Kanji
from threading import Thread
from requests import get
from googletrans import Translator
from util.comUtil import get_networkGraph_forward_dict

# quick translation model
en2jaModel = Word2word("en", "ja")
ja2enModel = Word2word("ja", "en")
googleTranslatorModel = Translator()

# load spacy model to check similarity
nlp = spacy.load('en_core_web_md')


def wordsSimilarity(w1, w2):
    """
    using method: glove_vectors.similarity("sweet", "spicy")
    :return: the similarity value between two word
    """
    return nlp(w1).similarity(nlp(w2))


# word 2 word func(get 5 best translation pairs)
def w2wsTranslation(lang, word):
    if lang == 'en':
        return en2jaModel(word)
    elif lang == 'jp':
        return ja2enModel(word)


def googleTranslator(toLang, word):
    res = None
    if toLang == "en":
        res = googleTranslatorModel.translate(word, src='ja', dest='en')
    elif toLang == "jp":
        res = googleTranslatorModel.translate(word, src='en', dest='ja')
    return res


# # jisho search func
def getTopJiTrans(wordGet):
    respond = Word.request(wordGet)
    respond = respond.data[:5 if len(respond.data) >= 5 else len(respond.data)]
    respond = [r.dict() for r in respond]
    return respond
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
