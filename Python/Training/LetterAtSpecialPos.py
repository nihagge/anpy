#!/usr/bin/python
l = [0,1,2,3,4,5,6,7,8,9]
check_a = 5
check_b = 9

for element in l:
    print ('Number : %s ' % (element))
    if element > 5:
        print ('greater than %s ' % (check_a))
    else:
        print "---"
        
    if element < 9:
        print ('still unter %s' % (check_b)
