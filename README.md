brainfuck
=========

A simple brainfuck interpreter I made in Python as homework. The only requirement is Python 3.

Usage
-----

This interpreter can be used in two different ways. It can either be called directly from the command line:

```
$ ./brainfuck.py programs/print_a.bf
A
```

or the Python APIs can be used:

```python
>>> import brainfuck as bf
>>> bf.run_program(">[-<+>]", [0, 4])
[4, 0]
```

Calling it from Python is more flexible due to support for custom memory initialization. Read the comments in the source code for more about that.

License
-------

The MIT License (MIT)

Copyright (c) 2016 Victor Diniz.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
