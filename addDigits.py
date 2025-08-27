def addDigits(num):
    temp = num
    total = 0
    while(temp > 0):
        total = total + temp % 10
        temp = temp//10

    print(total)
    print()

addDigits(3421)
