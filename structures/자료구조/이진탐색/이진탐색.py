# 21.05.15

def binary(start,end):
    global count
    middle = int((start+end)/2)

    if data[middle] == target:
        return middle
    elif data[middle] > target:
        count +=1
        return binary(0,middle-1)
    else:
        count +=1
        return binary(middle+1,end)

count =0
target = 30
data = [1,3,4,10,15,29,30,50,223,1211]

print(binary(0,len(data)-1))
print(count)