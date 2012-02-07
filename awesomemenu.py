#! /usr/bin/env python

import os, sys
from xdg.IconTheme import *
from xdg.DesktopEntry import *
from fnmatch import fnmatch

def main():
    desktops = []   # init empty list
# List of the categories we are interested in
    categories = ['Network' , 'Office', 'System', 'Development', 'Game',
                  'AudioVideo', 'Graphics', 'Settings']
    categories.sort()
    path = '/usr/share/applications/'
    files = os.listdir(path)
    # Init our config object
    for file in files:
        if fnmatch(file, '*.desktop'):
            entry = DesktopEntry(os.path.join(path, file))
            desktops.append(entry)

    for category in categories:
        print('my' + category + ' = { ')
        for entry in desktops:
            if category in entry.getCategories():
                if getIconPath(entry.getIcon()) and not (fnmatch(getIconPath(entry.getIcon()), '*.ico') or fnmatch(getIconPath(entry.getIcon()), '*.svg')):      # awesome fails with ico/svg
                    print('  { "' + entry.getName() + '", "' + entry.getExec() + '", "' +
                        getIconPath(entry.getIcon()) + '" },')
                else:
                    print('  { "' + entry.getName() + '", "' + entry.getExec() + '" },')
        print('}\n')

    print('myprogmenu {')
    for category in categories:
        print('  { "' + category + '", my' + category + ' },')
    print('}\n')

    return 0

if __name__ == '__main__':
    main()
