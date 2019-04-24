import os
import time

def ask():
    try:
        global num
        num = int(input("Your number: "))
    except ValueError:
        print ("That is not a number")
        exit()
    NumToSmall(num)

def NumToSmall(num):
    if num <= 3:
        print (num, "is prime, every number less than 4 is a prime")
        exit()

def CheckForPrime(num):
    for i in range(3, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            #return num
            SearchNextPrime(num)
            break

        else:
            #print (i)
            print(num, "is a prime number !!!")

def SearchNextPrime(num):
    newnum = num + 1
    CheckForPrime(newnum)
    print("End of line")

ask()
CheckForPrime(num)


