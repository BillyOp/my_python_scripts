def main():
    func(3)
    func(8)
    func(9)
    func()
    
    
def func(n = 3):
    for i in range(n, 10):
        print(i, end=" ")
    print()
        
if __name__ == "__main__":main()