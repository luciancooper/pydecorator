
import functools

# All functions decorate either a generator function or a function that yields an iterable.

def _list(fn):
    def wrapper(*args,**kwargs):
        return list(fn(*args,**kwargs))
    return functools.update_wrapper(wrapper,fn)

def _set(fn):
    def wrapper(*args,**kwargs):
        return set(fn(*args,**kwargs))
    return functools.update_wrapper(wrapper,fn)

def _tuple(fn):
    def wrapper(*args,**kwargs):
        return tuple(fn(*args,**kwargs))
    return functools.update_wrapper(wrapper,fn)

def _dict(fn):
    def wrapper(*args,**kwargs):
        return dict(fn(*args,**kwargs))
    return functools.update_wrapper(wrapper,fn)

def _str(fn):
    def wrapper(*args,**kwargs):
        return ''.join(fn(*args,**kwargs))
    return functools.update_wrapper(wrapper,fn)


