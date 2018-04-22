class Egg:
    def __init__(self, kind = "fried"):
        self.kind = kind
    def what_kind(self):
        return self.kind

def main():
    eggObject = Egg()
    eggScrambled = Egg("Scrambled")
    print(eggObject.what_kind())
    print(eggScrambled.what_kind())
    
if __name__ == "__main__":main()