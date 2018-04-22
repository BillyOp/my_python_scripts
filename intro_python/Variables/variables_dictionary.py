def main():
    d = {'one':1,
         'two':2,
         'three':3,
         'four':4,
         'five':5
         }
    
    #unsorted
    for k in d:
        print(k, d[k])
     
    #sorted    
    for k in sorted(d.keys()):
        print(k, d[k])
        
    d = dict(
        one = 2, two = 2, three = 3, four = 5, five = 'five')
        
    for k in sorted(d.keys()):
        print(k, d[k])
        
    d['seven'] = 7
    
    for k in sorted(d.keys()):
        print(k, d[k])
           
if __name__ == "__main__":main()