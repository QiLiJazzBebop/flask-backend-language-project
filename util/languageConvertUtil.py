import json

from jisho_api.word import Word
from jisho_api.kanji import Kanji
from threading import Thread
from requests import get, post, put, patch, delete, options, head

request_methods = {
    'get': get,
    'post': post,
    'put': put,
    'patch': patch,
    'delete': delete,
    'options': options,
    'head': head,
}


# create search api
def generateSearchURL(lang, wordGet):
    forwardURL = "https://smallworldofwords.org/search/" + lang + "/networkGraph/forward/" + wordGet + "/searchBox"
    return forwardURL


def async_request(method, *args, callback=None, timeout=15, **kwargs):
    """Makes request on a different thread, and optionally passes response to a
    `callback` function when request returns.
    """
    method = request_methods[method.lower()]
    if callback:
        def callback_with_args(response, *args, **kwargs):
            try:
                callback(response)
            except:
                callback("error")

        kwargs['hooks'] = {'response': callback_with_args}
    kwargs['timeout'] = timeout
    thread = Thread(target=method, args=args, kwargs=kwargs)
    thread.start()
    return thread


def enToJpConvertCall(wordGet):
    # get the word written in other language
    apiSearchR = Word.request(wordGet)
    # extract the words from request response
    wordList = []
    for word in apiSearchR.data:
        wordD = word.dict()
        wordExtract = wordD['slug']
        wordList.append(wordExtract)

    # generate the thread to call url
    threads = []
    resJsonResponse = []
    for i, word in enumerate(wordList):
        threadGet = async_request('get', generateSearchURL('jp', word),
                                  callback=lambda r: resJsonResponse.append((r.json()['nodes'])))
        threads.append(threadGet)
    # join result
    for threadGet in threads:
        threadGet.join()
    # get dictionary for relation explanation
    apiDictList = [data.dict() for data in apiSearchR.data]
    # return response from third party (en->jp relation) and node(en node connection)

    # # short
    # resJsonResponse = sorted(resJsonResponse, key=lambda x: x[0]['label'])
    # # long
    # apiDictList = sorted(apiDictList, key=lambda x: x['slug'])
    return resJsonResponse


def jpToEnConvertCall(wordGet):
    apiSearchR = Kanji.request(wordGet)
    wordList = apiSearchR.data.dict()['main_meanings']
    # multithread request
    threads = []
    resJsonResponse = []
    for word in wordList:
        threadGet = async_request('get', generateSearchURL('en', word),
                                  callback=lambda res: resJsonResponse.append((res.json()['nodes'])))
        threads.append(threadGet)
    # join result
    for t in threads:
        t.join()
    return resJsonResponse


# jp->en/ en->jp
def bilingualConvert(lang, wordGet):
    if lang == 'en':
        resJsonResponse = enToJpConvertCall(wordGet)
        return json.dumps(resJsonResponse)
    elif lang == 'jp':
        # only return nodes
        resJsonResponse = jpToEnConvertCall(wordGet)
        return json.dumps(resJsonResponse)
