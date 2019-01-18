import inspect
import functools
from .util import preserve_signature

# This function decorates generator functions with the signature fn(a,b)
# These functions should merge (a,b) together
def mergesort_algorithm(fn):
    def wrapper(data):
        if len(data)<=1:return data
        m = len(data)//2
        return [*fn(wrapper(data[:m]),wrapper(data[m:]))]
    return wrapper


# ====================================================================================================================================================== #


# This function decorates comparison functions with the signature fn(a,b), where
# [a] = the first value to be compared
# [b] = the second value to be compared
# The decorated function should return a one of the following integers: [-1,0,1], explained below
#   (-1) -> a < b
#   (1) -> a > b
#   (0) -> a == b
# The function returned by the decorator will has the signature fn(l), where
#   [l] = a 1d indexable collection to be sorted
# Returns:
#   [l] = the original 1d input in sorted form
def mergesort(duplicate_values=True):
    if duplicate_values:
        def dec(fn):
            def merger(a,b):
                i,j,x,y = 0,0,len(a),len(b)
                while i<x and j<y:
                    z = fn(a[i],b[j])
                    if z<0:
                        yield a[i]
                        i=i+1
                    elif z>0:
                        yield b[j]
                        j=j+1
                    else:
                        yield a[i]
                        yield b[j]
                        i,j=i+1,j+1
                while i<x:
                    yield a[i]
                    i=i+1
                while j<y:
                    yield b[j]
                    j=j+1
            
            def sorter(data):
                if len(data)<=1:return data
                m = len(data)//2
                return [*merger(sorter(data[:m]),sorter(data[m:]))]
            
            def wrapper(data):
                if inspect.isgenerator(data):
                    data = list(data)
                return sorter(data)
            
            return preserve_signature(wrapper,fn)
        return dec
    else:
        def dec(fn):
            def merger(a,b):
                i,j,x,y = 0,0,len(a),len(b)
                while i<x and j<y:
                    z = fn(a[i],b[j])
                    if z<0:
                        yield a[i]
                        i=i+1
                    elif z>0:
                        yield b[j]
                        j=j+1
                    else:
                        yield a[i]
                        i,j=i+1,j+1
                while i<x:
                    yield a[i]
                    i=i+1
                while j<y:
                    yield b[j]
                    j=j+1
            
            def sorter(data):
                if len(data)<=1:return data
                m = len(data)//2
                return [*merger(sorter(data[:m]),sorter(data[m:]))]
            
            def wrapper(data):
                if inspect.isgenerator(data):
                    data = list(data)
                return sorter(data)
            
            return preserve_signature(wrapper,fn)

        return dec

# This function decorates comparison functions with the signature fn(a,b), where
#   [a] = the first value to be compared
#   [b] = the second value to be compared
# The decorated function should return a one of the following integers: [-1,0,1], explained below
#   (-1) -> a < b
#   (1) -> a > b
#   (0) -> a == b
# The function returned by the decorator will has the signature fn(l), where
#   [array] = a 1d indexable collection to be sorted
# Returns:
#   [index] = a list of index values that map the input list to its sorted form
def mergesort_map(duplicate_values=True):
    if duplicate_values:
        def dec(fn):
            def merger(a,b,data):
                i,j,x,y = 0,0,len(a),len(b)
                while i<x and j<y:
                    z = fn(data[a[i]],data[b[j]])
                    if z<0:
                        yield a[i]
                        i=i+1
                    elif z>0:
                        yield b[j]
                        j=j+1
                    elif a[i]<b[j]:
                        yield a[i]
                        i=i+1
                    else:
                        yield b[j]
                        j=j+1
                while i<x:
                    yield a[i]
                    i=i+1
                while j<y:
                    yield b[j]
                    j=j+1
            
            def sorter(inx,data):
                if len(inx)<=1: return inx
                m = len(inx)//2
                return [*merger(sorter(inx[:m],data),sorter(inx[m:],data),data)]
            
            def wrapper(data):
                if inspect.isgenerator(data):
                    data = list(data)
                return sorter(range(len(data)),data)
            
            return preserve_signature(wrapper,fn)
        return dec
    else:
        def dec(fn):
            def merger(a,b,data):
                i,j,x,y = 0,0,len(a),len(b)
                while i<x and j<y:
                    z = fn(data[a[i]],data[b[j]])
                    if z<0:
                        yield a[i]
                        i=i+1
                    elif z>0:
                        yield b[j]
                        j=j+1
                    else:
                        yield min(a[i],b[j])
                        i,j=i+1,j+1
                while i<x:
                    yield a[i]
                    i=i+1
                while j<y:
                    yield b[j]
                    j=j+1
            
            def sorter(inx,data):
                if len(inx)<=1: return inx
                m = len(inx)//2
                return [*merger(sorter(inx[:m],data),sorter(inx[m:],data),data)]
            
            def wrapper(data):
                if inspect.isgenerator(data):
                    data = list(data)
                return sorter(range(len(data)),data)
            
            return preserve_signature(wrapper,fn)
        return dec


# This function decorates comparison functions with the signature fn(a,b), where
#   [a] = the first value to be compared
#   [b] = the second value to be compared
# The decorated function should return a one of the following integers: [-1,0,1], explained below
#   (-1) -> a < b
#   (1) -> a > b
#   (0) -> a == b
# The function returned by the decorator will has the signature fn(index,array), where
#   [index] = a 1d list of indexes
#   [array] = a 1d indexable collection to be sorted
# Returns:
#   [index] = the input 1d list of indexes in sorted form such that it maps the input array to its sorted form
def mergesort_index(duplicate_values=True):
    if duplicate_values:
        def dec(fn):
            def merger(a,b,data):
                i,j,x,y = 0,0,len(a),len(b)
                while i<x and j<y:
                    z = fn(data[a[i]],data[b[j]])
                    if z<0:
                        yield a[i]
                        i=i+1
                    elif z>0:
                        yield b[j]
                        j=j+1
                    elif a[i]<b[j]:
                        yield a[i]
                        i=i+1
                    else:
                        yield b[j]
                        j=j+1
                while i<x:
                    yield a[i]
                    i=i+1
                while j<y:
                    yield b[j]
                    j=j+1
            
            def sorter(inx,data):
                if len(inx)<=1: return inx
                m = len(inx)//2
                return [*merger(sorter(inx[:m],data),sorter(inx[m:],data),data)]
            
            def wrapper(inx,data):
                if inspect.isgenerator(data):
                    data = list(data)
                return sorter(inx,data)
            
            return preserve_signature(wrapper,fn)
        return dec
    else:
        def dec(fn):
            def merger(a,b,data):
                i,j,x,y = 0,0,len(a),len(b)
                while i<x and j<y:
                    z = fn(data[a[i]],data[b[j]])
                    if z<0:
                        yield a[i]
                        i=i+1
                    elif z>0:
                        yield b[j]
                        j=j+1
                    else:
                        yield min(a[i],b[j])
                        i,j=i+1,j+1
                while i<x:
                    yield a[i]
                    i=i+1
                while j<y:
                    yield b[j]
                    j=j+1

            def sorter(inx,data):
                if len(inx)<=1: return inx
                m = len(inx)//2
                return [*merger(sorter(inx[:m],data),sorter(inx[m:],data),data)]
            
            def wrapper(inx,data):
                if inspect.isgenerator(data):
                    data = list(data)
                return sorter(inx,data)
            
            return preserve_signature(wrapper,fn)
        return dec


# ====================================================================================================================================================== #

def mergesort_groups(fn):
    def merger(a,b,data):
        i,j,x,y = 0,0,len(a),len(b)
        while i<x and j<y:
            z = fn(data[a[i][0]],data[b[j][0]])
            if z<0:
                yield a[i]
                i=i+1
            elif z>0:
                yield b[j]
                j=j+1
            else:
                yield a[i]+b[j]
                i,j=i+1,j+1
        while i<x:
            yield a[i]
            i=i+1
        while j < y:
            yield b[j]
            j=j+1

    def sorter(inx,data):
        if len(inx)<=1: return inx
        m = len(inx)//2
        return [*merger(sorter(inx[:m],data),sorter(inx[m:],data),data)]

    def wrapper(inx,data):
        if inspect.isgenerator(data):
            data = list(data)
        return sorter([[x] for x in inx],data)
    return preserve_signature(wrapper,fn)




# ====================================================================================================================================================== #

# This function can decorate either a generator function or a function that returns an indexable collection
# signature is preserved
def sorted(duplicate_values=True):
    if duplicate_values:
        def merger(a,b):
            i,j,x,y = 0,0,len(a),len(b)
            while i<x and j<y:
                if a[i]<b[j]:
                    yield a[i]
                    i=i+1
                elif a[i]>b[j]:
                    yield b[j]
                    j=j+1
                else:
                    yield a[i]
                    yield b[j]
                    i,j=i+1,j+1
            while i<x:
                yield a[i]
                i=i+1
            while j<y:
                yield b[j]
                j=j+1
    else:
        def merger(a,b):
            i,j,x,y = 0,0,len(a),len(b)
            while i<x and j<y:
                if a[i]<b[j]:
                    yield a[i]
                    i=i+1
                elif a[i]>b[j]:
                    yield b[j]
                    j=j+1
                else:
                    yield a[i]
                    i,j=i+1,j+1
            while i<x:
                yield a[i]
                i=i+1
            while j<y:
                yield b[j]
                j=j+1

    def sorter(l):
        if len(l)<=1:return l
        m = len(l)//2
        return [*merger(sorter(l[:m]),sorter(l[m:]))]

    def dec(fn):
        if inspect.isgeneratorfunction(fn):
            def wrapper(*args,**kwargs):
                return sorter([*fn(*args,**kwargs)])
            return functools.update_wrapper(wrapper,fn)
        else:
            def wrapper(*args,**kwargs):
                return sorter(fn(*args,**kwargs))
            return functools.update_wrapper(wrapper,fn)
    return dec
