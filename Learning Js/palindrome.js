//Javascript Palindrome
//Takes any string that is passed through variable STRING_A and confirms
//whether it is a palindrome or not..
var string_a = "1111111111";
var string_b = "";
var string_array = [];

//console.log(string_a.charAt(0));
var checkForPalindromes = function(string_a){
	for(var i = 0; i < string_a.length; i++){
		string_array[i] = string_a.charAt(i);
	}

	var outcome = string_array.toString();
	var reversed_string = string_array.reverse().toString();

	if(outcome == reversed_string){
		console.log(string_a.toUpperCase() + " is a palindrome");
	}else{
		console.log(string_a.toUpperCase() + " is not a palindrome");
	}
}

//Invoke the javascript function
checkForPalindromes(string_a);


