from fastapi import FastAPI
# from fastapi.middleware import Middleware
# from fastapi.middleware.cors import CORSMiddleware
from route.nodesBilingualGraph import convertRoute
from route.wordGoogleTrans import wordTranRoute
from route.wordLegalTrans import wordTransRoute
from route.wordsLinkComment import wordsLinkComment
from route.wordsSimilarityGeneral import wordsSimilarityGeneral
from route.wordsSimilaritySpecified import wordsSimilaritySpecification
from route.helloWorld import baseRoute


def create_app():
    # middleware = [
    #     Middleware(
    #         CORSMiddleware,
    #         allow_origins=['*'],
    #         allow_credentials=True,
    #         allow_methods=['*'],
    #         allow_headers=['*']
    #     )
    # ]
    #
    # app = FastAPI(middleware=middleware)

    tags_metadata = [
        {"name": "Hello Word", "description": "Test whether website in online"},
        {"name": "Bilingual view", "description":
            "Main view\n"
            "1) Input a word, return list of available tran option(already test from ori api)\n"
            "2) Input the user selected word, return bilingual nodes, if no tran, then back monolingual nodes\n"
            "3) Input the word, then back the trans result, note jp word already attach nltk info"},
        {"name": "Word similarity", "description":
            "Check how much two word closeness\n"
            "1) general, return the value\n"
            "2) specification, return the definition list as well as definition pair closeness value"},
        {"name": "Words link", "description": "Build pos tag relation between two word, (sweet candy, nice look)"}
    ]

    app = FastAPI(openapi_tags=tags_metadata)
    # Registering endpoints
    app.include_router(baseRoute)
    app.include_router(wordTransRoute)
    app.include_router(convertRoute)
    app.include_router(wordTranRoute)
    app.include_router(wordsLinkComment)
    app.include_router(wordsSimilarityGeneral)
    app.include_router(wordsSimilaritySpecification)

    return app


app = create_app()
