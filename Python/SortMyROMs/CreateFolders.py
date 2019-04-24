#!/usr/bin/python3
import os
filelist =[]
foldername=[]
Access_rights = 0o700
# ABCFolder = ['a', 'b', 'c']
ABCFolder = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

Path1='./PATH1/'

#def CreateGameRomFolders():
#    # print ("Create new folder:")
#    for NewFolder in foldername:
#        try:
#            os.mkdir(NewFolder, Access_rights)
#        except OSError:
#           pass
#    print ("done")


def CreateGameRomFolders():
    # print ("Create new folder:")
    for NewFolder in foldername:
        try:
            os.mkdir(NewFolder, Access_rights)
            for SortFolder in ABCFolder:
                try:
                    PathToCreate=(Path1,SortFolder)
                    print ("here is comes: ", SortFolder)
                    print ("deeper path", PathToCreate)
                    os.mkdir(os.path.join(NewFolder,SortFolder))
                except:
                    pass
        except OSError:
           pass
    print ("done")

def ListFolders():
    # print ("list all folders ...")
    for x in os.listdir("."):
        if os.path.isfile(x):
           # print ("File found", x)
            filelist.append(x)
    for suffix in filelist:
        suffix1=suffix.split(".")
        foldername.append(suffix1[1])
    print (foldername)

def CreateABCFolder():
    print ("A B C D E F")
    for SortFolder in ABCFolder:
        try:
            PathToCreate=(Path1,SortFolder)
            print ("here is comes: ", SortFolder)
            print ("deeper path", PathToCreate)
            os.mkdir(os.path.join(Path1,SortFolder))
        except:
            pass

# CreateABCFolder()
ListFolders()
CreateGameRomFolders()


#root_path = '/whatever/your/root/path/is/'
#folders = ['Folder_1','Folder_x','Folder_y']
#for folder in folders:
#    os.mkdir(os.path.join(root_path,folder))
