console.log("1. Calculate the sum of numbers within an array")
console.log("-----------------------------------------------")
let numberArray = [9, 2, 3];
let sum = numberArray.reduce( (previousValue, currentValue) => previousValue + currentValue);
console.log(`The sum of the number withing array ${numberArray} is ${sum}`);
console.log('***********************************************************************************')
console.log('***********************************************************************************')

console.log("2. Create a length converter function")
console.log('---------------------------------------')
console.log('***********************************************************************************')
console.log('***********************************************************************************')


console.log("3. Print all even numbers from 0 – 10")
console.log('---------------------------------------')
const myArray=[0,1,2,3,4,5,6,7,8,9,10]

evenNos=myArray.filter(e=>(e%2 ===0))
evenNos.forEach( e => console.log(e))
console.log('***********************************************************************************')
console.log('***********************************************************************************')

console.log("4. Print a table containing multiplication tables")
console.log('---------------------------------------')
stop=10
start=1
line =""
space=4
for (i=start ; i< stop; i++)
{ line =""
  for (j=start; j< stop;j++)
  {
    product =(i*j).toString().padStart(space,' ')
    line = `${line }   ${product}  `
  }

  console.log(line)
}
console.log('***********************************************************************************')
console.log('***********************************************************************************')



console.log('---------------------------------------')
console.log("5.Create a function that reverses an array")
sampleData=["Ade",'Ojo',"Titus","Ajayi","Gabriel","Blessing"]

reverse = function(myarray)
{
    for(i =myarray.length-1; i >-1;i--)
    console.log(myarray[i])
}

reverse(sampleData)
console.log('***********************************************************************************')
console.log('***********************************************************************************')

console.log("6. Sort an array of strings in alphabetical order")
console.log('------------------------------------------------')
sampleData=["Ade",'Ojo',"Titus","Ajayi","Gabriel","Blessing"]
sampleData2=[10,4,2,9,4,7,2,1,90,23,45,56]
console.log('***********************************************************************************')
console.log('***********************************************************************************')



console.log("7. Sort an array of numbers in descending order")
console.log('-----------------------------------------------')
numArray = sampleData2.sort( (a, b) => a - b);
console.log(numArray.reverse())
console.log('***********************************************************************************')
console.log('***********************************************************************************')





console.log('------------------------------------------------')
console.log("8.Return a Boolean if a number is divisible by 10")
console.log("8.To return True if the remainder is zero after division by 10")

IsDivisiblebyTen= (num) =>(num %10 ===0)
nos=9
console.log(` The Number ${nos} is divible by 10 : ${IsDivisiblebyTen(nos)}`)

console.log('***********************************************************************************')
console.log('***********************************************************************************')


console.log('---------------------------------------')
console.log("9. Return the number of vowels in a string")
countVowel= (str) => str.match(/[aeiou]/gi).length;
let words= 'Vivian'
console.log(`The number of vowels in ${words} is ${countVowel(words)}`)
console.log('***********************************************************************************')
console.log('***********************************************************************************')


console.log('---------------------------------------')
console.log("10. Create  a  function  that  filters  out  negativenumbers")
const myAllArray=[0,1,-2,3,4,-5,6,7,-8,9,10]
evenNos=myAllArray.filter(e=>(e>0))
evenNos.forEach( e => console.log(e))
console.log('***********************************************************************************')
console.log('***********************************************************************************')



