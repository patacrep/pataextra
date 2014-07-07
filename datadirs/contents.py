#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Recursively create a list of all the .sg file in a datadir"""

from patacrep.files import recursive_find, relpath
import sys
import os
import argparse
import json


def argument_parser(args):
    """Parse arguments"""
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('--version', '-v', help='Show version', action='version',
            version='%(prog)s ' + "1")

    parser.add_argument('datadir', nargs=1, help="Datadir to explore.")

    parser.add_argument('--output', '-o', nargs=1, help="Output filename. Default to <datadir>.sbc")

    return parser.parse_args(args)

def main():
    options = argument_parser(sys.argv[1:])
    
    datadir = os.path.abspath(str(options.datadir[0]))

    if not os.path.isdir(datadir):
        print("Error: '{}' is not a directory.".format(datadir))
        sys.exit(1)
    
    if not options.output:
        output = os.path.basename(datadir) + ".sbc"
    else:
        output = str(options.output)
    
    songdir = os.path.join(datadir, "songs")
    
    if not os.path.isdir(songdir):
        print("Error: no songs directory in '{}'.".format(datadir))
        sys.exit(1)
    
    songs = recursive_find(songdir, "*.sg")
    
    songspath = []
    
    for path in songs:
        songspath.append(relpath(path, datadir))

    with open(output, "w") as out:
        json.dump(songspath, out, indent=4)
    
    
if __name__ == "__main__":
    main()