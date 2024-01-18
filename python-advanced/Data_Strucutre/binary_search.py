def binary_search(arr,key):
    if len(arr) ==1:
        if arr[0]==key:
            return 0
        else:
            return -1000
    mid=len(arr)//2
    if key==arr[mid]:
        return mid
    elif key<arr[mid]:
        return binary_search(arr[:mid],key)
    elif key>arr[mid]:
        return mid+binary_search(arr[mid:],key)
if __name__ =="__main__":
    arr=[1,2,3,4,5,6,7,8,9,10]
    n= binary_search(arr,3)
    if n<0:
        print("Not Found")
    else:
        print(n)
