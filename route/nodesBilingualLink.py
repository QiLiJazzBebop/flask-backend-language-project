import json
from flask import Blueprint, request
import spacy
nodeBilLink = Blueprint("nodeLink", __name__, url_prefix="/api/search/link")


@nodeBilLink.get("/")
def getBilLink():
    # receive word from request
    ew = request.args.get('enWord')
    jp = request.args.get('jpWord')
    # get sense of both ew and jp word
    senseJP = {}
    senseEN = {}
    # build corresponding relation between words

