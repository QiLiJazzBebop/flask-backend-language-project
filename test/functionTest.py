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

## test tag function
# import spacy
# from spacy import displacy
#
# nlp = spacy.load("en_core_web_lg")
# # doc = nlp("sweet sugar")
# # displacy.serve(doc, style="dep")
#
# ## doc similarity test
#
# docList = ['a set of rules or principles or laws (especially written ones', 'a coding system used for transmitting messages requiring brevity or secrecy', 'A sign is understood as a discrete unit of meaning in semiotics.']
# for i, doc in enumerate(docList):
#     n1 = nlp(doc)
#     if i < len(docList) - 1:
#         for j in range(i + 1, len(docList)):
#             print(i, ", ", j)
#             doc2 = docList[j]
#             n2 = nlp(doc2)
#             print(n1.similarity(n2))

## test google translator
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
#
# from random_word import RandomWords
# r = RandomWords()
# wordList = r.get_random_words()
# transRes = []
#
# for i in range(10):
#     translator = Translator()
#     word = wordList[i]
#     print(word)
#     threadTrans = ThreadWithReturnValue(target=translator.translate, args=[word, "ja", "en"])
#     threadTrans.start()
#     threadList.append(threadTrans)
#     # threadList.append(getTrans([wordList[i], "en", "ja", i], callback=lambda r: transRes.append(r.json()['nodes'])))
#
# for threadTrans in threadList:
#     transRes.append(threadTrans.join())
#
# print(time() - start_time)
#
#
# for t in transRes:
#     print(t.extra_data)
# resDict = {"synonymous word list: ": t.extra_data['parsed'][-1]}
# for pair, value in resDict.items():
#     print(pair, value)
# print("\n")
#
# start_time = time()
#
# threadList = []
# wordList = ["sweet"]
# transRes = []
# for i in range(1):
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
# print(t.extra_data['parsed'][-1][0])
# print(t.extra_data['parsed'][-1][1])
# print(t.extra_data['parsed'][-1][2])
# print(t.extra_data['parsed'][-1][3])
# print(t.extra_data['parsed'][-1][4])
# resDict = {"synonymous  word list: ": t.extra_data['parsed'][-1][5]}
# for pair, value in resDict.items():
#     print(pair, value)
# print("\n")
#
# print(time() - start_time)


### test meaning dictionary

## pydictionary
# from PyDictionary import PyDictionary
#
# # Call PyDictionary class
# dc = PyDictionary()
# # Get meaning of word "Code"
# mn = dc.meaning("Code")
# # Print Result
# print(mn)
#
# # Words
from util.comUtil import ThreadWithReturnValue, get_dictionaryAll
#
# dc = PyDictionary(my_words)
#
# # Get meaning of muli words
# res = dc.getMeanings()
#
# print("done")

## nltk
# import nltk
# from nltk.corpus import wordnet as wn
#
# # english definition
# nltk.download('omw-1.4')
#
# print(wn.synsets('receive'))
#
# from translate import Translator
#
# translator = Translator(to_lang="Japanese")
# translation = translator.translate("sweet")
# print(translation)

## argos
# from util.comUtil import get_project_root
# import argostranslate.package, argostranslate.translate
#
# # install package
# rootPath = get_project_root().__str__()
# en2jpModelPath = rootPath + "/util/argosTransModel/translate-en_ja-1_1.argosmodel"
# jp2enModelPath = rootPath + "/util/argosTransModel/translate-ja_en-1_1.argosmodel"
# argostranslate.package.install_from_path(en2jpModelPath)
# argostranslate.package.install_from_path(jp2enModelPath)
#
# # test trans function
# installed_languages = argostranslate.translate.get_installed_languages()
# translation_en_jp = installed_languages[0].get_translation(installed_languages[1])
# translation_jp_en = installed_languages[1].get_translation(installed_languages[0])
# print(translation_en_jp.translate("morning"))

# ## google trans list of word
# from util.wordTranslateUtil import googleTransLationMulti
# jp_wordList = ['今日', 'は', 'いい', '天気', 'です', 'ね']
# print(googleTransLationMulti("en", jp_wordList))

# nltk wordnet
import wn
from nltk.corpus import wordnet
import time
# example"
# partOfSpeech = {"n": "noun", "v": "verb", "a": "adjective", "r": "adverb", "s": "suffix"}
#
# dDogs = wordnet.synsets("sweet")
#
# start = time.process_time()
# for dDog in dDogs:
#     # pos and definition of word
#     print(partOfSpeech[dDog.pos()], dDog.definition())
#     # sentence example
#     print("examples: ", dDog.examples())
#     # reflections in english and japanese
#     print(dDog.lemma_names('eng'))
#     print(dDog.lemma_names('jpn'))
#
# print(time.process_time() - start)


# compare two word similarity(bilingual)
# from util.wordSimilarityUtil import wordsWordnetSimilarity, wordsSpacyGeneralSimilarity
#
# start = time.process_time()
# print(wordsSpacyGeneralSimilarity("eventually", "finally"))
#
# print("used: ", time.process_time() - start)
# start = time.process_time()
#
# print(wordsWordnetSimilarity("eventually", "finally"))
# print("used: ", time.process_time() - start)
#
# ## additional for japanese
# # jW = wordnet.synsets('家', lang='jpn')

# check word exist
# testList = ['fuc', 'you', 'can', 'try', 'out', 'setting', 'fuc', 'you', 'can', 'try', 'out', 'setting',
#             'fuc', 'you', 'can', 'try', 'out', 'setting', 'fuc', 'you', 'can', 'try', 'out', 'setting',
#             'fuc', 'you', 'can', 'try', 'out', 'setting', 'fuc', 'you', 'can', 'try', 'out', 'setting',
#             'fuc', 'you', 'can', 'try', 'out', 'setting', 'fuc', 'you', 'can', 'try', 'out', 'setting']
# print(len(testList))


# for i, word in enumerate(testList):
#     c = get_dictionaryAll("en", word)
#     print(i)

# ## multi thread
# tPool = []
# for i, word in enumerate(testList):
#     t = ThreadWithReturnValue(target=get_dictionaryAll, args=["en", word])
#     t.start()
#     tPool.append(t)
#
# for i, t in enumerate(tPool):
#     print(i, t.join())

from util.wordSimilarityUtil import getWordnetFormat
from nltk.corpus import wordnet
w = getWordnetFormat("word", "en")

print(w[0].name().split(".")[1])
