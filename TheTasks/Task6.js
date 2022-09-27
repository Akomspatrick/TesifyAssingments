const side1 = 2
const side2 = 3
const side3 = 4
let output = ""
const myc={
    a :number,
    get:function(){
        return a

    },
    b:string
}
mm = myc{
    a:6
}
if (side1== side2 && side2===side3)
{
    output ="Equilateral Triangle"
}
else if (side1== side2 || side2===side3 || side3===side1)
{
    output ="Isosceles Triangle"
}
else
output = "Scalene Triangle"
console.log(output)