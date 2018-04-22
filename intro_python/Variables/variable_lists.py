def main():
    x = (1,2,3) #tuple
    for i in x:
        print(i)
    print(type(x), x)
    
    x = [1,2,3] #list
    y = []
    y.append(3)
    x.append(6)
    x.insert(0, 7)
    x.insert(4, 9)
    x.insert(7, 12)
    x.insert(2, 2)
    print(x.count(2))
    print(type(x), x)
    print(type(y), y)
    
    x = 'string'
    for i in x:
        print(i)
    print(type(x), x[2:4])
    
if __name__ == "__main__":main()