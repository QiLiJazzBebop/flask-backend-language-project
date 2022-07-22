from fastapi import APIRouter
from util.nodeConvertFromOri import bilingualNodes

convertRoute = APIRouter(prefix="/api/search/nodes/backward")


@convertRoute.get("/en_jp/{wordGet}")
def bilingualEnConvertGet(wordGet):
    return bilingualNodes('en', 'jp', wordGet, False)


@convertRoute.get("/jp_en/{wordGet}")
def bilingualJpConvertGet(wordGet):
    return bilingualNodes('jp', 'en', wordGet, False)
