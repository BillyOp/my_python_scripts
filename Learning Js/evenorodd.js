/**
 * @author Billy Otieno
 * @project Number tester/classification
 * @programmer OtiBi
 */

//Question One Answer
function isEvenorOdd(anyNumber){
	var number = anyNumber;
		if(number%2 == 0){
			return "even";
		}
		else{
			return "odd";
		}
}

console.log(isEvenorOdd(14));
console.log(isEvenorOdd(1));
console.log(isEvenorOdd(2112511));
console.log(isEvenorOdd(80));

console.log("\n");

//Question Two Answer
function getMaxFromNumbers(number1, number2, number3){
	if(number1 > number2){
		if(number1 > number3){
			return number1;
		}else{
			return number3;
		}
	}else{
	    if(number2 > number3){
	    	return number2;
	    }else{
	    	return number3;
	    }
	}
}

console.log(getMaxFromNumbers(34,3,21));
console.log(getMaxFromNumbers(2,2,78));
console.log(getMaxFromNumbers(1,45,11));

//Question Three Answer - Flipping Coin
function numHeads(flips){
  //Flip Coin First
  var headTailArray = new Array("H","T");
  var result;
  var headcount = 0;
  for(var initial=0; initial<flips; initial++){
	 result = headTailArray[Math.floor(Math.random()*headTailArray.length)];
	 if(result == "H"){
		 headcount = headcount + 1;
	 }
  }
  return headcount/flips;
}

console.log("\n");
console.log(numHeads(10));
console.log(numHeads(10));
console.log(numHeads(10));
console.log(numHeads(10));

function concantenationNum(times, string){
	var stringvalue = string;
	var concatenated = "";
	for(var initial = 0; initial < times; initial++){
		concatenated = concatenated + stringvalue;
	}
	return concatenated;
}

console.log(concantenationNum(2, "wewe-"));

function rolladice(){
	var dicevalues = new Array(1,2,3,4,5,6);
	var countRolls = 0;
	var getsix = 0;
	for(var initial = 0; initial >= 0; initial++){
		getsix = dicevalues[Math.floor(Math.random()*dicevalues.length)];
		//console.log(getsix);
		countRolls = initial + 1;
		if(getsix == 6){
		    break;
		}
	}
	return countRolls;
}

console.log(rolladice());



