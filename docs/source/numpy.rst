=================
Numpy
=================

.. contents:: Contents
   :local:

These functions are meant to decorate generator functions to return `numpy` arrays. They are *signature preserving* decorators, and can therefore be used to decorate class methods as well as standalone functions. 

``np_c``
-----------------------------------------
This decorates generator functions and applys the `numpy.c_ <https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.c_.html>`_ routine to the output. For example::

    @pydecorator.np_c
    def array():
        for col in [[1,2,3],[4,5,6],[7,8,9]]:
            yield col

::

    >>> array()
    [[1 4 7]
     [2 5 8]
     [3 6 9]]


``np_r``
-----------------------------------------
This decorates generator functions and applys the `numpy.r_ <https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.r_.html>`_ routine to the output. For example::

    @pydecorator.np_r
    def array():
        for row in [[1,2,3],[4,5,6],[7,8,9]]:
            yield row

::

    >>> array()
    [1 2 3 4 5 6 7 8 9]


``np_rows``
-----------------------------------------

This decorates generator functions and returns their output as the rows of a `numpy.array <https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.array.html>`_. For example::

    @pydecorator.np_rows
    def array():
        for row in [[1,2,3],[4,5,6],[7,8,9]]:
            yield row

::

    >>> array()
    [[1 2 3]
     [4 5 6]
     [7 8 9]]