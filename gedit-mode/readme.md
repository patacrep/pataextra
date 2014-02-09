# Description

This [gedit](http://projects.gnome.org/gedit/) plugin provides a
highlight syntax mode for the song files `.sg` of the [Patacrep
Songbook](http://www.patacrep.com).

This package provides two files `songbook.lang` and `songbook.xml`
that you should copy in:

 * `~/.local/share/gtksourceview-3.0/language-specs`
 * `~/.local/share/mime/packages`

# Screenshot

![songbook-gedit-mode](http://www.patacrep.com/data/images/songbook-gedit-mode.png)

# Install 

You may want to run the following commands :

>     mkdir -p ~/.local/share/gtksourceview-3.0/language-specs
>     mkdir -p ~/.local/share/mime/packages
>     cp songbook.lang ~/.local/share/gtksourceview-3.0/language-specs
>     cp songbook.xml ~/.local/share/mime/packages

=====