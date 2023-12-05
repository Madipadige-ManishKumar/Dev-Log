class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l=set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    l2=[]
                    if k ==i or k ==j or i==j:
                        continue
                    else:
                        if nums[i]+nums[j]+nums[k] == 0:
                            l2=[nums[i],nums[j],nums[k]]
                            l2.sort()
                            l.append(l2)       
        lm=set(map(tuple,l))
        l=list(map(list,lm))
        return l
o= Solution()

o.threeSum([-12,0,6,-13,-7,-15,-6,-6,-2,-14,-2,14,1,11,-12,-11,-2,-6,7,2,-5,-9,-11,-13,9,-7,-8,9,-12,-1,5,14,14,-3,8,14,-3,-13,-14,3,10,-1,2,-3,-13,-3,-7,-7,-2,-15,2,8,-9,7,2,8,7,2,2,11,-14,-8,2,7,-4,-5,7,9,-11,0,-11,-15,14,6,-11,9,-11,-3,9,-6,-11,-4,-12,-4,10,5,11,-5,-8,-2,13,-7,-3,0,-14,1,10,0,-5,6,-15,-1,6,6])