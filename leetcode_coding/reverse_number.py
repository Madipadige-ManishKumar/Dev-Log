import math as mt 
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag=0
        ran=mt.pow(2,31)
        if x!=0:
            if x<0:
                flag=1
                x=abs(x)
            x=str(x)
            x=list(x[::-1])
            for i in range(len(x)):
                if x[i]!="0":
                    break
                else:
                    x[i]=""
            x=''.join(x)
            if flag==1:
                x='-'+x
            x=int(x)
        else:
            return 0
        if ((x!=0)  and (x<ran) and (x>(-ran))):
            return x
        else:
            return 0
        return x
o=Solution()
n=o.reverse(-123)
print(n)
