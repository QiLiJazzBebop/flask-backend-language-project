from fastapi import APIRouter
import spacy
wordsLinkComment = APIRouter(prefix="/api/search/link", tags=["Words link"])


@wordsLinkComment.get("/")
def getLinkComment(word1: str, word2: str):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(word1 + " " + word2)

    r = []
    for token in doc:
        w = {"word": token.text, "lemma": token.lemma_, "pos": token.pos_, "tag": token.tag_, "dep": token.dep_}
        r.append(w)

    return r
