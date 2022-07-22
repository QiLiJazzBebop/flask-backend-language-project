from util.wordSimilarity import wordsGeneralWordnetSimilarity
from fastapi import APIRouter

wordsSimilarityGeneral = APIRouter(prefix="/api/search/words/similarity/general")


@wordsSimilarityGeneral.get("/")
def getWordsSimilarityGeneral(word1: str, word2: str):
    return wordsGeneralWordnetSimilarity(word1, word2)