#!/usr/bin/python3
import os
filelist =[]
foldername=[]
directory="~/devel/Python-Trix/ROMs"
Access_rights = 0o700
# list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def CreateFolder():
    print ("Create new folder:")
    for NewFolder in foldername:
        try:
            os.mkdir(NewFolder, Access_rights)
        except OSError:
            print ("Create of the folder %s failed" % NewFolder)
        else:
            print ("done")
    print (directory)

def ListFolders():
    print ("list all folders ...")
    for x in os.listdir("."):
        if os.path.isfile(x):
            print ("File found", x)
            filelist.append(x)
    for suffix in filelist:
        suffix1=suffix.split(".")
        foldername.append(suffix1[1])
    print (foldername)

ListFolders()
CreateFolder()



