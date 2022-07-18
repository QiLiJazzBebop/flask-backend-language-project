from flask import Blueprint, jsonify
from util.wordTranslateUtil import getTopJiTrans

nodeTransRoute = Blueprint("nodeSpec", __name__, url_prefix="/api/search/node")


@nodeTransRoute.get("/en/<wordGet>")
def wordEnSpec(wordGet):
    return jsonify(getTopJiTrans(wordGet))


@nodeTransRoute.get("/jp/<wordGet>")
def wordJpSpec(wordGet):
    return jsonify(getTopJiTrans(wordGet))
