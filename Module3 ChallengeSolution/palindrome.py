#5.	Write  a  Python  program  that  checks  if  a  string  is  a palindrome,
# Then  optionally  write  a  unit  test  to  check your program's correctness.

def checkpalindrome(word):
    return str(word == word[::-1])

word= 'Patrick'
print(word +' is palindrome :' + checkpalindrome(word))

word= 'ADA'
print(word +' is palindrome :' + checkpalindrome(word))