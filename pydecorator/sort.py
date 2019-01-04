import inspect

def mergesort_algorithm(fn):
    def wrapper(l):
        if len(l)<=1:return l
        m = len(l)//2
        return [*fn(wrapper(l[:m]),wrapper(l[m:]))]
    return wrapper

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

            def wrapper(l):
                if len(l)<=1:return l
                m = len(l)//2
                return [*merger(wrapper(l[:m]),wrapper(l[m:]))]
            return wrapper
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
            def wrapper(l):
                if len(l)<=1:return l
                m = len(l)//2
                return [*merger(wrapper(l[:m]),wrapper(l[m:]))]
            return wrapper
        return dec

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

            def sorter(inx,data):
                if len(inx)<=1:
                    return inx
                m = len(inx)//2
                return [*merger(sorter(inx[:m],data),sorter(inx[m:],data),data)]

            def wrapper(data):
                inx = sorter([*range(len(data))],data)
                return inx
            return wrapper
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
                        yield a[i]
                        i,j=i+1,j+1
                while i<x:
                    yield a[i]
                    i=i+1
                while j<y:
                    yield b[j]
                    j=j+1

            def sorter(inx,data):
                if len(inx)<=1:
                    return inx
                m = len(inx)//2
                return [*merger(sorter(inx[:m],data),sorter(inx[m:],data),data)]

            def wrapper(data):
                inx = sorter([*range(len(data))],data)
                return inx
            return wrapper
        return dec

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
            return wrapper
        else:
            def wrapper(*args,**kwargs):
                return sorter(fn(*args,**kwargs))
            return wrapper
    return dec
