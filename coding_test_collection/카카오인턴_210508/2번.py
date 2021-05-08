def check(p):
    flag = True
    arr = []

    for s in p:
        s_list = list(s)
        arr.append(s_list)
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 'P':
                # 1번 +2 상하좌우 확인했을 때 가운데 X 있는지 확인
                if j+2 < len(arr) and arr[i][j+2] == 'P':
                    if not arr[i][j+1] == 'X':
                        flag = False
                if i + 2 < len(arr) and arr[i+2][j] == 'P':
                    if not arr[i+1][j] == 'X':
                        flag = False
                if j -2>0 and arr[i][j-2] == 'P':
                    if not arr[i][j -1] == 'X':
                        flag = False
                if i - 2 > 0 and arr[i-2][j] == 'P':
                    if not arr[i-1][j] == 'X':
                        flag = False
                # 2번 각 상하좌우 +1 확인
                if i+1 < len(arr) and arr[i+1][j] == 'P':
                    flag = False
                if j+1 < len(arr) and arr[i][j+1] == 'P':
                    flag = False
                if i-1 >0 and arr[i-1][j] == 'P':
                    flag = False
                if j-1 > 0 and arr[i][j-1] == 'P':
                    flag = False
                # 3번 대각선 확인
                if i+1 < len(arr) and j+1 < len(arr) and arr[i+1][j+1] == 'P':
                    if not (arr[i+1][j] == 'X' and arr[i][j+1] == 'X'):
                        flag = False
                if i+1 < len(arr) and j-1 > 0 and arr[i+1][j-1] == 'P':
                    if not (arr[i+1][j] == 'X' and arr[i][j-1] == 'X'):
                        flag = False
                if i-1 > 0 and j+1 < len(arr) and arr[i-1][j+1] == 'P':
                    if not (arr[i-1][j] == 'X' and arr[i][j+1] == 'X'):
                        flag = False
                if i-1 > 0 and j-1 > 0 and arr[i-1][j-1] == 'P':
                    if not (arr[i-1][j] == 'X' and arr[i][j-1] == 'X'):
                        flag = False
    return flag


def solution(places):

    result = []
    for p in places:
        result.append(check(p))
    answer = []
    for i in result:
        if i:
            answer.append(1)
        else:
            answer.append(0)
    return answer

pas = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

solution(pas)