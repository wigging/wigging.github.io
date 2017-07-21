---
title: macOS Applications and Command Line Tools
layout: post
---

# macOS Applications and Command Line Tools

Essential apps and command line tools to install on a new Mac. Some apps are
installed via the Mac App Store which requires an iCloud account. My preferred
configuration for each app or tool is also discussed. Let me know if you have
suggestions for other applications that I should use.

## AppCleaner

Thoroughly uninstall unwanted applications. In the Preferences panel, turn on
"Check updates automatically". Download at
[freemacsoft.net/appcleaner](https://freemacsoft.net/appcleaner/).

## iCloud

Sign in to iCloud in System Preferences to restore email, bookmarks, system
settings, etc.

## Xcode

Build iOS and Mac apps with the Xcode IDE. Download via the Mac App Store.

## Safari

Useful extensions to install for the Safari web browser include
[NoMoreiTunes](http://nomoreitunes.einserver.de),
[Wipr](http://giorgiocalderolla.com), and [Save To
Pocket](https://getpocket.com/safari/).

## iTerm2

A terminal emulator for macOS that does amazing things. Download at
[iterm2.com](http://www.iterm2.com).

Add a new profile named `gavin` with the following settings:

```
Profile > Text > Blinking cursor
Profile > Window > Columns = 120, Rows = 60 (depending on screen size)
Profile > Keys, set option keys as +Esc
Profile > Keys, set ⌥← to "Send Escape B" and ⌥→ to "Send Escape F"
General > select "Quit when all windows are closed"
```

Use the default `Solarized Dark` color scheme with the following settings:

```
Profile > Colors > uncheck "Smart Cursor Color"
Profile > Colors > change Red to hex color "e35d5b"
Profile > Text > uncheck "Draw bold text in bold font"
Profile > Text > uncheck "Draw bold text in bright colors"
Profile > Text > select "Never" for "Use thin strokes for anti-aliased text"
Profile > Text > Font should be 12pt or 13pt "Menlo Regular"
Profile > Text > check "Anti-aliased"
```

Right click the iTerm icon in Dock > Options > then choose "Keep in Dock".

## Homebrew

The missing package manager for macOS. Installation instructions are provided
at [brew.sh](http://brew.sh).

## Zsh and Prezto

Use Homebrew to install the Zsh shell.

```bash
brew install zsh
```

Install Prezto using instructions at [sorin-ionescu/prezto](https://github.com/sorin-ionescu/prezto).

Also see instructions at [Mac OS X Setup Guide](http://sourabhbajaj.com/mac-setup/iTerm/zsh.html).

If using MiniConda or Anaconda for Python, make sure the currect PATH is declared in `.zshrc`.

## Vim

Install MacVim via Homebrew using the command below to override the system vim.

```bash
brew install macvim --with-override-system-vim
```

After installation, link MacVim as shown below to the Applications folder.

```bash
brew linkapps macvim
```

Use the [vim-plug](https://github.com/junegunn/vim-plug) manager to install and
update plugins.

Use the [solarized8_dark_high](https://github.com/lifepillar/vim-solarized8)
color scheme.

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

## Git

Git is already installed with macOS; however, the username and email for commit
messages need to be set (see example below).

```bash
git config --global user.name "John Doe"
git config --global user.email johndoe@example.com
```

Also need to add a global ignore file. Use
[gitignore.io](https://www.gitignore.io) to create a file for `macOS, vim,
python, xcode`. Place the file in `~/.gitignore` and tell Git to use it.

```bash
git config --global core.excludesfile '~/.gitignore'
```

## GNU Units

An excellent command line unit converter. Documentation at
[gnu.org](https://www.gnu.org/software/units/). Install via Homebrew with `brew
install gnu-units`. Invoke the unit converter with the command `gunits`.

## speedtest-cli

Command line interface tool built with Python for testing internet bandwidth
using speedtest.net. Install via Homebrew with `brew install speedtest-cli`.
Type `speedtest-cli` in the terminal to run a test that displays ping, download
speed, and upload speed.

## aria2

A next generation download utility. Documentation is available at
[aria2.github.io](https://aria2.github.io). The command line tool can be
installed via Homebrew with `brew install aria2`.

## LaTeX

Install the BasicTex distribution from [tug.org/mactex](http://www.tug.org/mactex/).

## Miniconda for Python 3

Easily install Python 3 and other packages. Follow instructions at
[conda.io/miniconda](https://conda.io/miniconda.html).

After installation, update conda to the latest version with `conda update
conda`. Then use the `conda` command to install the following Python packages:

```
ipython
numpy
scipy
matplotlib
pandas
```

