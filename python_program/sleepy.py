# program to find x as input and log x base 2 as output 
import math
def log_base_2(x):
    if x <= 0:
        return "Error: Logarithm is undefined for non-positive numbers."
    else:
        return math.log2(x)

# Example usage:
# 0       1   
a1=[[2,1],[2,1],[1,2],[0,3],[2,1],[1,2],[2,1],[1,2],[1,2],[1,2],[1,2]]
b0=[[0,2],[2,0],[2,0],[1,1],[2,0],[1,1],[1,1],[2,0],[1,1],[0,2],[1,1]]



k=0
res=[]
h=1
for i ,m in zip(a1,b0):
    for j in range(len(i)):
        r=(i[j]+m[j])
        p=(i[j]/r)
        q=(m[j]/r)
        re1=0.9709505944546686
        if (i[j]==0):
            p=0
        else:
            p=p*log_base_2(p)
        if (m[j]==0):
            q=0
        else:
            q=q*log_base_2(q)
        res.append(0-p-q)
        k=k+1
        if k==2:
            k=0
            totalresult=re1-(p*res[0])-(q*res[1])
            print(f"Attribute {h} = {totalresult}")
            h+=1
            res.clear()