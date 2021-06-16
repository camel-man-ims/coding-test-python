# 21.05.19
# 배열파티션 1
# 두 개의 수 중에서 최소값을 return 할 때, 만들 수 있는 최대 합

class Solution:
    def arrayPairSum(self, nums):
        nums.sort()
        result = 0
        for i in range(len(nums)):
            if i%2==0:
                result += nums[i]
        return result

a = Solution()
pair_sum = a.arrayPairSum([6,2,6,5,1,2])
print(pair_sum)