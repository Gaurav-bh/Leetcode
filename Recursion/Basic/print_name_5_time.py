def printName(name:str,times:int)->None:
    if times==0:
        return
    print(name)
    printName(name,times-1)
if __name__ == '__main__':
    printName("Gaurav",5)
