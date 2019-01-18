

import numpy
import functools

# decorates either a generator function that yields rows, or an iterable containing rows. 
def np_r(fn):
    def wrapper(*args,**kwargs):
        return numpy.r_[(*fn(*args,**kwargs),)]
    return functools.update_wrapper(wrapper,fn)

# decorates either a generator function that yields columns, or an iterable containing columns. 
def np_c(fn):
    def wrapper(*args,**kwargs):
        return numpy.c_[(*fn(*args,**kwargs),)]
    return functools.update_wrapper(wrapper,fn)

# decorates either a generator function that yields rows, or an iterable containing rows. 
def np_rows(fn):
    def wrapper(*args,**kwargs):
        return numpy.array([*fn(*args,**kwargs)])
    return functools.update_wrapper(wrapper,fn)
