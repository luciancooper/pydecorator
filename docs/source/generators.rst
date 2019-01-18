=================
Generators
=================

.. contents:: Contents
   :local:

All functions decorate either a generator function or a function that yields an iterable. They return a specified type like ``list`` or ``dict``. All of the decorators in this category are *signature preserving*, therefore they can be used to decorate class methods as well as standalone functions. 

``list``
---------------------
This function decorates either a generator function or a function that yields an iterable. For example::

    @pydecorator.list
    def generate_list():
        """Generates a list"""
        for i in "generator":
            yield i

The ``generate_list`` function will return a list, like so::

    >>> generate_list()
    ['g', 'e', 'n', 'e', 'r', 'a', 't', 'o', 'r']


``tuple``
---------------------
This is the same as the ``pydecorator.list`` function, but for tuples. For example::

    @pydecorator.tuple
    def generate_tuple():
        """Generates a tuple"""
        for i in "generator":
            yield i

The ``generate_tuple`` function will return a tuple, like so::

    >>> generate_tuple()
    ('g', 'e', 'n', 'e', 'r', 'a', 't', 'o', 'r')


``set``
---------------------
This is the same as the ``pydecorator.set`` function, but for sets. For example::

    @pydecorator.set
    def generate_set():
        """Generates a set"""
        for i in "ababc":
            yield i

The ``generate_set`` function will return a set, like so::

    >>> generate_set()
    {'a', 'c', 'b'}


``dict``
---------------------
This must decorate a generator function that yields key value pairs, or a function that returns an iterable of key value tuple pairs. For example::

    @pydecorator.dict
    def keymap():
        """Generates a dict"""
        for k,v in zip('ABC','XYZ'):
            yield k,v


The ``keymap`` function will return a dict::

    >>> keymap()
    {'A': 'X', 'B': 'Y', 'C': 'Z'}


``str``
---------------------
This can decorate either a generator function that yields strings, or a function that returns an iterable of strings. For example::

    @pydecorator.str
    def word():
        """Generates a string"""
        for letter in ['g','e','n','e','r','a','t','e']:
            yield letter

The ``word`` function will return a concatenated string::

    >>> word()
    'generator'

