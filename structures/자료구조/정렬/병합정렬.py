# 21.05.15

def merge(left,right):
    merged = []
    left_pointer,right_pointer = 0,0

    while len(left)>left_pointer and len(right) >right_pointer:
        if left[left_pointer] > right[right_pointer]:
            merged.append(right[right_pointer])
            right_pointer+=1
        else:
            merged.append(left[left_pointer])
            left_pointer+=1

    # 왼쪽이 남아있다면
    while len(left)>left_pointer:
        merged.append(left[left_pointer])
        left_pointer+=1

    # 오른쪽이 남아있다면
    while len(right)>right_pointer:
        merged.append(right[right_pointer])
        right_pointer+=1
    return merged

def split(data):
    if len(data) <=1:
        return data
    middle = int(len(data)/2)
    left = split(data[:middle])
    right = split(data[middle:])
    return merge(left,right)

data_list = [3,2,5,1,9,10]
print(split(data_list))