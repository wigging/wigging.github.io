---
title: Python Basics
date: 2019-07-25
layout: article
---

Basics of the Python programming language.

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
d = [1, 2, 3, 4]
```

## Further Reading

- [Python.org](https://www.python.org)
- [Real Python](https://realpython.com)
