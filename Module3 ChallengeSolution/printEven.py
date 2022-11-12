#8.	Create a program that prints out the even numbers in an array.
# Sample array: a. [1, 2, 3, 4, 5, 6] b. [ 34, 2, 9, 91, 19,401, 0 ]
def Iseven(num):
    return (num % 2) ==0

def returnEvenArray(myarray):
    temp=[]
    for value in myarray:
        if Iseven(value):
            temp.append(value)
    return  temp

print(returnEvenArray([1, 2, 3, 4, 5, 6] ))
print(returnEvenArray([ 34, 2, 9, 91, 19,401, 0 ]))