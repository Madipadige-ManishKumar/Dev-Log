class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        list=[]
        list.append([char for char in s])
        
        for i in range(len(s)):
            list1=[]
            for j in range(i,len(s)):
                str=s[i:j+1]
                if(str==str[::-1]):
                    list1.append(str)
            list.append(list1)
        return list
o=Solution()
list=o.partition("aab")
print(list)