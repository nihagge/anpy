from __future__ import print_function

num = (1024)
print (num)
print (hex(num))
print (bin(num))
print("--------")

num = (5.232222)
print (round(num,2))

s = 'HalLO'
print (len(s))

for count in range(len(s)):
    print (s[count])
#   print (s[count]).lower()
    if s[count].isupper() == True:
        print ("Juchu")
    else:
        print (not True)
print ("-------------")
s = 'wwwxxx'
count = 0
for val in range(len(s)):
    # print (s[val])
    if s[val] == "w":
        count = count + 1
print (count)

print ("-------------")

set1 = {2,3,1,5,6,8,9999}
set2 = {3,1,7,5,6,8,9999}

print (set1.intersection(set2))

print ("-------------")

l = [1,2,3,4]
print (l.reverse(l))
print (l.sort(reversed))