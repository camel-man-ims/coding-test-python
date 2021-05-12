# 21.04.17
# 대표적 dp 문제 dp = memoization, 점화식
# 피보나치 수열이랑 같음
# i-2 번째에 00을 붙이거나, i-1 번째에 1을 붙인 값이 현재 i 번째의 값이기 때문

n = int(input())

dp = [0]*10000001
dp[1]=1
dp[2]=2

for i in range(3,n+1):
    dp[i] = (dp[i-1]+dp[i-2]) % 15746

print(dp[n])