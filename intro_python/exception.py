# Python Programming - Handling python exceptions
def main():
# python exception block 
    try:
        fh = open('document.txt')
    # It will be better if you specifically understand a particular exception/problem
    except FileNotFoundError as e:
        print("Such file does not exist", e)
    else:
        for lines in fh:
            print(lines.strip())
            
if __name__ == "__main__":main()