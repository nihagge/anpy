# python -c 'import crypt; print crypt.crypt("This is my Password1", "SALT1")'
import crypt
import hashlib

def testPass(cryptPass):
    salt = cryptPass[0:2]
    dictFile = open('dictionary.txt','r')
    for word in dictFile.readlines():
        word = word.split('\n')
        cryptWord = crypt.crypt("word", "salt")
        if (cryptWord == cryptPass):
            print ("[+] Passoword found:", cryptPass, "\n")
            return
        print ("[-] No password found")
    return

def main():
    passFile = open('password.txt')
    for line in passFile:
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1]
            print ("[*] Cracking password for user: ", user)
            testPass(cryptPass)

main()
