#!/bin/sh

SRC="./src"

# make directory
mkdir -p ${HOME}/.config/fontconfig
mkdir -p ${HOME}/.config/gtk-3.0

# append
cat ${SRC}/bash_profile >> ${HOME}/.bash_profile
cat ${SRC}/bashrc >> ${HOME}/.bashrc

# copy
cp ${SRC}/fonts.conf ${HOME}/.config/fontconfig
cp ${SRC}/gtkrc-2.0 ${HOME}/.gtkrc-2.0
cp ${SRC}/settings.ini ${HOME}/.config/gtk-3.0/
cp ${SRC}/vimrc ${HOME}/.vimrc
cp ${SRC}/Xdefaults ${HOME}/.Xdefaults
cp ${SRC}/xinitrc ${HOME}/.xinitrc

# link
ln -s ${HOME}/.config/fontconfig ${HOME}/.fonts.conf
