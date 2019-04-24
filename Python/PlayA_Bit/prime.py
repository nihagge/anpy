# Prime number ?

try:
    num = int(input("Enter a number: "))
except ValueError:
    print ("Oops, that's not a number")
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

