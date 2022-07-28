import spacy
import nltk
from fastapi import HTTPException
from util.comUtil import legalLanguageList
from googletrans import Translator

googleTranslatorModel = Translator()
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import wordnet

## load spacy model to check similarity
nlp = spacy.load('en_core_web_md')


# spacy method
def wordsGeneralWordnetSimilarity(w1, w2, lang1, lang2):
    """
    using method: spacy lib
    only apply for general meaning
    :return: the similarity value between two word
    """

    # trans to english
    if lang1 == "en" and lang2 == "en":
        return nlp(w1).similarity(nlp(w2))
    else:
        w1T = googleTranslatorModel.translate(w1, dest="en").text
        w2T = googleTranslatorModel.translate(w2, dest="en").text
        return nlp(w2T).similarity(nlp(w1T))


def getWordnetFormat(w, lang):
    """
    change the word as format of nltk.wordnet.synsets
    :param w: the input word
    :param lang: the language word use
    :return: the wordnet format of word
    """
    # input check
    if lang not in legalLanguageList:
        raise HTTPException(status_code=406, detail="language input not legal, it should not to be " + lang)

    # value assign
    wordSyns = []
    if lang == "jp":
        wordSyns = wordnet.synsets(w, lang='jpn')
    elif lang == "en":
        wordSyns = wordnet.synsets(w)

    # check the outcome, if it is a legal word
    if len(wordSyns) == 0:
        raise HTTPException(status_code=406, detail="word input not legal, it should not to be " + w)

    return wordSyns


def wordsWordnetSimilarity(w1, w2, lang1, lang2):
    """
    using method: nltk similarity of words
    for specific definitions of word with same pos
    :param lang1: the language of word1
    :param lang2: the language of word2
    :param w1: word1 text
    :param w2: word2 text
    :return: list of tuple, (id of w1 definition, id of w2 definition, similarity value)
    """
    # posDict = {"n": "noun", "v": "verb", "a": "adjective", "r": "adverb", "s": "suffix"}

    w1Syns = getWordnetFormat(w1, lang1)
    w2Syns = getWordnetFormat(w2, lang2)

    # error handle
    if len(w1Syns) == 0:
        raise HTTPException(status_code=404, detail="word1 input not legal " + w1)
    if len(w2Syns) == 0:
        raise HTTPException(status_code=404, detail="word1 input not legal " + w2)

    res = {"word1": w1,
           "word2": w2,
           "word1DefinitionList": [{"id": i,
                                    "definition": w1Syn.definition(),
                                    "pos": w1Syn.name().split(".")[1]
                                    } for i, w1Syn in enumerate(w1Syns)],
           "word2DefinitionList": [{"id": i,
                                    "definition": w2Syn.definition(),
                                    "pos": w2Syn.name().split(".")[1]
                                    } for i, w2Syn in enumerate(w2Syns)],
           "links": []}
    for i, w1Syn in enumerate(w1Syns):
        for j, w2Syn in enumerate(w2Syns):
            # only apply for the words with same pos
            if w1Syn.name().split(".")[1] == w2Syn.name().split(".")[1]:
                sValue = w1Syn.wup_similarity(w2Syn)
                res['links'].append({"id1": i, "id2": j, "simValue": sValue})
    # only save the top 10
    res['links'].sort(key=lambda dic: dic['simValue'], reverse=True)
    res['links'] = res['links'][:10]
    return res
