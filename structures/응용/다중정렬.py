x= {('얼수',3,10),('희찬',3,42),('서연',3,15),('규헌',4,100)}

sortedArray = sorted(x, key=lambda x: (x[1], -x[2]))

print(sortedArray)

x= [['얼수',3,10],['희찬',3,42],['서연',3,15],['규헌',4,100]]

sortedArray = sorted(x, key=lambda x: (x[1], -x[2]))

print(sortedArray)