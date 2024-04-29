def sum(n:int)->int:
    if n==1:
        return 1
    return n+sum(n-1)
if __name__=='__main__':
    s=sum(4)
    print(s)