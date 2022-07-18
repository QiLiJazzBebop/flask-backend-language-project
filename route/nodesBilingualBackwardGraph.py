from flask import Blueprint, jsonify, request

from util.wordConvertUtil import bilingualNodes
from util.wordTranslateUtil import *

convertRoute = Blueprint("nodesBackward", __name__, url_prefix="/api/search/nodes/backward")


@convertRoute.get("/en/<wordGet>")
def bilingualEnConvertGet(wordGet):
    return bilingualNodes('en', wordGet, False)


@convertRoute.get("/jp/<wordGet>")
def bilingualJpConvertGet(wordGet):
    return bilingualNodes('jp', wordGet, False)
