=================
Transforms
=================

.. contents:: Contents
   :local:


These functions transform the output of the decorated function. They are *signature preserving*, so can therefore be used to decorate class methods as well as standalone functions

``transpose``
-----------------------------------------
This function can decorate either a generator function that yields iterables, or a function that returns an iterable containing iterable values. For example::

    @pydecorator.transpose
    def matrix():
        """Generates 4 lists of 3 values"""
        for i in range(4):
            yield ["%i-%i"%(i,j) for j in range(3)]

The ``matrix`` function will yield 3 lists of 4 values, like so::

    >>> [*matrix()]
    [['0-0', '1-0', '2-0', '3-0'], ['0-1', '1-1', '2-1', '3-1'], ['0-2', '1-2', '2-2', '3-2']]

``list_transpose``
-----------------------------------------

This function does the same thing as `transpose`_, but the decorated function will return a list, instead of being a generator. For example::

    @pydecorator.list_transpose
    def matrix():
        """Generates 4 lists of 3 values"""
        for i in range(4):
            yield ["%i-%i"%(i,j) for j in range(3)]

The ``matrix`` function will return a list containing 3 lists of 4 values each::

    >>> matrix()
    [['0-0', '1-0', '2-0', '3-0'], ['0-1', '1-1', '2-1', '3-1'], ['0-2', '1-2', '2-2', '3-2']]
