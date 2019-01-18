=================
Sorting
=================

.. contents:: Contents
   :local:

All the decorators in this category take a single keyword argument ``duplicate_values``, a boolean value that indicates whether or not the sorting algorithm removes extra duplicate values. The default is ``True``, meaning duplicate values are allowed, and not removed. 


Comparison function decorators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following three decorators, `mergesort`_, `mergesort_map`_, and `mergesort_index`_ are all used to decorate a comparison function that follows the signature stipulated below.

The decorated comparator must have the signature ``(a,b)``, and must return either -1, 0, or 1, indicating the following:

=========== ===============
Returned    Interpretation
=========== ===============
0           a = b
-1          a < b
1           a > b
=========== ===============

These decorators change the signature of the function they decorate, therefore if they are used to decorate a class method, ``@staticmethod`` must be stacked on top like this::

    class Sorter():

        @staticmethod
        @pydecorator.mergesort(duplicate_values=True)
        def sort(a,b):
            return 1 if a > b else -1 if a < b else 0

``mergesort``
"""""""""""""""""""""""""

The decorated function will have the signature ``(array)``, where ``array`` is either a generator or an indexable collection. The function will return the input as a sorted list::

    @pydecorator.mergesort(duplicate_values=False)
    def sorted_set(a,b):
        return 1 if a > b else -1 if a < b else 0

::

    >>> sorted_set([1,3,0,1,2])
    [0, 1, 2, 3]


``mergesort_map``
"""""""""""""""""""""""""

The decorated function will have the signature ``(array)``, where ``array`` is either a generator or an indexable collection. The function will return a list of integers, each within the range (``0 ,..., len(array)-1``). Each int in the returned array of the returned each corresponding to an index  the input as a sorted list::

    @pydecorator.mergesort_map(duplicate_values=True)
    def sorted_map(a,b):
        return 1 if a > b else -1 if a < b else 0

::

    >>> test = ['b','d','a','b','c']
    >>> test
    ['b', 'd', 'a', 'b', 'c']
    >>> index = sorted_map(test)
    >>> index
    [2, 0, 3, 4, 1]
    >>> [test[i] for i in index]
    ['a', 'b', 'b', 'c', 'd']


``mergesort_index``
"""""""""""""""""""""""""

The decorated function will have the signature ``(index,array)``, where ``array`` is either a generator or an indexable collection, and ``index`` is an indexable collection of integers, each within the range (``0 ,..., len(array)-1``), corresponding to an element in ``array``. 
The function will return the input ``index``, in sorted order (when mapped to ``array``). A simple example::

    @pydecorator.mergesort_index(duplicate_values=False)
    def sorted_indexes(a,b):
        return 1 if a > b else -1 if a < b else 0

::

    >>> test = ['b','d','a','b','c']
    >>> test
    ['b', 'd', 'a', 'b', 'c']
    >>> index = sorted_indexes(range(len(test)),test)
    >>> index
    [2, 0, 4, 1]
    >>> [test[i] for i in index]
    ['a', 'b', 'c', 'd']

.. note::
    The ``mergesort_index`` decorator is meant to be used to create functions that are part of more complex routines, such as sorting multi-dimensional data, and does not have much of a practical application as a standalone function. Use ``mergesort_map`` instead.

``sorted``
^^^^^^^^^^^^^^^^^^^^^^^^^^
This function can decorate either a generator function or a function that returns an indexable collection. It preserves the decorated functions signature. Here's a simple example::

    @pydecorator.sorted(duplicate_values=False)
    def make_list():
        return [1,0,3,5,1]

::

    >>> make_list()
    [0, 1, 3, 5]