""""
generate the fibunacci sequence until the given number
"""
try:
    global FibuCount
    FibuCount = int(input("Your number: "))
except ValueError:
    print ("That's not a number!")
    exit()

a = c = 0
b = 1

for i in range(1,FibuCount):
    c = a + b
    print (c)
    a = b
    b = c


