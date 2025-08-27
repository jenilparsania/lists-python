"""
Q1. Make your own list of numbers. Ask a start and end position from User.
Print the list from start position to end position using without using Slicing

"""
a = [4,5,1,2,45,69,21,"Jenil",915,45,96,96,7,100,99]
b = []

start = int(input("Enter the start position : "))
end = int(input("Enter the end position : "))

if start < end:
    for i in range(start,end+1):
        b.append(a[i])
else:
    for i in range(start+1,end,-1):
        b.append(a[i])

print(b)