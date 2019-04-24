"""
Write a Python function that checks whether a passed string is palindrome or not.
"""
def palindrome(s):
    s = s.replace(' ', '.')
    s = s[::-1]
    print s

palindrome("hallo da draussen")
exit()

"""
Write a Python function to multiply all the numbers in a list.

Sample List : [1, 2, 3, -4]
Expected Output : -24
"""
def multiply(numbers):
    y = 1
    for x in numbers:
        y  *= x
    print y

multiply([1, 2, 3, -1,])

"""
Write a Python function that takes a list and returns a new list with unique elements of the first list.

Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
"""
def unique_list(l):
    print "The origin list:", l
    x = []
    for a in l:
        if a not in x:
            x.append(a)

    print x


unique_list([1,1,1,1,2,2,3,3,3,3,4,5])

"""
Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
Use this string : 'Hello Mr. Rogers, how are you this fine Tuesday?'
"""

def up_low(s):
    length=len(s)
    print "Length of the complete srting : %s" %str(length)
    Counter = 1
    for i in s:
        if i.isupper():
            Counter += 1
    print "Number of upper letter : ", Counter

up_low('Hello Mr. Rogers, how are you this fine Tuesday?')


"""
Write a function that checks whether a number is in a given range (Inclusive of high and low)
"""


def ran_check(num,low,high):
    if num in range(low,high+1):
        print "%s -> TRUE" % str(num)
        print "%s is in the range" % str(num)
    else:
        print "FAIL"


ran_check(3,1,8)


"""
Write a function that computes the volume of a sphere given its radius.
somme commenct : A = PI * r**2
"""
def rad(radius):
    A = 3.1415 * (radius**2)
    print A
rad(7)



