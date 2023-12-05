class Solution:
    
    def twoSum(self, nums: List[0], target: int) -> List[1]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # No solution found

l=[2,7,11,15]
t=9
o=Solution()
ml=o.twoSum(l,t)
print(ml)

