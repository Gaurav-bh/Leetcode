def reverse_array(arr:list,n:int,i)->None:
    if i>=n:
        return
    arr[i],arr[n]=arr[n],arr[i]
    reverse_array(arr,n-1,i+1)

if __name__=='__main__':
    arr=[1,2,7,4,5,6]
    print("Before Reverse",arr)
    reverse_array(arr,5,0)
    print("After Reverse",arr)
