//Javascript Loops
var days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
console.log(days_of_the_week);

//A do..while for printing days..
var i = 0;
do{
   console.log("Today is on " + days_of_the_week[i++])
   document.write(days_of_the_week[i++]);
}while(i < days_of_the_week.length);

