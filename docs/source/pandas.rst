=================
Pandas
=================

.. contents:: Contents
   :local:


These functions decorate are used to decorate generators, returning various `pandas <https://pandas.pydata.org/pandas-docs/stable/index.html>`_ classes. They are *signature preserving* decorators, and can therefore be used to decorate class methods as well as standalone functions.

``pd_dfrows``
-----------------------------------------

Decorates a generator function that yields items in the form ``[row,...]``. The resulting function returns a pandas dataframe. Has the optional keyword argument ``columns``, which allows you to name the columns of the returned dataframe. For example::

    @pydecorator.pd_dfrows(columns=['a','b'])
    def dataframe():
        for row in [[0,1],[2,3],[4,5]]:
            yield row

::

    >>> dataframe()
    a  b
    0  0  1
    1  2  3
    2  4  5


``pd_dataframe``
-----------------------------------------

Decorates a generator function that yields items in the form ``(key,[row,..])``, and returns a pandas dataframe. Has the optional keyword arguments ``index`` and ``columns``, which allow you to name the index and columns of the returned dataframe. For example::

    @pydecorator.pd_dataframe(index='i',columns=['a','b'])
    def dataframe():
        for k,v in zip('xyz',[[0,1],[2,3],[4,5]]):
            yield k,v

::

    >>> dataframe()
       a  b
    i      
    x  0  1
    y  2  3
    z  4  5

``pd_multiframe``
-----------------------------------------

Decorates a generator function that yields items in the form ``([key,..],[row,..])``, and returns a pandas dataframe with a `MultiIndex <https://pandas.pydata.org/pandas-docs/stable/generated/pandas.MultiIndex.html>`_. Has the optional keyword arguments ``index`` and ``columns``, which allow you to name the index and columns of the returned dataframe. For example::

    @pydecorator.pd_multiframe(index=['i','j'],columns=['a','b'])
    def dataframe():
        for k1,k2,v in zip('xyz','abc',[[0,1],[2,3],[4,5]]):
            yield (k1,k2),v

::

    >>> dataframe()
         a  b
    i j      
    x a  0  1
    y b  2  3
    z c  4  5

``pd_series``
-----------------------------------------

Decorates a generator function that yields items in the form ``(key,value)``, and returns a pandas series. Has the optional keyword arguments ``index`` and ``name``, which allow you to name the index of the series, and the series itself, respectively. For example::

    @pydecorator.pd_series(index='i',name='a')
    def series():
        for k,v in zip('xyz',[0,1,2]):
            yield k,v

::

    >>> series()
    i
    x    0
    y    1
    z    2
    Name: a, dtype: int64


``pd_multiseries``
-----------------------------------------

Decorates a generator function that yields items in the form ``([key,..],value)``, and returns a pandas series with a `MultiIndex <https://pandas.pydata.org/pandas-docs/stable/generated/pandas.MultiIndex.html>`_. Has the optional keyword arguments ``index`` and ``name``, which allow you to provide names for the index of the series and the name of the series itself, respectively. For example::

    @pydecorator.pd_multiseries(index=['i','j'],name='a')
    def series():
        for k1,k2,v in zip('xyz','abc',[0,1,2]):
            yield (k1,k2),v

::

    >>> series()
    i  j
    x  a    0
    y  b    1
    z  c    2
    Name: a, dtype: int64


``pd_index``
-----------------------------------------

Decorates a generator function that yields non iterable items, and returns a pandas `Index <https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Index.html>`_. Has the optional keyword argument ``name``, which allows you to provide a name for the returned index. For example::

    @pydecorator.pd_index(name='i')
    def index():
        for k in 'xyz':
            yield k

::

    >>> index()
    Index(['x', 'y', 'z'], dtype='object', name='i')



``pd_multi_index``
-----------------------------------------

Decorates a generator function that yields items in the form ``[key,...]``, and returns a pandas `MultiIndex <https://pandas.pydata.org/pandas-docs/stable/generated/pandas.MultiIndex.html>`_. Has the optional keyword argument ``names``, which allows you to provide the level names for the returned index. For example::

    @pydecorator.pd_multi_index(names=['i','j'])
    def index():
        for k1,k2 in zip('xyz','abc'):
            yield (k1,k2)

::

    >>> index()
    MultiIndex(levels=[['x', 'y', 'z'], ['a', 'b', 'c']],
               labels=[[0, 1, 2], [0, 1, 2]],
               names=['i', 'j'])

