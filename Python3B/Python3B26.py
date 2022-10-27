
#Create a test case that compares two strings

#Create another test case that compares different numbers

def StringCompare(firstString, secString):
    if isinstance(firstString, str) and isinstance(secString, str):
        return firstString == secString
    return False

def NumberCompare(firstnum ,secNum):
    if  not (isinstance(firstnum,str)) and  not isinstance(secNum,str) and str(firstnum).isnumeric  and str(secNum).isnumeric:
        return firstnum == secNum
    return False

print (StringCompare(4,4))
print (StringCompare('4','4'))
print (StringCompare(5,4))
print (StringCompare('5','4'))

print (NumberCompare(4,4))
print (NumberCompare('4','4'))
print (NumberCompare(5,4))
print (NumberCompare('5','4'))