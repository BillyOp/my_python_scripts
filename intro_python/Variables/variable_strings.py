def main():
    s = "This is a\n string"
    n = 42
    s2 = r"This is a\n string" #raw_string
    s = "This is a {} string!".format(n)
    s1 = "This is a %s string!" % n
    s4 = '''this is a string '''
    print(s)
    print(s1)
    print(s4)
    
if __name__=="__main__":main()