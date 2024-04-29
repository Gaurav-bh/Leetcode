def palindrome(i:int,n:int,s:str)->bool:
    if i>=(n-i-1):
        return True
    if s[i]==s[n-i-1] and palindrome(i+1,n,s):
        return True
    return False

if __name__=="__main__":
    s="abc"
    print(palindrome(0,3,s))