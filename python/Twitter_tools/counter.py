counter = 1
counter_old = 1
counter_max = 1

for num in range(5):
    print (counter, counter_old, counter_max)
    counter  += 1
    if counter > counter_old:
        print ("counter GT counter_old")
        break
    counter_old = counter




