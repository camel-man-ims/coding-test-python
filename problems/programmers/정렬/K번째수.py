def solution(array,commands):
    result=[]
    for arr in commands:
        temp=array[arr[0]-1:arr[1]]
        temp.sort()
        result.append(temp[arr[2]-1])
    return result