
import functools
from .util import preserve_signature

def file_writer(fn):
    def wrapper(path,*args,**kwargs):
        with open(path,'w') as f:
            for l in fn(*args,**kwargs):
                print(l,file=f)
    return preserve_signature(wrapper,fn)
    #return functools.update_wrapper(wrapper,fn,assigned=('__module__', '__name__', '__qualname__', '__doc__'))


def file_reader(fn):
    def wrapper(path,*args,**kwargs):
        with open(path,'r') as f:
            for l in f:
                yield fn(l,*args,**kwargs)
    return preserve_signature(wrapper,fn)
    #return functools.update_wrapper(wrapper,fn,assigned=('__module__', '__name__', '__qualname__', '__doc__'))