from util.wordSimilarity import wordsWordnetSimilarity
from fastapi import APIRouter

wordsSimilaritySpecification = APIRouter(prefix="/api/search/words/similarity/specification")


@wordsSimilaritySpecification.get("/")
def getWordsSimilaritySpecification(word1: str, word2: str):
    return wordsWordnetSimilarity(word1, word2)