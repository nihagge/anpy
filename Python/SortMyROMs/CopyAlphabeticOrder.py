#import SortTheRoms

import os
from os import path


WorkDir =("/tmp/SortMyRoms/alphabet")
AlphabeticFolders=['/a','/b','/c','/d','/e','/f']

def DirectoryCheckAndCreate(WorkDir):
    #check if work dir exits
    if path.isdir(WorkDir) == False:
        print ("WorkDir does not extis")
        exit(200)

    for i in AlphabeticFolders:
        NewFolder=WorkDir+i
        if path.os.path.isdir(NewFolder) == False:
            print ("Folder", i, "must be created ...")
            os.mkdir(NewFolder,0o700)
        else:
            print ("Folder already exists")
    # return AlphabeticFolders

def CopyFilesInAlphabeticFolder():
    print (AlphabeticFolders)



DirectoryCheckAndCreate(WorkDir)
CopyFilesInAlphabeticFolder()
