#!/usr/bin/env python3
import sys
import os

docstring == """

"""

def get_notes(notes_dir):
    os.chdir(notes_dir)
    notes = os.listdir()
    return notes

def search(search_string, notes, case=False):
    for note in notes:
        with open(note, 'r') as f:
            for line in f.readlines():
                if case == False:
                    if search_string.lower() in line.lower():
                        return (note, line)
                else:
                    if search_string in line:
                        return (note, line)

def main(): 
    # Options
    case = False
    
    if len(sys.argv) == 1:
        print(docstring)
        return
    elif len(sys.argv) >= 2:
        if '-h' in sys.argv or '--help' in sys.argv:
            print(docstring)
            return
        if '-c' in sys.argv:
            case = True
            sys.argv.pop(sys.argv.index('-c'))
    else:
        print('Something went wrong')
        return

    if len(sys.argv) == 1: 
        if case == False
            search(sys.argv[0])
        else:
            search(sys.argv[0], case=True)
    else:
        print('you passed too many arguments')

if __name__ == '__main__':
    main()
