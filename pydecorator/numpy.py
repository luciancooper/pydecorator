

import numpy

def np_r(fn):
    def wrapper(*args,**kwargs):
        return numpy.r_[(*fn(*args,**kwargs),)]
    return wrapper

def np_c(fn):
    def wrapper(*args,**kwargs):
        return numpy.c_[(*fn(*args,**kwargs),)]
    return wrapper
