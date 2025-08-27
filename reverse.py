def reverse(num:int)->int:
    n = num # it is not recommanded to change the orginal parameter
    result = 0
    while n>0:
        lastDigit = n%10 # stores the last digit of number in the var
        result = (result * 10) + lastDigit
        n = n//10 # returns the quotient

    return result


print(reverse(3421))

"""
Q2. Make a function named checkPalindrome which accepts an integer n
from the user. Return True or False if the number is palindrome or not.

"""
def checkPalindrome(num)->str:
    if num == reverse(num):
        return f"{num} is an Palindrome"
    else:
        return f"{num} is NOT an palindrome"
    

print(checkPalindrome(1111))

print(""" wv""")
