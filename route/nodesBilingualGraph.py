from typing import Union

from fastapi import APIRouter, HTTPException
from util.nodeInfoAttachUtil import bilingualNodesBuild, monolingualNodesBuild

convertRoute = APIRouter(prefix="/api/search/nodes", tags=["Bilingual view"])


@convertRoute.get("/")
def bilingualConvertGet(word1: str,
                        lang1: str,
                        convertType: str,
                        lang2: str,
                        word2: Union[str, None] = None
                        ):
    # define direction
    if convertType == "forward":
        direction = True
    elif convertType == "backward":
        direction = False
    else:
        # if direction not defined, then return none
        raise HTTPException(status_code=404,
                            detail="direction format is not correct, please select in this field: [forward, backward]")

    # special case, there is no corresponding trans, then back one side node
    if word2 is None:
        return monolingualNodesBuild(word1, lang1, lang2, direction)
    # return bilingual nodes
    else:
        return bilingualNodesBuild(word1, word2, lang1, lang2, direction)
