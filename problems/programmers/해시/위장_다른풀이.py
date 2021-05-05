# https://eda-ai-lab.tistory.com/472

def solution(clothes):
    answer = {}
    for i in clothes:
        if i[1] in answer:
            answer[i[1]] += 1
        else:
            answer[i[1]] = 1

    cnt = 1
    # 각 경우를 다 곱하면 얻는 값 = 각 원소들을 +1 한 값들을 곱한 값
    # 아무것도 안 입는 경우는 -1 해줌
    for i in answer.values():
        cnt *= (i+1)
    return cnt - 1


result = solution([["q", "A"], ["w", "B"], ["e", "C"], ["q", "A"], ["q", "A"], ["q", "A"], ["q", "B"]])
print(result)