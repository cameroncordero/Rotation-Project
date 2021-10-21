print ("hi")
i = 0
for line in f:
    if i % 2 == 0:
        print (line)
    i += 1


for i,line in enumerate(f):
    if i % 2 == 0:
        print (line)
    lineColumns = line.strip().split('\t')
    x = int(lineColumns[1]) - 1
    y = int(lineColumns[2]) + 1

    myList = [0,1,2]
firstItem, secondItem = myList[1], myList[2]
print(firstItem)
print(secondItem)
