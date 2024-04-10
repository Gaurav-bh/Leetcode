#all the susequence having sum k

def subsequnce_equal_k(arr:list,ind:int,res:list,curr:list,n:int,k:int)->None:
    if ind==n:
        s=sum(curr)
        if s==k:
            res.append(curr.copy())
        return
    
    subsequnce_equal_k(arr,ind+1,res,curr+[arr[ind]],n,k)
    subsequnce_equal_k(arr,ind+1,res,curr,n,k)


#only one subsequnce having sum k
def subsequnce_equal_k1(arr:list,ind:int,res:list,curr:list,n:int,k:int)->bool:
    if ind==n:
        s=sum(curr)
        if s==k:
            res.append(curr.copy())
            return True
        return False
    
    if subsequnce_equal_k1(arr,ind+1,res,curr+[arr[ind]],n,k):
        return True
    if subsequnce_equal_k1(arr,ind+1,res,curr,n,k):
        return True
    return False




def subsequnce_equal_k_count(arr:list,ind:int,res:list,curr:list,n:int,k:int)->int:
    if ind==n:
        s=sum(curr)
        if s==k:
            res.append(curr.copy())
            return 1
        return 0
    
    take=subsequnce_equal_k_count(arr,ind+1,res,curr+[arr[ind]],n,k)
    not_take=subsequnce_equal_k_count(arr,ind+1,res,curr,n,k)
    return take+not_take
    

if __name__=='__main__':
    arr=[1,2,1]
    k=2
    res=[]
    print(subsequnce_equal_k_count(arr,0,res,[],3,2))
    print(res)



    """
                    121
                
            

    
    """
