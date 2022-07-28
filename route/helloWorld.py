from fastapi import APIRouter
baseRoute = APIRouter()


@baseRoute.get("/", tags=["Hello Word"])
def helloWorld():
    return {"message": "HelloWorld"}
