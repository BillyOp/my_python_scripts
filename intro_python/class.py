class Human():
#   This is a python comment....
# python class constructor showb by def __init__
    def __init__(self, n, o, s, h):
        self.name = n
        self.occupation = o
        self.skinColor = s
        self.homeTown = h
        
    def eats(self):
        print(self.name, " eats good food")
        
    def worksat(self):
        if self.occupation == "engineer":
            print(self.name, " works at an engineering/construction firm")
        elif self.occupation == "salesman":
            print(self.name, " work at a sales company selling products")
        elif self.occupation == "mechanic":
            print(self.name, " works at a car station, he repairs cars")
        else:
            print(self.name, " works everywhere")


def main():            
#Instatiating the Human Being Object
    human1 = Human("Billy Otieno", "engineer","brown", "Kisumu")
    human1.eats()
    human1.worksat()
    
if __name__ == "__main__" : main()