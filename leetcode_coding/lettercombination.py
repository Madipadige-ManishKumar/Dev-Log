# class Solution(object):
#     def letterCombinations(self, digits):
#         """
#         :type digits: str
#         :rtype: List[str]
#         """
#         if digits =="":
#             return []
#         all=[[],[],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
#         d=str(digits)
#         num=[]
#         for i in range(len(d)):
#             num.append(all[int(d[i])])
#         result=[]
#         if len(num)==2:
#             result=[]
#             for i in range(len(num[0])):
#                 for j in range(len(num[1])):
#                     result.append(str(num[0][i])+str(num[1][j])) 
#         elif len(num)==1:
#             result=[]
#             result=num[0]
#         elif len(num) ==3:
#             result=[]
#             for i in range(len(num[0])):
#                 for j in range(len(num[1])):
#                     for k in range(len(num[2])):
#                         result.append(str(num[0][i])+str(num[1][j])+str(num[2][k]))
#         elif len(num)==4:
#             result=[]
#             for i in range(len(num[0])):
#                 for j in range(len(num[1])):
#                     for k in range(len(num[2])):
#                         for l in range(len(num[3])):
#                             result.append(str(num[0][i])+str(num[1][j])+str(num[2][k])+str(num[3][l]))
#         return result
            
class Solution(object):
    def letterCombinations(self, digits):
        
        phoneMap = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        if digits == "":
            return []
        output = []

        def backtrack(currentResult, i):
            if i > len(digits) - 1:
                output.append(currentResult)
                return
            
            for char in phoneMap[digits[i]]:
                backtrack(currentResult + char, i+1)

O=Solution()
n=O.letterCombinations("234")
print(n)

