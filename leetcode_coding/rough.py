#User function Template for python3
import langchain.llms
class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        #Complete the function
        f=0
        r=0
        i=0
        len1=0
        while (f < len(arr)-1) or  (r < len(arr)-1):
            if r==len(arr):
                f+=1
                r=f
            # if sum(arr[f:r+1])==9:
            print(f,r+1,len1,sum(arr[f:r+1]))
                # print("in if",f,r)
            if int(sum(arr[f:r+1])) == k:
                print(f,r+1)
                if len1 < len(arr[f:r+1]):
                    len1=len(arr[f:r+1])
            r+=1

        return len1
        
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3

o=Solution()
print(o.lenOfLongSubarr([-16,-12,-6,5,-12,-3,2,18,12,-11,-15,-15,15,12,-1,-14,-6,1,12,1],20,9))



# } Driver Code Ends