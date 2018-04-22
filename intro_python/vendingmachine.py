from click._compat import raw_input
from datetime import datetime
class VendingMachine():
    change = 0
    def __init__(self, name, color, weight, totalNoOfProducts, collectedCash, operationLogs, products):
        self.machine_name = name
        self.machine_weight = weight
        self.machine_color = color
        self.totalProducts = totalNoOfProducts
        self.remainingProducts = self.totalProducts
        self.collectedCash = 0.00
        self.operationLogs = False
        self.products = products
        self.cashrecieved = []
        
    def getVendingMachineName(self):
        return self.machine_name
        
    def showProducts(self):
        # to show list of products and their prices
        for product in self.products:
            print("Product Name : " + product + " " + "Product Price : " + str(self.products[product]))
            
    def recieveCash(self, paidAmount, product_pricing, product_name):
        logs = {}
        logs[product_name] = str(paidAmount) + "@" + str(datetime.now())
        self.cashrecieved.append("For product " + product_name + logs[product_name])
        self.calculateChange(paidAmount, product_pricing, product_name)
        
    def calculateChange(self, paidAmount, product_pricing, product_name):
        #calculate remaining change and return to the customer
        print("Your cash has been received and its being processe .....")
        if int(paidAmount) > product_pricing:
            change = int(paidAmount) - product_pricing
            print("Please collect your change of" + str(change) + " from the change counter")
            ischange = True
            self.showReciept(product_name, product_pricing, ischange, change)
        elif int(paidAmount) < product_pricing: 
            print("The amount you have entered is not enought to purchase the product")
            exit
        else:
            print("Thank you for service, we are glad to to be your service providers")
            change = int(paidAmount) - product_pricing
            ischange = False
            self.showReciept(product_name, product_pricing, ischange, change)
            
    def showReciept(self, product_name, product_price, ischange, changeValue):
        print("===============================================================")
        print(self.machine_name.upper() + " TRANSACTION RECIEPT DATED " + str(datetime.today()))
        print("===============================================================")
        print("PRODUCT PURCHASED | " + product_name + " PRICE " + str(product_price))
        print("CHANGE AVAILABLE |" + str(ischange) + "CHANGE VALUE" + str(changeValue))
        print("Thank you for your services esteemed client, you did quite well this time round.")
    
    def printRecievedCashLogs(self):
        for i in self.cashrecieved:
            print(i)
            
    def processSelection(self, productName, paidAmount):
        #check first if product name exist in the list
        if productName in self.products.keys():
            # continue
            product_pricing = self.products[productName]
            print("You have selected = " + productName + "it goes for " + str(product_pricing))
            return product_pricing
        else:
            print("The product you have selected does not exist in the list of products")
     


# our main class for th program..
def main():
    
    products = {
        "cocacola" : 1000,
        "fanta" : 120,
        "ice cream" : 200,
        "chocolate" : 150,
        "chrisps" : 15,
        "queen cakes" : 46,
        "cocktail" : 24,
        "cocacola" : 1000,
        "avocado" : 120,
        "nuggets" : 200,
        "sharwama" : 150,
        "apple juice" : 15
        }
    
    vendingManenoz = VendingMachine("Janta Machine", "Blue", "120kg", "12", "0", False, products)
    print("Welcome to " + vendingManenoz.getVendingMachineName() + " vending machine")
    print("You are welcomed to enjoy yourself with any product you seem to want, Just enter a coin")
    print("We offer the following products and their pricing: ")
    vendingManenoz.showProducts()
    product_name = raw_input("Select the product you want by its name: ")
    paid_amount = raw_input("Enter cash in the money pane to continue: ")
    product_pricing = vendingManenoz.processSelection(product_name, paid_amount)
    vendingManenoz.recieveCash(paid_amount, product_pricing, product_name)
    
    vendingManenoz.printRecievedCashLogs()
    
if __name__ == "__main__" : main()