#! /usr/bin/env python

import os, sys
from xdg.IconTheme import *
from xdg.DesktopEntry import *
from fnmatch import fnmatch

def main():
    path = '/usr/share/applications/'
    files = os.listdir(path)
    # Init our config object
    for file in files:
        print(file)
        if fnmatch(file, '*.desktop'):
            entry = DesktopEntry(os.path.join(path, file))
            if getIconPath(entry.getIcon()):
                print('{ "' + entry.getName() + '", "' + entry.getExec() + '", "' +
                    getIconPath(entry.getIcon()) + '" },')
            else:
                print('{ "' + entry.getName() + '", "' + entry.getExec() + '" },')

    return 0

if __name__ == '__main__':
    main()
