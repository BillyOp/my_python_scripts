//Designing a vending machine with all its functionalities with Javascript...
//Programmer: OtiBi
/*
 * Objects: Product, Money, Vending Machine
 */

//The product class
function Product(pname, pvalue, pcode){
     this.name = pname;
     this.value = pvalue;
     this.shelfcode = pcode;
     this.setProductName = function(productname){
    	  this.name = productname;
     }
     this.getProductName = function(){
    	 return this.name;
     }
     this.getProductValue = function(){
    	 return this.value;
     }
}

//The money class
function Money(mvalue, mtype, mcode){
	this.code = mcode;
	this.value = mvalue;
	this.type = mtype;
	this.getMoneyValue = function(){
		return this.value;
	}
	this.setMoneyValue = function(moneyvalue){
		this.value = moneyvalue;
	}
}

//The vending machine class
function VendingMachine(vname){
    
	productsArray = new Array();
    moneyArray = new Array();
    this.name = vname;
    
    this.enterNewProduct = function(pname, pvalue, pcode){
       var product = new Product(pname, pvalue, pcode);
       productsArray.push(product);
       console.log("New product has been added to the list of products. View below");
//     Display the new list of products..
    }
    
    this.enterNewCostCodes = function(mvalue, mtype, mcode){
       var money = new Money(mvalue, mtype, mcode);
       moneyArray.push(money);
       console.log("New money code has been configured in the Vending Machine");
    }
    
    this.enterProductCode = function(code){
    	console.log("Enter the code of the product you need: ");
    	var product_code = "DDD";
    	var code_exist = false;
    	
    	//Check in product array is product with the code exist
    	for(index=0; index<productsArray.length; index++){
    	   if(productsArray[index].shelfcode == product_code){
    		   this.enterCash(productsArray[index]);
    		   code_exist = true;
    		   break;
    	   }
    	}
    	
    	if(code_exist == false){
    		console.log("There is no product with Such a code, Kindly confirm and reenter");
    	}
    }
    
    this.displayProducts = function(){
    	for(index = 0; index < productsArray.length; index++){
    		console.log("Product Name " + productsArray[index].name);
    		console.log("Product Code " + productsArray[index].shelfcode);
    		console.log("Product Value " + productsArray[index].value);
    		console.log("============================================");
    	}
    }
    
    this.enterCash = function(productObject){
        console.log("The cost of " + productObject.name + " is " + productObject.value +". Enter your money code to transact: ");
        var moneyCode = "Four";
        var code_exist = false;
        
        //Check in money array is money with the code exist
        for(index = 0; index<moneyArray.length; index++ ){
        	if(moneyArray[index].code == moneyCode){
        		this.checkMoneyValue(moneyArray[index], productObject);
        		code_exist = true;
        		break;
        	}  
        }
        
        if(code_exist == false){
        	console.log("The money code you have entered in the system does not exist. Kindly Confirm")
        }
        
//		This is a classical recursive function --- a function that calls itself..
//		this.enterCash();
    }
    
    this.transactionClearedMessage = function(message){
    	console.log(message);
    	console.log("Thank you for trusting in our services");
    }
    
   this.requestForMoreMoney = function(){
	   console.log("Please add more money for you to acquire the product you need");
   }
    
   this.checkMoneyValue = function(money, product){
      //Compare product value against what the value of the money entered..
      var money_value = money.getMoneyValue();
      var product_value = product.getProductValue();
      
      if(product_value == money_value){
    	  var message = "Zero balance Transaction processed Successfully"
    	  this.processTransaction(product);
    	  this.transactionClearedMessage(message);
      }else if(product_value > money_value){
    	  var balance = product_value - money_value;
    	  var message = "Please add " + balance + " Ksh. More";
    	  this.requestForMoreMoney();
      }else if(product_value < money_value){
    	  var balance = money_value - product_value;
    	  this.processTransaction(product);
    	  var message = "Wait for Your balance of " + balance + " in the money output";
    	  this.transactionClearedMessage(message);
      }
      else{
    	  console.log("Gone beyond the pricing scope");
      }
    }
   
   this.processTransaction = function(product){
	   console.log("Your product " + product.getProductName() + ", Will come from containment AB2");
   }
}

var vendingMachineSession = new VendingMachine("CocaCola Vending Machine");
vendingMachineSession.enterNewProduct("Chai Moto", 100, "AAA");
vendingMachineSession.enterNewProduct("Coca Cola", 400, "BBB");
vendingMachineSession.enterNewProduct("Chapati", 150, "CCC");
vendingMachineSession.enterNewProduct("Pepsi Cola", 50, "DDD");
vendingMachineSession.enterNewProduct("Fruit Juice", 130, "EEE");
vendingMachineSession.enterNewProduct("Milk", 100, "FFF");
vendingMachineSession.enterNewProduct("Banana", 1500, "GGG");
vendingMachineSession.enterNewProduct("Honey Jar", 896, "HHH");

vendingMachineSession.enterNewCostCodes(1000, "Note", "One");
vendingMachineSession.enterNewCostCodes(2000, "Note", "Two");
vendingMachineSession.enterNewCostCodes(3000, "Coin", "Three");
vendingMachineSession.enterNewCostCodes(4000, "Note", "Four");
vendingMachineSession.enterNewCostCodes(5000, "Coin", "Five");
vendingMachineSession.enterNewCostCodes(6000, "Coin", "Six");


vendingMachineSession.displayProducts();
//May the activities begin now..
vendingMachineSession.enterProductCode();

 
