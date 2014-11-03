#!/bin/sh

SRC="./src"

cp ${SRC}/bashrc ${HOME}/.bashrc
cp ${SRC}/tmux ${HOME}/.tmux.conf
cp ${SRC}/vimrc ${HOME}/.vimrc

mkdir -p ${HOME}/.config/fontconfig
cp ${SRC}/fonts.conf ${HOME}/.config/fontconfig/

cp ${SRC}/gtkrc-2.0 ${HOME}/.gtkrc-2.0
cp ${SRC}/gtkrc-2.0.mine ${HOME}/.gtkrc-2.0.mine

mkdir -p ${HOME}/.config/gtk-3.0
cp ${SRC}/settings.ini ${HOME}/.config/gtk-3.0/

cp ${SRC}/Xdefaults ${HOME}/.Xdefaults

mkdir -p ${HOME}/.config/dunst
cp ${SRC}/dunstrc ${HOME}/.config/dunst/
