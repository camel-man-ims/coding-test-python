# 21.05.13

def qsort(data):
    if len(data) <= 1 :
        return data

    left,right = [],[]
    pivot = data[0]

    for i in range(1, len(data)):
        if pivot > data[i]:
            left.append(data[i])
        else:
            right.append(data[i])
    return qsort(left) + [pivot] + qsort(right)

arr = [3,2,1,55,2312,12,343,45]

print(qsort(arr))