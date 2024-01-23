def merge_sort(arr):
    if len(arr) <=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    left=merge_sort(left)
    right=merge_sort(right)
    arr=merging(left,right)
    return arr
def partition(element,key_value,desc):
    arr=[]
    for i in range(len(element)):
        arr.append(element[i][key_value])
    arr=merge_sort(arr)
    if desc:
        arr=arr[::-1]    
    return arr
def merging(left,right):
    i=0
    j=0
    sort_arr=[]
    while i<len(left) and j < len(right):
        if left[i]<right[j]:
            sort_arr.append(left[i])
            i+=1
        else:
            sort_arr.append(right[j])
            j+=1
    if i <len(left):
        sort_arr.extend(left[i:])
    elif j < len(right):
        sort_arr.extend(right[j:])
    return sort_arr
if __name__=="__main__":
    element=[
        {"name":"vedanth","age":17,"time_hours":1},
        {"name":"rajab","age":12,"time_hours":3},
        {"name":"vignesh","age":21,"time_hours":2.5},
        {"name":"chinmay","age":24,"time_hours":1.5}
    ]
    print(partition(element,"time_hours",1))

