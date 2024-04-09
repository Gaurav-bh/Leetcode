def print_N(Num:int)->None:
    if Num==0:
        return 
    print_N(Num-1)
    print(Num)

if __name__=='__main__':
    print_N(5)