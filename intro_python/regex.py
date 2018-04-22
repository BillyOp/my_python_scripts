import re 


def main():
    fh = open('raven.txt')
    for line in fh:
        if re.search('', line):
            print(line, end='')
            
if __name__ == '__main__':main()