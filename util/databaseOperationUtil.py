# status code checker
from util.comUtil import ThreadWithReturnValue, get_dictionaryAll


def extractWordExist(wordList, lang):
    ## multi thread
    wordExistIndexList = []

    tPool = []
    for i, word in enumerate(wordList):
        t = ThreadWithReturnValue(target=get_dictionaryAll, args=[lang, word])
        t.start()
        tPool.append(t)

    for i, t in enumerate(tPool):
        print(i, t.join())
    return wordExistIndexList

