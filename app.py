from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from route.helloWorld import baseRoute
from route.nodesBilingualForwardGraph import convertRoute as convertRouteF
from route.nodesBilingualBackwardGraph import convertRoute as convertRouteB
from route.wordGoogleTrans import wordTransRoute
from route.wordsLinkComment import wordsLinkComment
from route.wordsSimilarityGeneral import wordsSimilarityGeneral
from route.wordsSimilaritySpecified import wordsSimilaritySpecification


def create_app():
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=['*'],
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*']
        )
    ]

    app = FastAPI(middleware=middleware)
    # Registering endpoints
    app.include_router(baseRoute)
    app.include_router(convertRouteF)
    app.include_router(convertRouteB)
    app.include_router(wordsLinkComment)
    app.include_router(wordTransRoute)
    app.include_router(wordsSimilarityGeneral)
    app.include_router(wordsSimilaritySpecification)

    return app


app = create_app()
