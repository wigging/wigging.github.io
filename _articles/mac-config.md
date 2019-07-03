---
title: Mac configuration
date: 2018-10-29
category: notes
tags: [macos]
layout: article
---

Notes about selling a Mac, configuring a new Mac, essential apps to install,
and useful command line tools.

Before you sell or give away your Mac, follow the instructions at
[support.apple.com](https://support.apple.com/en-us/HT201065). The article
guides you through the process of backing up your computer, disabling features
and services, and erasing the hard drive.

When you get a new computer, don't forget to update the operating system.

## AppCleaner

Thoroughly uninstall unwanted applications. In the Preferences panel, turn on
"Check updates automatically". Download at
[freemacsoft.net/appcleaner](https://freemacsoft.net/appcleaner/).

## iCloud

Sign in to iCloud in System Preferences to restore email, bookmarks, system
settings, etc. Check devices associated with your Apple ID at
[appleid.apple.com](https://appleid.apple.com/).

## Safari

Useful extensions to install for the Safari web browser include
[NoMoreiTunes](http://nomoreitunes.einserver.de),
[Wipr](http://giorgiocalderolla.com), and [Save To
Pocket](https://getpocket.com/safari/).

## Sublime Text

This is a great text editor for code and markup. Download at
[sublimetext.com](https://www.sublimetext.com).

See the [prefs](https://github.com/wigging/prefs) repository for my Sublime
Text preferences.

## Xcode

Build iOS and Mac apps with the Xcode IDE. Download via the Mac App Store.

## Git

Git is already installed in macOS; however, the username and email for commit
messages need to be set. See my [git](https://github.com/wigging/notes/blob/master/git.md) notes to learn more about Git and GitHub.
 
## Git LFS

Git Large File Storage (LFS) replaces large files such as audio samples,
videos, datasets, and graphics with text pointers inside Git. It can be
installed with Homebrew.

```bash
brew install git-lfs
```

## iTerm2

A terminal emulator for macOS that does amazing things. Download at
[iterm2.com](http://www.iterm2.com).

Save your settings by going to "Preferences -> General" and at the bottom of
the window enable "Load preferences from a custom folder or URL". Then choose a
location with the Browse button. And finally select the Save Current Settings
to Folder button to save your preferences to a plist file. This file can be
loaded on a new Mac to restore your preferences in a new iTerm installation.

## Homebrew

The missing package manager for macOS. Installation instructions are provided
at [brew.sh](http://brew.sh).

## Vim

Install Vim via Homebrew using the command below to override the system vim.

```bash
brew install vim --with-override-system-vi
```

Use the [vim-plug](https://github.com/junegunn/vim-plug) manager to install and
update plugins. Use the [solarized8_dark_high](https://github.com/lifepillar/vim-solarized8) color scheme.

## Pandoc

A greate universal document converter. Install via Homebrew.

```bash
brew install pandoc
```

Install the "citeproc" filter for citations and bibliography formatting. Also,
install the "crossrefr" filter for referencing figures, equations, and tables

```bash
brew install pandoc-citeproc
brew install pandoc-crossref
```

## GNU Units

An excellent command line unit converter that can be installed with Homebrew.
Documentation at [gnu.org](https://www.gnu.org/software/units/). Invoke the
unit converter with the "gunits -v" command.

```bash
brew install gnu-units
```

## aria2

A next generation download utility. Documentation is available at
[aria2.github.io](https://aria2.github.io). The command line tool can be
installed via Homebrew.

```bash
brew install aria2
```

## LaTeX

Install the MacTex or BasicTex distribution from [tug.org/mactex](http://www.tug.org/mactex/).

## Miniconda for Python 3

Easily install Python 3 and other packages. Follow instructions at
[conda.io/miniconda](https://conda.io/miniconda.html). After installation, update conda to the latest version with "conda update conda". Then use the conda command to install some essential Python packages such as ipython, numpy, scipy matplotlib, and pandas.
