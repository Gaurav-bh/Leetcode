def subsequence(i:int,n:int,arr:list,res:list,curr:list)->None:
    if i==n:
        res.append(curr.copy())
        return 
    subsequence(i+1,n,arr,res,curr)
    subsequence(i+1,n,arr,res,curr+[arr[i]])

if __name__=='__main__':
    arr=[3,1,2]
    n=3
    res=[]
    subsequence(0,3,arr,res,[])
    print(res)
        