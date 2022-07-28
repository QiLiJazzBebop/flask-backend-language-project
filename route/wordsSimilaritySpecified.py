from util.wordSimilarityUtil import wordsWordnetSimilarity
from fastapi import APIRouter

wordsSimilaritySpecification = APIRouter(prefix="/api/search/words/similarity/specification", tags=["Word similarity"])


@wordsSimilaritySpecification.get("/")
def getWordsSimilaritySpecification(word1: str, word2: str, lang1: str, lang2: str):
    return wordsWordnetSimilarity(word1, word2, lang1, lang2)
