"""
Convert binary to decimal number
"""
def askType():
    global NumTyp
    NumTyp = input("binary or decimal numer(bin/dec)? ").lower()
    NumTyp.lower()
    print(NumTyp)



def askNum() -> object:
    try:
        global Num
        Num = int(input("Number: "))
    except ValueError:
        print("That's not a numer!")
        exit()



def ConvertBinToDec():
    int(BinNum, 2)
    BinNum = int(1010)
    Num = hex(BinNum)
    print(Num)


#    print(len(BinNum))


#    for i in range(len(BinNum)):
#        print(BinNum[i])




ConvertBinToDec()
#askType()
#askNum()