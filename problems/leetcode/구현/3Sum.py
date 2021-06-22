class Solution:
    def threeSum(self, arr):
        arr.sort()
        hash_map = dict()
        print(arr)

        result = []

        for i in arr:
            hash_map[i] = i

        for i in range(len(arr) - 2):
            for k in range(i + 1, len(arr) - 1):
                target = -(arr[i] + arr[k])
                if target in hash_map:
                    result.append([arr[i], arr[k], hash_map[target]])

        print(result)


a = Solution()
a.threeSum([-1, 0, 1, 2, -1, -4])
