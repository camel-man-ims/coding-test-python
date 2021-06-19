# 아래 경우를 만족하는 행렬을 반환
# 아래 예의 경우 11001,10100 을 반환
# 행은 2개, 열은 C의 수만큼 존재

# U = 0번째 행의 합
# L = 1번째 행의 합
# C = 각 열의 합

# U = 3, L=2 , C= [2,1,1,0,1] 이라면
#   0  1  2  3  4
# 0 1  1  0  0  1
# 1 1  0  1  0  0

# 불가능하다면 IMPOSSIBLE 을 반환

def solution(first_row_sum,second_row_sum,each_col_sum_arr):
    first = []
    second = []

    for i in each_col_sum_arr:

        if first_row_sum<0 or second_row_sum<0:
            return "IMPOSSIBLE"
        elif i==2:
            first.append(1)
            second.append(1)
            first_row_sum-=1
            second_row_sum-=1
        elif first_row_sum > 0 and i==1:
            first.append(1)
            second.append(0)
            first_row_sum-=1
        elif first_row_sum==0 and second_row_sum>0 and i==1:
            first.append(0)
            second.append(1)
            second_row_sum-=1
        elif first_row_sum ==0 and second_row_sum ==0 and i==1:
            return "IMPOSSIBLE"
        elif i==0:
            first.append(0)
            second.append(0)

    result = ""
    temp = ""
    for k in first:
        temp += str(k)

    result += temp

    temp += ","
    for k in second:
        temp += str(k)
    result += temp
    return result


s = solution(3, 2, [2, 1, 1, 0, 1])
print(s)
# print(solution(2,3,[0,0,1,1,2]))