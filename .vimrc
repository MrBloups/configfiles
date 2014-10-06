syntax on

set t_Co=256
set nocompatible
set background=dark
set ttyfast
set ruler
set nowrap
set backspace=eol,start,indent

" show line number
set nu
hi LineNr ctermfg=darkgray

" status bar
set wildmenu
set showcmd
set laststatus=2
hi StatusLine cterm=reverse

" tabs
set tabstop=4
set shiftwidth=1
set expandtab

" show hidden characters
set listchars=nbsp:¤,trail:¤,tab:^^
set list

" indent
filetype plugin indent on
set autoindent
set smartindent

" encodage
set encoding=utf8
set ffs=unix,dos,mac

" no backup file
set nobackup
set nowb
set noswapfile
