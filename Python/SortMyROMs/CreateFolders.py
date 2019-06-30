#!/usr/bin/python3
import os
import shutil
from os import path
target1=[]
filelist =[]
foldername=[]
WorkFolder=("/home/nelse/tmp/SortMyRoms")
Access_rights = 0o700
ABCFolder = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def ListFolders():
    os.chdir(WorkFolder)
    for x in os.listdir():
        if os.path.isfile(x):
            if x not in filelist:
                filelist.append(x)
                #check for duplicates
    print ("-> filelist:", filelist)
    # print ("done")

    for suffix in filelist:
        suffix=suffix.split(".")
        # print ("Suffix split:", suffix)
        suffix1=(suffix[1])
        # print ("Suffix:", suffix1)
        if suffix1 not in foldername:
            foldername.append(suffix1)
    print ("foldername:", foldername)


def CreateGameRomFolders():
    print ("Foldername: ", foldername)
    for NewFolder in foldername:
        try:
            os.mkdir(NewFolder, Access_rights)
            for SortFolder in ABCFolder:
                try:
                    os.mkdir(os.path.join(NewFolder,SortFolder))
                    # print("here is comes: ", NewFolder, SortFolder)
                except:
                    pass
        except OSError:
           pass
    print ("done")

def CopyRomsIntoConsoleFolder():
    print ("Files to copy:", filelist)
    for ROM in filelist:
        target=ROM.split(".")
        target1=(target[1])
        print ("Target1:", target1)
        print ("Roms:", ROM)
        #check if ROM == file
        shutil.copy(ROM,target1)
        return target1
def CopyRomsAlphabeticalOder():
    print ("Copy Roms in alphabetic order ...")
    # target=("./nils")
    target=("/home/nelse/tmp/SortMyRoms/nils")
    os.chdir(target)
    #print (os.getcwd())
    #print (os.listdir(target))
    print (".....................")
    print (os.path.isdir(target))
    print ("---------------------")

    for files in os.listdir(target):
        #print ("files ??? ")
        #print ("Files:", files)
        #print ("Target:", target)
        #print ("Is it File? ", (path.isfile(files)))
        if os.path.isfile(files) == True:
            print ("File !!", files)
#



ListFolders()
CreateGameRomFolders()
CopyRomsIntoConsoleFolder()
CopyRomsAlphabeticalOder()
# exit(100)
# ListFolders()
# CreateGameRomFolders()


