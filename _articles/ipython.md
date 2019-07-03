---
title: iPython
date: 2018-10-03
category: python
tags: [software]
layout: article
---

Some notes on setting up iPython on macOS.

Create a configuration file with the command shown below. The file will be
located at `~/.ipython/profile_default/ipython_config.py`. The settings in
`ipython_config.py` apply to all iPython sessions. See the documentation at
[ipython.readthedocs.io][ipython] for a full list of configuration options.

```bash
ipython profile create
```

In the newly created `ipython_config.py` file. Uncomment the following two
lines and edit them as follows:

```python
c.InteractiveShellApp.gui = 'osx'
c.InteractiveShellApp.matplotlib = 'osx'
```

As of Matplotlib version 3.0, a framework build of python is needed when using
the osx backend with Matplotlib and iPython. This framework build can be invoked
with `pythonw` rather than `python` (see [here][matplotlib] for more details).
Run the following command to install the framework build:

```bash
conda install python.app
```

To run iPython with the framework build, you can point `pythonw` to the ipython
path or create an alias in `~/.bash_profile` as follows:

```bash
alias ipy="pythonw /Users/gavin/miniconda3/bin/ipython"
```

[ipython]: https://ipython.readthedocs.io
[matplotlib]: https://matplotlib.org/faq/osx_framework.html#osxframework-faq
