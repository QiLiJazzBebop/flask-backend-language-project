from fastapi import APIRouter
from util.nodeConvertFromOri import bilingualNodes

convertRoute = APIRouter(prefix="/api/search/nodes/forward")


@convertRoute.get("/en_jp/{wordGet}")
def bilingualEnConvertGet(wordGet):
    return bilingualNodes('en', 'jp', wordGet, True)


@convertRoute.get("/jp_en/{wordGet}")
def bilingualJpConvertGet(wordGet):
    return bilingualNodes('jp', 'en', wordGet, True)
