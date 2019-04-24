class Sample(object):
    pass

x = Sample()
print x

type(x)
exit()


def squ(num):
    print num**2

squ(456)



def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

add(1,3)