# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        
        n=(len(nums1))//2
        
        if(len(nums1)%2==0):
            n=float(nums1[n-1]+nums1[n])/2
        else:
            n=float(nums1[n])
        return n
        
        
O=Solution()
n=O.findMedianSortedArrays([1,2],[3,4])
print(n)