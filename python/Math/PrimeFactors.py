
def ask():
    try:
        global num
        num = int(input("You number: "))
        if num <=3:
            print(num, "is a prime")
            exit()
    except ValueError:
        print("That's not a numer!")
        exit()

def CheckForPrime(num):
    for i in range(3,num):
        if (num % i) == 0:
            print(num, " is a not a prime")
            print(i,"is",num//i, "times in", num)
#            Prime == "No"
        else:
            Prime = "yes"
            # print(num, "is a prime")
    if Prime == "yes":
        print(num, "is a prime")


ask()
CheckForPrime(num)