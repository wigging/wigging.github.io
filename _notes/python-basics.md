---
title: Python basics
desc: The basics of the Python programming language
date: 2019-08-05
layout: note
---

Basics of the Python programming language.

- [String](#string)
- [Dictionary](#dictionary)
- [List](#list)
- [Further Reading](#further-reading)

## String

A string in Python is represented by a series of characters enclosed by single or double quotes.

```python
# declare a string
s = 'hello there'
t = "yap, it's another string"
```

```python
# return a capitalized version of the string
>>> s = 'hello there'
>>> s.capitalize()
'Hello there'
```

```python
# return a caseless (un-capitalized) version of the string
>>> s = 'HeLlo TheRe'
>>> s.casefold()
'hello there'
```

## Dictionary

```python
d = {'one': 1, 'two': 2}
```

Update a dictionary with the key/value pairs from another dictionary. This overwrites existing keys in the original dictionary.

```python
params = {'d': 3.14, 'ep': 0.46, 'phi': 0.8}
case1 = {'d': 2.89, 'phi': 0.9}

params.update(case1)
# updates `params` to {'d': 2.89, 'ep': 0.46, 'phi': 0.9}
```

## List

```python
a = [1, 2, 3, 4]
```

## Further Reading

- [Python.org](https://www.python.org)
- [Real Python](https://realpython.com)
