#2.	Create  a  function  that  calculates  the  power  of  a  number. Then  write  a  unit  test  to  check  the  correctness  of  the function

def powerfunc(base ,exponent):
    result = 1
    for exponent in range(exponent, 0, -1):

        result *= base
    return  result

#print("Answer = " + str(powerfunc(2,3)))
#print("Answer = " + str(powerfunc(3,4)))