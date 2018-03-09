
def sorted_set(fn):
    def sort(l):
        if len(l)<=1:
            for x in l: yield x
            return
        m = len(l)//2
        a,b = [*sort(l[:m])],[*sort(l[m:])]
        i,j,x,y = 0,0,len(a),len(b)
        while i<x and j<y:
            if a[i] < b[j]:
                yield a[i]
                i=i+1
            elif a[i] > b[j]:
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
    def wrapper(*args,**kwargs):
        return [*sort(fn(*args,**kwargs))]
    return wrapper

def mergesort_set(compare):
    def sort(l):
        if len(l)<=1:
            for x in l: yield x
            return
        m = len(l)//2
        a,b = [*sort(l[:m])],[*sort(l[m:])]
        i,j,x,y = 0,0,len(a),len(b)
        while i<x and j<y:
            z = compare(a[i],b[j])
            if z < 0:
                yield a[i]
                i=i+1
            elif z > 0:
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
    return sort

def mergesort_list(compare):
    def sort(l):
        if len(l)<=1:
            for x in l: yield x
            return
        m = len(l)//2
        a,b = [*sort(l[:m])],[*sort(l[m:])]
        i,j,x,y = 0,0,len(a),len(b)
        while i<x and j<y:
            z = compare(a[i],b[j])
            if z < 0:
                yield a[i]
                i=i+1
            elif z > 0:
                yield b[j]
                j=j+1
            else:
                yield a[i]
                yield b[i]
                i,j=i+1,j+1
        while i<x:
            yield a[i]
            i=i+1
        while j<y:
            yield b[j]
            j=j+1
    return wrapper
