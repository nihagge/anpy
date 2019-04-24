a = (1, 3, 5, 7, 9)
print(len(a))
print(a[:3])


for i in range(1,10,2):
    print(i)


nb = input('Choose a number')
print ('Number%s \n' % (nb))


def fasel():
        print ("blabla")
fasel()


def blubber(zahl):
    print ("zalh :", zahl)

blubber(3)



fw = open('text_sample-1.txt', 'w')
fw.write('bla bla bla\n')
fw.write('foo foo foo foo')
fw.close()



fr = open('text_sample-1.txt','r')
text = fr.read()
print (text)
fr.close()