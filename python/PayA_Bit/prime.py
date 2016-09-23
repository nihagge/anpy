# Prime number ?


num = int(input("Enter a number: "))

#try:
#    num = int(num)
#    int(num)
#except ValueError:
#    return False
#    print("bla")
#   exit()
#except ValueError:
#print ("That is an integer")

if type(num) == int:
    pass
else:
    print("Not an integer ")
    exit()


if num > 3:
    for i in range(3,num):
        if ( num % i ) == 0:
            print (num,"is not a prime number")
            print (i, "times", num // i, "is", num)
            break
        else:
            print (num, "is a prime number !")
else:
    print ("every number until 3 is a prime number ;)")
