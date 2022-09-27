console.log("3. Print all even numbers from 0 – 10")
console.log('---------------------------------------')

const myArray=[0,1,2,3,4,5,6,7,8,9,10]

//evenNos=myArray.filter( e =>( e%2 === 0) )
evenNos=[]
for (let i = 0; i < myArray.length; i++) {
 
    if (myArray[i]%2 ===0)
    {
        evenNos.push(myArray[i])
    }
}
console.log(`The even numbers  in ${myArray} are  ${evenNos}`)