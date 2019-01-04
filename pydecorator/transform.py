
def transpose(fn):
    def wrapper(*args,**kwargs):
        for x in zip(*fn(*args,**kwargs)):
            yield list(x)
    return wrapper

def transpose_tuple(fn):
    def wrapper(*args,**kwargs):
        for x in zip(*fn(*args,**kwargs)):
            yield tuple(x)
    return wrapper
