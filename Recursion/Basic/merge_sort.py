def merge(arr:list,l:int,mid:int,r:int)->None:
    #print("l,mnid,r ",l,mid,r)
    temp1=arr[l:mid+1]
    temp2=arr[mid+1:r+1]
    #print("arr",temp1,temp2)
    
    size1=mid-l+1
    size2=r-mid
    #print("size",size1,size2)
    i=0
    j=0
    res=[]
    while i<size1 and j<size2:
        if temp1[i]<temp2[j]:
            res.append(temp1[i])
            i+=1
        else:
            res.append(temp2[j])
            j+=1
    while i<size1:
        res.append(temp1[i])
        i+=1
    while j<size2:
        res.append(temp2[j])
        j+=1
    size=len(res)
    i=0
    while i<size:
        arr[l+i]=res[i]
        i+=1

def mergesort(l,r,arr):
    #print(l,r)
    if l<r:
        mid=(l+r)//2
        mergesort(l,mid,arr)
        mergesort(mid+1,r,arr)
        merge(arr,l,mid,r)

if __name__=='__main__':
    arr=[4,3,9,5,6,7,1]
    mergesort(0,6,arr)
    print(arr)

