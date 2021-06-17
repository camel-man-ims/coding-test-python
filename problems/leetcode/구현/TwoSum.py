class Solution:
    def twoSum(self,nums,target):
        hash_map = dict()
        for index,value in enumerate(nums):
            hash_map[value]=index
        result =[]
        for i in range(len(nums)):
            if target-nums[i] in hash_map:
                result.append(i)
                result.append(hash_map[target-nums[i]])
                return result

a = Solution()
two_sum = a.twoSum([2, 7, 11, 15], 9)
print(two_sum)