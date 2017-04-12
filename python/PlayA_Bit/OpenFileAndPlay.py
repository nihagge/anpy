"""
open a file and twist the content
open a text file, where the elements seperated by ":".
more element 0 to 1 and 1 to 0
"""
rFile = open('FooBar.txt', 'r+')
wFile = open('OutPut.txt', 'a')
wFile.truncate(0)
for content in rFile:
    left = content.split(':')[0]
    right = content.split(':')[1].strip('\n').lstrip()
    WriteString = right + " : " + left + "\n"
    print(content)
    print(WriteString)
    print(content)
    wFile.write(WriteString)
rFile.close()
wFile.close()
