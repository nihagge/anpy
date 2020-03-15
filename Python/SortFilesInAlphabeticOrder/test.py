#!/usr/bin/env python3
"""Bla Bla."""
import os
import shutil
import configparser
ABC = " A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U ,V, W, X, Y, Z"
# ABC = " A, B, C"
# SOURCEDIR = "/home/nelse/tmp/SortMyRoms"
# SOURCEDIR = "/opt/Emulator/Amiga/Source"
# DESTDIR = "/home/nelse/tmp/ABC"
# DESTDIR = "/opt/Emulator/Amiga/Destination"
FILELIST = []
def GetConfig():
    config = configparser.ConfigParser()
    config.read('config.ini')
    SOURCEDIR = config['amiga']['src']
    DESTDIR = config['amiga']['des']
    print("Source ", SOURCEDIR)
    print("Destination ", DESTDIR)
    return

def abc_folder():
    """Bla ."""
    os.chdir(DESTDIR)
    for file_list in ABC:
        if not os.path.exists(file_list):
            os.makedirs(file_list)

def list_of_items():
    """Bla. """
    os.chdir(SOURCEDIR)
    for file_list in os.listdir():
        if os.path.isfile(file_list):
            FILELIST.append(file_list)
    for copy_item in FILELIST:
        first_letter = copy_item[0].upper()
        source_file = SOURCEDIR+"/"+copy_item
        dest_file = DESTDIR+"/"+first_letter[0]+"/"+copy_item
        print("Copy", source_file, "to ", dest_file)
        shutil.copyfile(source_file, dest_file)

def PrintConfig():
    print("Source ", SOURCEDIR)
    print("Destination ", DESTDIR)


GetConfig()
#abc_folder()
#list_of_items()
