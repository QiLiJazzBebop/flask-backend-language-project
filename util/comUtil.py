import logging
import sys
from pathlib import Path
from threading import Thread
from requests import get

# define legal language
legalLanguageList = ['en', 'jp']


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
        raise Exception


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
        raise Exception("url called failed")


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
        raise Exception("url called failed")


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
        self.exception = None
        try:
            if hasattr(self, '_Thread__target'):
                # Thread uses name mangling prior to Python 3.
                self._return = self._Thread__target(*self._Thread__args, **self._Thread__kwargs)
            else:
                self._return = self._target(*self._args, **self._kwargs)
        except Exception as e:
            ## except handle
            self.exception = e

    def join(self, timeout: object = None) -> object:
        super().join(timeout)
        if self.exception:
            raise self.exception
        return self._return
