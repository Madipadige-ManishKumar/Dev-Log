class Solution {
    public int searchInsert(int[] nums, int target) {
        int l=0;
        int r=nums.length-1;
        int mid=l+r/2;
        int s=mid;
        System.out.println(l+"   "+r);
        while (l<=r)
        {
            System.out.println("The l is "+l+"  The r is "+r);
            mid=(l+r)/2;
            if(nums[mid]==target)
            {
                System.out.println("Hello s:-"+s);
                return mid;
            }
            else if(nums[mid]<target)
            {
                l=mid+1;
            }
            else if (nums[mid]>target)
            {            
                r=mid-1;
            }
        }
        System.out.println("the l is "+l+"the r is "+r);
        if (nums[l]==target)
        {
            return l;
        }
        else if (nums[r]==target)
        {
            return r;
        }
        else if(nums[l]>target)
            {
                l=l-1;
                if(l<0)
                {
                    return 0;
                }
                else
                {
                    return l;
                }
                
            }
            else if (nums[l]<target && nums[r]>target)
            {
                if (l==0)
                return (l+r/2)+1;
                else
                return (l+r)/2;
            }
            else if (nums[r]<target)
            {
                r=r+1;
                return r;
            }
        return 0;
    }
    public static void main(String[] args) {
        Solution o = new Solution();
        int arr[]= {1,3,5,6};
        System.out.println(o.searchInsert(arr, 5));
    }
}
