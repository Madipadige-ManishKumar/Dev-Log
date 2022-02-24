# # Excepiton Handling 
# while(True):
#     print("Enter q To Exit ")
#     print("Enter A Value")
#     a =input("Enter A Value")
#     if a=="q":
#         break
#     try:
#         a = int(a) 
#         if (a<6):
#             print("The Entered Number Is Less Than 6")
#     except Exception as e:
#         print(e)

# print("Thanks For Playing This Game ")

# try Catch Block
# try:
#     b=int(input("enter A Integer Number"))
#     a=1/b
#     print("There is No Error")
# except:
#     print("There Is Error Occured ")

# # MultiPle Catches 
# try:
#      b=int(input("enter A Integer Number"))
#      a=1/b
# # except ValueError as e:
#      print("Catch 1")
#      print(e)
# except ZeroDivisionError as e:
#      print("Catch 2")
#      print(e)
# The Below Give Will Act as Else for Example If No Except Catch It then 
# this Block Will Called or Used we can as 
# except:
#      print("This Is  Else Of Exception ")

# Try With Else 
# try:
#      b=int(input("enter A Integer Number"))
#      a=1/b
# except ValueError as e:
#      print("Catch 1")
#      print(e)
# except ZeroDivisionError as e:
#      print("Catch 2")
#      print(e)
# # Else block :This Is Block Called When We Use The Try And Don't get The Exception
# else:
#      print("This Is Block Called When We Use The Try And Don't get The Exception")


#try  with Finallay 
# try:
#      b=int(input("enter A Integer Number"))
#      a=1/b
# except:
#      print("This Is Exception Handlong Section ")
#      exit()
# finally: # This Block Will execute what ever may be the case 
#      print("This Is Finally Block")    
#      print("we Are Done")


# Global Variable and local variable 
a=2378 #Global Variable
def ValueChange():
    # To Create A Local Variable We Use Like This
    # a=20
    global a  # global keyword is used to change the local variable to global variable 
    a=90
    print(a)
ValueChange()
print(a)

# enumerate function
# list1=[23,"sdjhv",3.14,'c']
# for index,item1 in enumerate(list1):  # Note The Enumerate Function Will print The index Value also
#     # note that you have give fisrt index and then item1
#     print(item1,index)

# list comprehensions
# a=[234,34,234,6547,756744,24,23,7,3421,342211]
# b=[]
# # Method 1 Normal Method
# # for i in a:
# #     if i%2==0:
# #         b.append(i)
# # Method 2 list comprehensions
# b=[i for  i in a if i%2==0]
# print(b)