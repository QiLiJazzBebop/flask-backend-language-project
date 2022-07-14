from flask import Blueprint, jsonify, request
from util.wordTranslateUtil import *
from util.wordConvertUtil import bilingualConvertOri

convertRoute = Blueprint("nodes", __name__, url_prefix="/api/search/nodes")


@convertRoute.get("/en/<wordGet>")
def bilingualEnConvertGet(wordGet):
    return bilingualConvertOri('en', wordGet)


@convertRoute.get("/jp/<wordGet>")
def bilingualJpConvertGet(wordGet):
    return bilingualConvertOri('jp', wordGet)
