def solution(prices):
    answer = []
    for i in range(len(prices)):
        count = 0
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                count +=1
                break
            else:
                count +=1

        answer.append(count)
    return answer


price = [1, 6, 2, 3, 2, 3, 2, 3]

l = solution(price)
print(l)
