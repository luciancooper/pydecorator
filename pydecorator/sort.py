
# fn is comparator function
def mergesort(fn):
    def merge(a,b):
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

    def wrapper(l):
        if len(l)<=1:return l
        m = len(l)//2
        return [*merge(wrapper(l[:m]),wrapper(l[m:]))]
    return wrapper

# fn is comparator function
def mergesort_set(fn):
    def merge(a,b):
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

    def wrapper(l):
        if len(l)<=1:return l
        m = len(l)//2
        return [*merge(wrapper(l[:m]),wrapper(l[m:]))]
    return wrapper


# fn is generator function
def sorted(fn):
    def merge(a,b):
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

    def sort(l):
        if len(l)<=1:return l
        m = len(l)//2
        return [*merge(sort(l[:m]),sort(l[m:]))]

    def wrapper(*args,**kwargs):
        return sort([*fn(*args,**kwargs)])
    return wrapper


# fn is generator function
def sorted_set(fn):
    def merge(a,b):
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

    def sort(l):
        if len(l)<=1:return l
        m = len(l)//2
        return [*merge(sort(l[:m]),sort(l[m:]))]

    def wrapper(*args,**kwargs):
        return sort([*fn(*args,**kwargs)])
    return wrapper
