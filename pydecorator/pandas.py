import pandas as pd

def pd_dataframe(index=None,columns=None):
    def dec(fn):
        def wrapper(*args,**kwargs):
            i,d = [[*x] for x in zip(*fn(*args,**kwargs))]
            return pd.DataFrame(d,pd.Index(i,name=index),columns=columns)
        return wrapper
    return dec

def pd_series(index=None,name=None):
    def dec(fn):
        def wrapper(*args,**kwargs):
            i,d = [[*x] for x in zip(*fn(*args,**kwargs))]
            return pd.Series(d,index=pd.Index(i,name=index),name=name)
        return wrapper
    return dec


def pd_multi_index(names=None):
    def dec(fn):
        def wrapper(*args,**kwargs):
            return pd.MultiIndex.from_tuples([*fn(*args,**kwargs)],names=names)
        return wrapper
    return dec

def pd_index(name=None):
    def dec(fn):
        def wrapper(*args,**kwargs):
            return pd.Index([*fn(*args,**kwargs)],name=name)
        return wrapper
    return dec



def pd_concat(axis=0):
    def dec(fn):
        def wrapper(*args,**kwargs):
            return pd.concat([*fn(*args,**kwargs)],axis=axis)
        return wrapper
    return dec


def df_reindex(name=None):
    def dec(fn):
        def wrapper(df):
            inx = pd.Index([*map(fn,df.index)],name=(name if name!=None else df.index.names if df.index.ndim>1 else df.index.name))
            return pd.DataFrame(df.values,index=inx,columns=df.columns)
        return wrapper
    return dec
