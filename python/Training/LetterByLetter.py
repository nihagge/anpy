#!/usr/bin/python
text = raw_input('Text: ')
LEN = len(text)

#for i in range(LEN):
#    print text[i]

#print text.upper()

#reverse letter by letter
print "reverse letter by letter"
A = LEN - 1
for i in range(LEN):
    POS = A - i
#    print POS
    print text[POS]


# print text[::-1]



