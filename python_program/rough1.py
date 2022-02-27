class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=l+1
        c=0
        while l<len(nums) and r<len(nums):
            if nums[r]=="_" or  nums[l]=="_":
                return c+1
            if nums[l] == nums[r]:
                nums.pop(l)
                nums.append("_")
                c+=1
            else:
                l=r
                r=r+1
        c= int(len(nums))-c+1
        return c
o =Solution()
print(o.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))