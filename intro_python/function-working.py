# python functions
def main():
    testfunction()
    # Sums both of the arguments
    function_with_values(15, 14)
    # You can create any number of arguments in this
    arbitrary_arguments(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
    keyword_arguments(name = 'billy', address ='2131321', phone ='0715805770', feedback ='good')
    
    for i in return_func():
        print(i, end=",")
    
def testfunction():
    print("I am the test function")
    
def donothingfunction():
    pass

def function_with_values(initialized_arg = 0, variable = None):
    print(initialized_arg + variable)
    
def arbitrary_arguments(*args):
    for items in args:
        print(items, end=" ")
        
def keyword_arguments(**kwargs):
    for k in kwargs:
        print(k, kwargs[k])
        
def return_func():
    return range(100)

    
if __name__=="__main__":main()