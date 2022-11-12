#4.	Writing  a  well-documented  code  creates  a  function  that calculates simple interest
# Documentation does not only mean adding comment but making the code readable and self explanatory



def simple_interest(pricipal, thetime, rate):

    si = (pricipal * thetime * rate) / 100

    return si



print('The Simple Interest is', simple_interest(8, 6, 8))