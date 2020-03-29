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
    

if __name__ == '__main__':
    main()
