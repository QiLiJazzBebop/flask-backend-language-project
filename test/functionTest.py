from threading import Thread
from time import time

### test url result
# from util.comUtil import get_dictionaryAll, get_networkGraph_backward_dict, get_networkGraph_forward_dict
#
# start_time = time()
# print(get_networkGraph_backward_dict("jp", "甘い"))
# print(time() - start_time)

### test jisho lib
# from jisho_api import scrape
# from jisho_api.word import Word
#
# word_requests = scrape(Word, ['sweet', 'get', 'result', 'away'], './jishoResTest')

## test sudachi lib
# from sudachipy import tokenizer
# from sudachipy import dictionary
#
# tokenizer_obj = dictionary.Dictionary().create()
#
# mode = tokenizer.Tokenizer.SplitMode.C
# m = tokenizer_obj.tokenize("食べ", mode)[0]
#
# print()
# print(m.part_of_speech())

### word similarity test
# import gensim.downloader
# glove_vectors = gensim.downloader.load('glove-wiki-gigaword-300')
#
# glove_vectors.similarity("sweet", "spicy")

### test bilingual convert
# from util.wordConvertUtil import bilingualNodes
# start_time = time()
# print(bilingualNodes("en", "sweet", 1))
# print(time() - start_time)


### test version2 similarity check
#
# import spacy
#
# nlp = spacy.load('en_core_web_md')
#
# token1 = nlp("cat")
# token2 = nlp("dog")
#
# print(token1.similarity(token2))

## tag function text
# import spacy
# from spacy import displacy
#
# nlp = spacy.load("en_core_web_sm")
# doc = nlp("sweet sugar")
# displacy.serve(doc, style="dep")


### test google translator
# import googletrans
# from googletrans import Translator
#
#
# class ThreadWithReturnValue(Thread):
#     def run(self):
#         if self._target is not None:
#             self._return = self._target(*self._args, **self._kwargs)
#
#     def join(self):
#         super().join()
#         return self._return
#
#
# start_time = time()
#
# threadList = []
# wordList = ["do", "spicy", "word", "forget", "jump", "through", "take", "finally", "try", "finish"]
# transRes = []
# for i in range(10):
#     translator = Translator()
#     threadTrans = ThreadWithReturnValue(target=translator.translate, args=[wordList[i], "ja", "en"])
#     threadTrans.start()
#     threadList.append(threadTrans)
#     # threadList.append(getTrans([wordList[i], "en", "ja", i], callback=lambda r: transRes.append(r.json()['nodes'])))
#
# for threadTrans in threadList:
#     transRes.append(threadTrans.join())
#
# t = transRes[0]
# print(t.extra_data['parts'][0])
# resDict = {"synonymous word list: ": t.extra_data['parsed'][-1]}
# for pair, value in resDict.items():
#     print(pair, value)
# print("\n")
#
# start_time = time()
#
# threadList = []
# wordList = ["遂に", "漸く", "挙句", "等々", "揚句"]
# transRes = []
# for i in range(5):
#     translator = Translator()
#     threadTrans = ThreadWithReturnValue(target=translator.translate, args=[wordList[i], "en", "ja"])
#     threadTrans.start()
#     threadList.append(threadTrans)
#     # threadList.append(getTrans([wordList[i], "en", "ja", i], callback=lambda r: transRes.append(r.json()['nodes'])))
#
# for threadTrans in threadList:
#     transRes.append(threadTrans.join())
#
# t = transRes[2]
# print(t.extra_data['parts'][0])
# resDict = {"synonymous  word list: ": t.extra_data['parsed'][-1][5]}
# for pair, value in resDict.items():
#     print(pair, value)
# print("\n")
#
# print(time() - start_time)
