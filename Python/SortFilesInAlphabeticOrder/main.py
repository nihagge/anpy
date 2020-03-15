#!/usr/bin/env python3
"""Bla Bla."""
import configparser
import os
import shutil
import sys
ABC = "A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U ,V, W, X, Y, Z"
FILELIST = []

def copyFileInABCOrder(hostsystem):
    """Copy all ROM. """
    SOURCEDIR = config[hostsystem]['src']
    DESTDIR = config[hostsystem]['des']
    os.chdir(DESTDIR)
    #Let's check if all folders from A to Z are there, if not, let's creat them.
    for file_list in ABC:
        if not os.path.exists(file_list):
            os.makedirs(file_list)
    #Copy files into folders
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
if __name__ == '__main__':
    hostsystem = sys.argv[1]
    if len(sys.argv) != 2:
     	print("more than 2 parameters")
    print("Main says: ", hostsystem)
    config = configparser.ConfigParser()
    config.read('config.ini')
    SOURCEDIR = config[hostsystem]['src']
    DESTDIR = config[hostsystem]['des']
    print("src and des: ", SOURCEDIR, DESTDIR)

copyFileInABCOrder(hostsystem)
