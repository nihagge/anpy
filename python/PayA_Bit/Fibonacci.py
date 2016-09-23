# Count the fibonacci number


def fib(count):
    a = 0
    b = 1
    for count in range(count):
        c = a + b
        a = b
        b = c
        print (c)

fib(10)
try:
except: