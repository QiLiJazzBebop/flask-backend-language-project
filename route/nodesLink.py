import json
from flask import Blueprint, request
import spacy
nodeLink = Blueprint("nodeLink", __name__, url_prefix="/api/search/link")


@nodeLink.get("/en")
def getLink():
    word1 = request.args.get('word1')
    word2 = request.args.get('word2')
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(word1 + " " + word2)

    r = []
    for token in doc:
        w = {"word": token.text, "lemma": token.lemma_, "pos": token.pos_, "tag": token.tag_, "dep": token.dep_}
        r.append(w)
    return json.dumps(r)
