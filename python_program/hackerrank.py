# The Spy Life Code From SoloLearn 

# s=input("Enter The String ")
# a=""
# n=len(s)
# print (n)
# for i in range(1,n+1):
#     a+=s[n-i]
# print(a)
# b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# c="abcdefghijklmnopqrstuvwxyz"
# d=""
# for i in range(0,(len(a))):
#     for j in range(0,(len(b))):
#         if a[i]==b[j]:
#             print("1")
#             d+=b[j]
#         elif a[i]==c[j]:
#             print("2")
#             d+=c[j]

# print("The Final Result is", d)



# Secret Message Problem in sololearn 

# s=input("Enter The Message")
# a="abcdefghijklmnopqrstuvwxyz"
# c=" "
# s=s.lower()
# b=""
# for i in range(0,len(s)):
#     for j in range(0,len(a)):
#         if s[i]==a[j]:
#             b+=a[len(a)-j-1]
#         if s[i]==' ':
#             b+=" "
# print(b)


# Mathematics   (Hard_One)

# n=int(input("Enter A Number "))
# s=input("Enter The Expression")
# a="0123456789"
# b="+-*/"
# n1=0
# k=0
# l=[]
# o=0
# n2=0
# for i in range(0,len(s)):
#     for j in range(0,len(a)):
#         if s[i]==a[j]:
#             if k==1:
#                 n2=j
#                 k=0
#             else:            
#                 n1=j
#                 k=1
#         if j <4:
#             if b[j]==s[i]:
#                 o=j
#     if s[i]==")":
#         if o==0:
#             l.append(n1+n2)
#         elif o==1:
#             l.append(n1-n2)
#         elif o==2:
#             l.append(n1*n2)
#         elif o==3:
#             l.append(n1/n2)
# if n in l:
#     print(l.index(n))
# else:
#     print("none")



# Runner up score
a=int(input())
s=set()
n=(input())
l=[int(x) for x in n.split()]
l.sort()
s=set(l)
l=list(s)
print(l[a-3]) 


# Consonents and vowels
# s=input("Enter The String")
# a="aeiou"
# l=[]
# count=1
# kev=0
# stu=0
# for i in range(len(s)):
#     for j in range(len(a)):
#         n=int(j)
#         n=int(n)
#         if(s[i]==a[j]):
#             l.append(s[i])
#             while (j+count) <= (len(s) -1):
            
#                 kev+=s.count(s[i:i+count])
#                 print(s[i:i+count],s.count(s[i:i+count]))
#                 count=count+1

# print(kev)