def sum(n:int,su:int)->None:
    if n==0:
        print(su)
        return 
    return sum(n-1,su+n)
if __name__=='__main__':
    sum(4,0)
    