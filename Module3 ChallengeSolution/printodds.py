#7.	Create a program that prints out the odd numbers in an array.
# Sample array: a. [1, 2, 3, 4, 5, 6] b. [ 34, 2, 9, 91, 19,401, 0 ]

def Isodd(num):
    return (num % 2) !=0

def returnOddArray(myarray):
    temp=[]
    for value in myarray:
        if Isodd(value):
            temp.append(value)
    return  temp

print(returnOddArray([1, 2, 3, 4, 5, 6] ))
print(returnOddArray([ 34, 2, 9, 91, 19,401, 0 ]))