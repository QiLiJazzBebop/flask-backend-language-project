from fastapi import APIRouter
from util.wordTranslateUtil import googleTranslation

wordTransRoute = APIRouter(prefix="/api/search/word")


@wordTransRoute.get("/en/{wordGet}")
def wordEnSpec(wordGet):
    return googleTranslation("jp", wordGet)


@wordTransRoute.get("/jp/{wordGet}")
def wordJpSpec(wordGet):
    return googleTranslation("en", wordGet)
