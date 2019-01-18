=================
Files
=================

.. contents:: Contents
   :local:

The file functions are *signature changing* decorators. They allow you to read and write files by write functions that handle only a single line at a time.

``file_reader``
-----------------------------------------

This decorates a function that accepts a string as the first argument. It changes the signature of the decorated function to ``(filepath,*args,**kwargs)``. The returned function is a generator that will open the file specified in the ``filepath`` argument, and then yield the result of calling the decorated function with the signature ``(line,*args,**kwargs)`` for each line in that file. For example::

    @pydecorator.file_reader
    def read_csv(line):
        return line.strip().split(",")

Given the file ``sometext.csv`` which contains::

    A,B,C
    D,E,F
    G,H,I

The ``read_csv`` function will return::

    >>> read_csv('sometext.csv')
    [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]


``file_writer``
-----------------------------------------

This decorates a generator function that yields each line in a file. It changes the signature of the decorated function to ``(filepath,*args,**kwargs)``. The returned function calls the original function with the signature `(*args,**kwargs)`, and writes out each line to the file specified by ``filepath``. For example::

    @pydecorator.file_writer
    def write_csv():
        for line in ["ABC","DEF","GHI"]:
            yield line

Calling ``write_csv('newfile.txt)`` would create a ``newfile.txt`` with the contents::

    ABC
    DEF
    GHI

