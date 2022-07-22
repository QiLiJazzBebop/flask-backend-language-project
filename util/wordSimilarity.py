import spacy
from nltk.corpus import wordnet

## load spacy model to check similarity
nlp = spacy.load('en_core_web_md')


# spacy method
def wordsSpacyGeneralSimilarity(w1, w2):
    """
    using method: spacy lib
    only apply for general meaning
    :return: the similarity value between two word
    """
    return nlp(w1).similarity(nlp(w2))


def wordsGeneralWordnetSimilarity(w1, w2):
    """
    using method: spacy lib
    only apply for general meaning
    :return: the similarity value between two word
    """
    return nlp(w1).similarity(nlp(w2))


def wordsWordnetSimilarity(w1, w2):
    """
    using method: nltk similarity of words
    for specific definitions of word with same pos
    :param w1: word1 text
    :param w2: word2 text
    :return: list of tuple, (id of w1 definition, id of w2 definition, similarity value)
    """
    posDict = {"n": "noun", "v": "verb", "a": "adjective", "r": "adverb", "s": "suffix"}

    w1Syns = wordnet.synsets(w1)
    w2Syns = wordnet.synsets(w2)

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
    res['links'] = res['links'][:20]
    return res
