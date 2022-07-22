from pathlib import Path
from threading import Thread

from requests import get


def get_project_root() -> Path:
    return Path(__file__).parent.parent


# the small word of words projects web call api
def get_dictionaryAll(lang, wordGet):
    """
    call format: https://smallworldofwords.org/search/<lang>/dictionary/all/<word>
    :return: dict format of response
    """
    url = "https://smallworldofwords.org/search/" + lang + "/dictionary/all/" + wordGet
    try:
        res = get(url).json()
        return res
    except Exception:
        raise


def get_bubGraph_forward_dict(lang, wordGet):
    """
    call format: https://smallworldofwords.org/search/<en>/bubbleGraph/forward/<word>/searchBox
    :return: dict format of response
    """
    url = "https://smallworldofwords.org/search/" + lang + "/bubbleGraph/forward/" + wordGet + "/searchBox"
    try:
        res = get(url).json()
        return res
    except Exception:
        raise


def get_bubGraph_backward_dict(lang, wordGet):
    """
    call format: https://smallworldofwords.org/search/<en>/bubbleGraph/backward/<word>/searchBox
    :return: dict format of response
    """
    url = "https://smallworldofwords.org/search/" + lang + "/bubbleGraph/backward/" + wordGet + "/searchBox"
    try:
        res = get(url).json()
        return res
    except Exception:
        raise


def get_networkGraph_backward_dict(lang, wordGet):
    """
    call format: https://smallworldofwords.org/search/<en>/networkGraph/backward/<word>/searchBox
    :return: dict format of response
    """
    url = "https://smallworldofwords.org/search/" + lang + "/networkGraph/backward/" + wordGet + "/searchBox"
    try:
        res = get(url).json()
        return res
    except Exception:
        raise


def get_networkGraph_forward_dict(lang, wordGet):
    """
    call format: https://smallworldofwords.org/search/<en>/networkGraph/forward/<word>/searchBox
    :return: dict format of response
    """
    url = "https://smallworldofwords.org/search/" + lang + "/networkGraph/forward/" + wordGet + "/searchBox"
    try:
        res = get(url).json()
        return res
    except Exception:
        raise


# # create search api
def async_request(method, *args, callback=None, timeout=15, **kwargs):
    if callback:
        def callback_with_args(response, *args, **kwargs):
            try:
                callback(response)
            except:
                callback("error")

        kwargs['hooks'] = {'response': callback_with_args}
    kwargs['timeout'] = timeout
    thread = Thread(target=method, args=args, kwargs=kwargs)
    thread.start()
    return thread


class ThreadWithReturnValue(Thread):
    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self):
        super().join()
        return self._return
