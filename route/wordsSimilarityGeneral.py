from util.wordSimilarityUtil import wordsGeneralWordnetSimilarity
from fastapi import APIRouter

wordsSimilarityGeneral = APIRouter(prefix="/api/search/words/similarity/general", tags=["Word similarity"])


@wordsSimilarityGeneral.get("/")
def getWordsSimilarityGeneral(word1: str, word2: str, lang1: str, lang2: str):
    return wordsGeneralWordnetSimilarity(word1, word2, lang1, lang2)
