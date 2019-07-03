---
title: Vim
date: 2018-08-19
category: notes
tags: [software]
layout: article
---

My `.vimrc` file for Mac computers.

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

" Press F1 to save and quit a file
" use :update to only save when changes have been made 
nnoremap <F1> :update<CR>:q<CR>
inoremap <F1> <Esc>:update<CR>:q<CR>

" Press F2 to save file
" use :update to only save when changes have been made 
nnoremap <F2> :update<CR>
inoremap <F2> <Esc>:update<CR>

" Press F3 to view directory
nnoremap <F3> :e.<CR>
inoremap <F3> <Esc>:e.<CR>

" Press F4 to switch buffers
nnoremap <F4> <C-^>
inoremap <F4> <C-^>

" change cursor to vertical bar in insert mode when using iTerm on Mac
if $TERM_PROGRAM =~ "iTerm"
  let &t_SI = "\<Esc>]50;CursorShape=1\x7" " vertical bar in insert mode
  let &t_EI = "\<Esc>]50;CursorShape=0\x7" " block in normal mode
endif
```