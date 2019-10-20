---
title: Mac setup
date: 2019-10-20
layout: note
---

# Mac setup

My preferred macOS Catalina setup for a new Mac. Install and/or configure items in the order they appear on this list. This assumes the computer is starting from a fresh Catalina installation.

## Local machine name

Go to System Preferences -> Sharing and set the computer name.

## iCloud

Sign in to iCloud to sync bookmarks, email, etc.

Disable FaceTime by opening the app and signing out.

## Xcode

Install Xcode from the App Store which will also install Git.

Open Xcode to make sure developer tools are installed.

## iTerm

Download from https://iterm2.com

## Oh My Zsh

Installation instructions available at https://ohmyz.sh

## Vim

Place the following settings in the `~/.vimrc` file:

```bash
" Use Vim settings, which are much better than Vi settings. Vi is for grandpas.
" This must be first, because it changes other options as a side effect.
set nocompatible

" Enable file type detection and do language-dependent indenting
filetype plugin indent on

" Turn on syntax highlighting
syntax on

" Make backspace behave in a sane manner
set backspace=indent,eol,start

" Use the system clipboard
set clipboard=unnamed

" Allow switching buffers without saving currently modified file
set hidden

" Highlight search results
set hlsearch

" Enable mouse support
set mouse=a

" Show line numbers
set number

" Disable swap file creation
set noswapfile

" Always display status line
set laststatus=2

" Press jj to exit from insert mode
imap jj <Esc>

" change cursor to vertical bar in insert mode when using iTerm on Mac
if $TERM_PROGRAM =~ "iTerm"
  let &t_SI = "\<Esc>]50;CursorShape=1\x7" " vertical bar in insert mode
  let &t_EI = "\<Esc>]50;CursorShape=0\x7" " block in normal mode
endif
```

## Sublime Text

Download from https://www.sublimetext.com

To open Sublime Text from the command line add the following alias to `~/.zshrc`:

```bash
# Open Sublime Text from command line
alias subl="/Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl"
```

Preferences for Sublime Text are given below. Go to "Sublime Text -> Preferences -> Settings".

```json
{
    "color_scheme": "Packages/Color Scheme - Default/Mariana.sublime-color-scheme",
    "hot_exit": false,
    "font_size": 13,
    "theme": "Adaptive.sublime-theme",
    "translate_tabs_to_spaces": true,
    "trim_trailing_white_space_on_save": true,
}
```

## Git

Configure Git in the terminal using the following commands (change name and email accordingly):

```bash
git config --global user.name "John Doe"
git config --global user.email "johndoe@example.com"
```

Use https://www.gitignore.io to create a Git ignore file at `~/.gitignore` and set it as the global file with:

```bash
git config --global core.excludesfile ~/.gitignore
```

## Homebrew

Installation instructions are provided at https://brew.sh

## Jekyll

Installation instructions at https://jekyllrb.com

## aria2

Installation instructions provided at https://aria2.github.io

## LaTeX

Download from http://www.tug.org/mactex/

## Miniconda

Installer available at https://docs.conda.io/en/latest/miniconda.html

To permanently enable the Miniconda Python add the following to `~/.zshrc`:

```bash
# Set Python PATH to Miniconda3
export PATH="$HOME/miniconda3/bin:$PATH"
```

## Photos

Move the photos library `~/Pictures/Photos Library.photoslibrary` from the old Mac to the new Mac.

## AppCleaner

Download from https://freemacsoft.net/appcleaner/

## Jekyll

Installation instructions at https://jekyllrb.com
