
def _list(fn):
    def wrapper(*args,**kwargs):
        return list(fn(*args,**kwargs))
    return wrapper

def _tuple(fn):
    def wrapper(*args,**kwargs):
        return tuple(fn(*args,**kwargs))
    return wrapper

def _dict(fn):
    def wrapper(*args,**kwargs):
        return dict(fn(*args,**kwargs))
    return wrapper

def _str(fn):
    def wrapper(*args,**kwargs):
        return ''.join(fn(*args,**kwargs))
    return wrapper
