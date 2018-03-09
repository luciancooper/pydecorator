
def list_generator(fn):
    def wrapper(*args,**kwargs):
        return list(fn(*args,**kwargs))
    return wrapper

def tuple_generator(fn):
    def wrapper(*args,**kwargs):
        return tuple(fn(*args,**kwargs))
    return wrapper

def dict_generator(fn):
    def wrapper(*args,**kwargs):
        return dict(fn(*args,**kwargs))
    return wrapper

def str_generator(fn):
    def wrapper(*args,**kwargs):
        return ''.join(fn(*args,**kwargs))
    return wrapper

def file_generator(fn):
    def wrapper(path,*args,**kwargs):
        with open(path,'w') as f:
            for l in fn(*args,**kwargs):
                f.write(l)
    return wrapper
