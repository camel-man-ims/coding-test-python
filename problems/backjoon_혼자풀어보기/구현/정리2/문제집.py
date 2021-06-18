# 21.06.18
# 위상정렬을 이용해서 풀어야한다
# 나는 다르게 풀려다가 실패

n,m = map(int,input().split())

arr = []

for _ in range(m):
    a,b = map(int,input().split())
    arr.append([a,b])

arr.sort()

nums = []

for i in range(1,n+1):
    nums.append(i)

for num_arr in arr:
    first = num_arr[0]
    second = num_arr[1]

    index_first = 0
    index_second = 0

    for i in range(len(nums)):
        if nums[i]==first:
            index_first=i
        if nums[i]==second:
            index_second=i

    nums[index_second],nums[index_first] = nums[index_first],nums[index_second]
    nums.insert(index_second+1,nums[index_first])
    nums.pop(index_first+1)

for i in nums:
    print(i,end=' ')