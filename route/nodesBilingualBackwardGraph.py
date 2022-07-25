from fastapi import APIRouter
from util.nodeConvertFromOri import bilingualNodes

convertRoute = APIRouter(prefix="/api/search/nodes/backward")


@convertRoute.get("/en_jp/{wordGet}")
def bilingualEnConvertGet(wordGet):
    try:
        res = bilingualNodes('en', 'jp', wordGet, False)
        return res
    except Exception as e:
        return e


@convertRoute.get("/jp_en/{wordGet}")
def bilingualJpConvertGet(wordGet):
    try:
        res = bilingualNodes('jp', 'en', wordGet, False)
        return res
    except Exception as e:
        return e
