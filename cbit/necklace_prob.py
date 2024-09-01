if __name__ =="__main__":
    n=int(input("Enter the Number of Test Cases "))
    arr=[]
    result=[]
    for i in range(n):
        n1=int(input("Enter the size"))
        k=int(input("Enter k value"))
        arr=[]
        arr1=[]
        arr2=[]
        for i in range(n1):
            n3=int(input("Enter the number"))
            arr.append(n3)
        arr1=arr[:k]
        arr2=arr[k:]
        arr1.reverse()
        arr2.reverse()
        arr=arr1+arr2
        arr.reverse()
        result.append(list(arr))
    for i in result:
        print(i)
