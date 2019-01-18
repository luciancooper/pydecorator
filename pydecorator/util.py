

def preserve_signature(wrapper,wrapped):
    # Manually update wrapper to avoid changing the signature (by copying __wrapped__)
    wrapper.__module = wrapped.__module__
    wrapper.__name__ = wrapped.__name__
    wrapper.__qualname__ = wrapped.__qualname__
    wrapper.__doc__ = wrapped.__doc__
    wrapper.__annotations__ = wrapped.__annotations__
    return wrapper

def method_decorator(decorator):
    def dec(method=False):
        def wrapper(fn):
            return staticmethod(decorator(fn)) if method==True else decorator(fn)
        return wrapper
    return dec
