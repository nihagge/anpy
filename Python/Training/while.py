#Lambda:

leng = lambda item: len(item)

leng('bal bla bla')

exit()


sqare = lambda num: num**2
sqare (3)
print num

exit()
def square(num):
    return num**2
square(12)


exit()
#function:
def is_prime(num):
    """"
    This function checks for prime numbers
    """
    #print "Number:" 'num'
    #print num
    for n in range(2,num):
        if num % n == 0:
            print "not prime"
            break
    else:
        print "This number is prime ;)"

#    if num % 2==0:
#        print "could be"

is_prime(1711111111)


exit()
def add_num(num1, num2):
    return num1+num2

x = add_num(2,3)
print x

exit()
def greeting(name):
    print "hallo," + name

greeting("nils")


exit()

def my_addition_func(arg1, arg2):
    """
    Comment!
    """
    print arg1
    print arg2
    print arg1+arg2

my_addition_func(1,2)





#Methods:
l = [1,2,3,4,5]
l.append(3)
print
exit()


st = 'Create a list of the first letters of every word in this string'
w = [word[0] for word in st.split()]
print w

exit()


for num in range(1,100):
    if num % 3 == 0 or num % 5 == 0:
        print "FizzBuzz"
    elif num % 3 == 0:
        print "Fizz"
    elif num % 5 == 0:
        print "Buzz"
    else:
        print num

exit()





st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word)%2 == 0:
        print word + " <-- has an even length!"

exit()


y = [x for x in range(1,50) if x%3 == 0]
print y

exit()


a=range(0,11,2)
print a
exit()

st = 'Print only the words that start with s in this sentence'
print "SPLIT solution:"
for word in st.split():
    if word[0] == 's':
        print word


exit()



lst = [x**2 for x in range(1,11)]
print lst

exit ()
l = []

for letter in 'word':
    l.append(letter)

print l

exit ()


l = (1,2,3,4,5,6,7,8)
for num in xrange(1,10):
    print num
    type(num)


exit()

y =  5.5
print(int(y))
print y
v=range(0,10,3)
print v
print type(v)

exit()

x = 0
while x < 10:
    print 'blabla:', x
    x +=1
    if x==3:
        print 'X is 3'
    else:
        print 'contiuning ...'
        continue
else:
    print "done"