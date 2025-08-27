"""
Ask a number from user. Print if that number is prime or not, use
functions
"""

"""
How to check if the number is prime or not:
STEP 1: Take num as input.

STEP 2: Initialize a variable temp to 0.

STEP 3: Iterate a “for” loop from 2 to num/2.

STEP 4: If num is divisible by loop iterator, then increment temp.

STEP 5: If the temp is equal to 0,

    Return “Num IS PRIME”
"""

def isPrime(num:float)->None:
    temp = 0
    for i in range(2,num):
        if num % i == 0:
            temp += 1
        
    if temp == 0:
        print(f"{num} is a PRIME number")
    else:
        print(f"{num} is a COMPOSITE number")


isPrime(31)

def isPrime2(n: int) -> None:
    i = 1
    count = 0
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    if count == 2:
        print("Prime")
    else:
        print("Not Prime")


isPrime2(10)
isPrime2(7)

"""
def Primefactors(num):
    for i in range(1,num+1):
        if num%i == 0:
            #print(i, end=" ")
            count = 0
            for j in range(1,i+1):   # it is been always a problem not just i , write i+1
                if i % j==0:
                    count = count +1
            if count ==  2:
                print(f"Prime --> {i}")

"""