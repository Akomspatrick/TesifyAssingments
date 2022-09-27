
console.log("5.Create a function that reverses an array")
console.log('------------------------------------------')
sampleData=["Ade",'Ojo',"Titus","Ajayi","Gabriel","Blessing"]
reversed=[]
reverse = function(myarray)
{


    for(i =myarray.length-1; i >-1;i--)
    reversed.push(myarray[i])
}
reverse(sampleData)
console.log(`The original   array is  ${sampleData}`)
console.log(`The reversed   array is  ${reversed}`)



console.log('***********************************************************************************')
console.log('')
console.log('')
console.log('')