console.log("QUESTION 1. Calculate the sum of numbers within an array")
console.log("---------------------------------------------------------")
const numberArray = [9, 2, 3,8,9];
//let sum = 0;
//for (let i = 0; i < numberArray.length; i++) {
//    sum = sum + numberArray[i];
    
//}
let sum = numberArray.reduce( (previousValue, currentValue) => previousValue + currentValue);
console.log(`The Sum  of Array ${numberArray} is ${sum}`)
