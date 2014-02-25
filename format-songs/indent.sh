#!/bin/sh

#Author: Romain Goffe
#Date: 27/10/2010
#Descritpion: correctly indent all songs with emacs
#Commentary: can't manage to use a relative path to emacs-format-file.el
#            so be sure to indicate the right path
#
# Usage: indent.sh DATADIR

if [ ! $# -eq 1 ]
then
  echo "Usage: indent.sh DATADIR"
  exit 1
fi

DATADIR="$1"

for song in $(find "$DATADIR" -name '*.sg') ; do
    emacs -batch $song -l "$(dirname $0)/emacs-format-file.el" -f emacs-format-function ;
done;
