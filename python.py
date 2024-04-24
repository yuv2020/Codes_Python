#Program to print the pattern of square shape.
n=int(input("Enter the number of range for printing the pattern:"))
for i in range(n): #No. of rows is declare by i.
    for j in range(n): #No. of columns is declare by j.
        print("#",end=" ")
    print()
        
print()


#Program to print  the pattern of decreasing triangle.
x=int(input("Enter the number of starting range:"))
for row in range(x):
    for column in range(x-row):
        print("$",end=" ")
    print()


print()


#Program to print  the pattern of right angle triangle?
x=int(input("Enter the number of starting range:"))
a=int(input("Enter the number of range : "))
for row in range(x):
    for column in range(a):
        print(row * '* ')
  
print()
  

#Program to print  the pattern of increasing triangle.
x=int(input("Enter the number of starting range:"))
for row in range(x):
    for column in range(x+row):
        print("$", end=" ")
    print()


print()



