def is_prime(num):
    """"
    This function checks for prime numbers
    """
    #print "Number:" 'num'
    #print num
    for n in range(2,num):
        print n
        if num % n == 0:
            print "not prime"
            print n
            break
    else:
        print n
        print "This number is prime ;)"

#    if num % 2==0:
#        print "could be"

is_prime(121)
