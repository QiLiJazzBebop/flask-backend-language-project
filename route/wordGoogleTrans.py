from fastapi import APIRouter
from util.wordTranslateUtil import googleTranslation

wordTranRoute = APIRouter(prefix="/api/search/word", tags=["Bilingual view"])


@wordTranRoute.get("/")
def wordEnSpec(word: str, fromLang: str, toLang: str):
    return googleTranslation(fromLang, toLang, word)
