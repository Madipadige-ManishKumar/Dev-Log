class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {'I': 1, 'V': 5, 'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum = 0
        i=1
        while i<len(s):
            #print(f"The I value at the starting {i}")
            if roman_dict[s[i]]>roman_dict[s[i-1]]:
                sum=sum +(roman_dict[s[i]]-roman_dict[s[i-1]])
                #print("In The If Block ")
                #print(f"The Sum is {sum} ")
                if i != len(s):
                    i=i+1
            else:
                #print("In the Else block ")
                sum=sum+roman_dict[s[i-1]]
                #print(f"The Sum is {sum}")
            #print(f"The value of i is {i} at the end ")
            i=i+1
        if i ==len(s):
            sum=int(sum+roman_dict[s[len(s)-1]])
        print(sum)
        return int(sum)
    

            
O=Solution()
O.romanToInt("MCMXCIV")
            