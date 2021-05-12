class Solution:
    def twoSum(self,nums,target):
        result = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    result.append(i)
                    result.append(j)
                    result.sort()
        return result
a = Solution()
two_sum = a.twoSum([2, 7, 11, 15], 9)
print(two_sum)