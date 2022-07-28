from fastapi import APIRouter

from util.comUtil import ThreadWithReturnValue, get_dictionaryAll
from util.wordTranslateUtil import getGoogleTransPairs

wordTransRoute = APIRouter(prefix="/api/search/wordTrans", tags=["Bilingual view"])


@wordTransRoute.get("/")
def wordEnSpec(fromLang: str, toLang: str, word: str):
    # extract wordTransList
    wordTransList = getGoogleTransPairs(word, fromLang, toLang)
    # check exist, using multithread
    tPool = []
    existIndexList = []
    for i, wordTran in enumerate(wordTransList):
        word = wordTran['transResult']
        t = ThreadWithReturnValue(target=get_dictionaryAll, args=[toLang, word])
        t.start()
        tPool.append(t)

    for i, t in enumerate(tPool):
        wordAllDict = t.join()
        if len(wordAllDict['forward']) != 0:
            existIndexList.append(i)

    # only return exist result
    return [wordTransList[i] for i in existIndexList]
