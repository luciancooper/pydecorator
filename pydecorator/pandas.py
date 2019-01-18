import pandas as pd
import inspect
import functools

# ============================================ DataFrame ============================================ #

# Decorates a generator function that yields rows (v,...)
def pd_dfrows(columns=None):
    def dec(fn):
        def wrapper(*args,**kwargs):
            return pd.DataFrame([*fn(*args,**kwargs)],columns=columns)
        return functools.update_wrapper(wrapper,fn)
    return dec

# Decorates a generator function that yields k,(v,...) pairs
def pd_dataframe(index=None,columns=None):
    def dec(fn):
        def wrapper(*args,**kwargs):
            i,d = (list(x) for x in zip(*fn(*args,**kwargs)))
            return pd.DataFrame(d,pd.Index(i,name=index),columns=columns)
        return functools.update_wrapper(wrapper,fn)
    return dec

# Decorates a generator function that yields (k,...),(v,...) pairs
def pd_multiframe(index=None,columns=None):
    def dec(fn):
        def wrapper(*args,**kwargs):
            i,d = (list(x) for x in zip(*fn(*args,**kwargs)))
            return pd.DataFrame(d,index=pd.MultiIndex.from_tuples(i,names=index),columns=columns)
        return functools.update_wrapper(wrapper,fn)
    return dec


# ============================================ Series ============================================ #

# Decorates a generator function that yields k,v pairs
def pd_series(index=None,name=None):
    def dec(fn):
        def wrapper(*args,**kwargs):
            i,d = (list(x) for x in zip(*fn(*args,**kwargs)))
            return pd.Series(d,index=pd.Index(i,name=index),name=name)
        return functools.update_wrapper(wrapper,fn)
    return dec

# Decorates a generator function that yields (k,...),v pairs
def pd_multiseries(index=None,name=None):
    def dec(fn):
        def wrapper(*args,**kwargs):
            i,d = [[*x] for x in zip(*fn(*args,**kwargs))]
            return pd.Series(d,index=pd.MultiIndex.from_tuples(i,names=index),name=name)
        return functools.update_wrapper(wrapper,fn)
    return dec


# ============================================ Index ============================================ #

# Decorates a generator function that yields (k,...)
def pd_multi_index(names=None):
    def dec(fn):
        def wrapper(*args,**kwargs):
            return pd.MultiIndex.from_tuples([*fn(*args,**kwargs)],names=names)
        return functools.update_wrapper(wrapper,fn)
    return dec

# Decorates a generator function that yields k
def pd_index(name=None):
    def dec(fn):
        def wrapper(*args,**kwargs):
            return pd.Index([*fn(*args,**kwargs)],name=name)
        return functools.update_wrapper(wrapper,fn)
    return dec



# ============================================ Joins ============================================ #

# decorates either a generator function that yields dataframes, or an iterable containing dataframes. 
def pd_concat(axis=0,**catargs):
    def dec(fn):
        def wrapper(*args,**kwargs):
            return pd.concat([*fn(*args,**kwargs)],axis=axis,**catargs)
        return functools.update_wrapper(wrapper,fn)
    return dec



# ============================================ Transforms ============================================ #

# decorates a function that reindexes dataframes
def pd_reindex(name=None):
    def dec(fn):
        def wrapper(df):
            inx = pd.Index([*map(fn,df.index)],name=(name if name!=None else df.index.names if df.index.ndim>1 else df.index.name))
            return pd.DataFrame(df.values,index=inx,columns=df.columns)
        return wrapper
    return dec


# decorates a function that transforms both the index values and column values of an inputted dataframe
def pd_transform(inx=None,col=None):
    def dec(fn):
        def wrapper(df,*args,**kwargs):
            i,d = [[*x] for x in zip(*fn(df,*args,**kwargs))]
            index = pd.Index(i,name=(inx if inx!=None else df.index.names if df.index.ndim>1 else df.index.name))
            return pd.DataFrame(d,index,columns=(col if col!=None else df.columns))
        return wrapper
    return dec


# ============================================ GroupBy ============================================ #


def pd_groupby_agg(by,columns=None):
    def dec(fn):
        if inspect.isgeneratorfunction(fn):
            def wrapper(df,*args,**kwargs):
                i,d = [[*x] for x in zip(*(a for b in (((g,r) for r in fn(data,*args,**kwargs)) for g,data in df.groupby(by)) for a in b))]
                inx = pd.Index(i,name=by) if type(by) == str else pd.MultiIndex.from_tuples(i,names=by)
                return pd.DataFrame(d,inx,columns=columns)
            return wrapper
        else:
            def wrapper(df,*args,**kwargs):
                i,d = [[*x] for x in zip(*((g,fn(data,*args,**kwargs)) for g,data in df.groupby(by)))]
                inx = pd.Index(i,name=by) if type(by) == str else pd.MultiIndex.from_tuples(i,names=by)
                return pd.DataFrame(d,inx,columns=columns)
            return wrapper

    return dec
