
import functools
from .generator import _list

def transpose(fn):
    def wrapper(*args,**kwargs):
        for x in zip(*fn(*args,**kwargs)):
            yield list(x)
    return functools.update_wrapper(wrapper,fn)


def list_transpose(fn):
    @_list
    def wrapper(*args,**kwargs):
        for x in zip(*fn(*args,**kwargs)):
            yield list(x)
    return functools.update_wrapper(wrapper,fn)
