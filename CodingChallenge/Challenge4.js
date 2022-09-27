stop=4
start=1
console.log(`4. Print a multiplication tables between ${start} and ${stop}`)
console.log('-------------------------------------------------------------------------------')

//line =""
space=4
for (i=start ; i< stop; i++)
{ 
    line =""
  for (j=start; j< stop;j++)
  {
    
    
    product =(i*j).toString().padStart(space,' ')
    line = `${line }   ${product}  `
  }

  console.log(line)
}