/**
 * Recapping Javascript Development - Always have to remind yourself the hustle is real...
 * Document by Billy Otieno.
 */
console.log("Welcome to Javascript Software Development");

function Apple(type){
	this.color = "green";
	this.shape = "circle";
	this.price = 10.20;
	this.getDetails = getAppledetails;
	this.setDetails = setAppledetails;
}

function getAppledetails(){
	return "The apple details are " + this.color + " " + this.shape + " " + this.price;
}

function setAppledetails(color, shape, price){
	this.color = color;
	this.shape = shape;
	this.price = price;
}

var greenapple = new Apple();

//Displaying the output of the javascript instance...
console.log(greenapple.getDetails());

greenapple.setDetails("red","square", 142.3);
console.log(greenapple.getDetails());

