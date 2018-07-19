---
title: Write to a file in Python
excerpt: Write text and variables from Python code to a text file.
date: 2018-07-18
---

# Write to a file in Python

According to the [Python documentation](https://docs.python.org/3/tutorial/inputoutput.html), it is good practice to use the "with" keyword when dealing with file objects. This ensures that the file is properly closed even if an error is raised. The example below creates a file named "somefile.txt" in the current directory and writes the string "hello there" to the file.

```python
with open('somefile.txt', 'w') as f:
    f.write('hello there')
```

Variables such as a multiline string can be passed to the write function. The escape "\\" character in the first line removes the blank line that would appear at the top of the text file.

```python
s = """\
Multi line string.
This is anothe line here.
Done.
"""

with open('somefile.txt', 'w') as f:
    f.write(s)
```

An "f-string" can be used to write variables to a file. This is handy for generating reports containing model parameters and results from Python code.

```python
x = 3.7
y = 9.12
z = 'apple'

sf = f"""Parameters
x is {x}
y is {y}
z is {z}
"""

with open('somefile.txt', 'w') as f:
    f.write(sf)
```
