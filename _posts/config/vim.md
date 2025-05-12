---
title: Vim Configuration
date: May 12, 2025
---

Vim is a terminal editor that is available on almost every computer. The configuration file shown below is located at `~/.vimrc`.

```vim
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

" Change cursor to vertical bar in insert mode
if $TERM_PROGRAM =~ "Apple_Terminal"
  let &t_SI = "\<Esc>]50;CursorShape=1\x7" " vertical bar in insert mode
  let &t_EI = "\<Esc>]50;CursorShape=0\x7" " block in normal mode
else
  let &t_SI = "\e[6 q"
  let &t_EI = "\e[2 q"
endif
```
