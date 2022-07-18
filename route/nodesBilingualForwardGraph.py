from flask import Blueprint
from util.wordConvertUtil import bilingualNodes

convertRoute = Blueprint("nodesForward", __name__, url_prefix="/api/search/nodes/forward")


@convertRoute.get("/en/<wordGet>")
def bilingualEnConvertGet(wordGet):
    return bilingualNodes('en', wordGet, True)


@convertRoute.get("/jp/<wordGet>")
def bilingualJpConvertGet(wordGet):
    return bilingualNodes('jp', wordGet, True)
