from fastapi import APIRouter
baseRoute = APIRouter()


@baseRoute.get("/")
def helloWorld():
    return {"message": "HelloWorld"}
