from flask import Blueprint
from util.languageConvertUtil import bilingualConvert

convertRoute = Blueprint("convert", __name__, url_prefix="/api/search/convert")


@convertRoute.get("/en/<word>")
def bilingualEnConvertGet(word):
    return bilingualConvert("en", word), 200


@convertRoute.get("/jp/<word>")
def bilingualJpConvertGet(word):
    return bilingualConvert("jp", word), 200
