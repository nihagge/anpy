try:
    num = int(input("Your number: "))

except ValueError:
    print ("That is not a number")
    exit()

if num <= 3:
    print (num, "is prime, every number less than 4 is a prime")
    exit()

for i in range(4, num):
    if (num % i) == 0:

        print (":::",i,":::",num,":::")
        print(num, "is not a prime number")
        print(i, "times", num // i, "is", num)
        break
    else:
        print(num, "is a prime number !")



#NumToSmall(num)
ask = input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
print (ask)



