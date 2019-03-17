# #!/usr/bin/python3
import os

Access_rights = 0o700
list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def CreateFolder():

    print ("Create new folder:")
    for NewFolder in list:
        try:
            os.mkdir(NewFolder, Access_rights)
            # os.rmdir(NewFolder)
        except OSError:
            print ("Create of the folder %s failed" % NewFolder)
        else:
            print ("done")

CreateFolder()


