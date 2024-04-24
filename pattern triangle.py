#Program to create pattern of triangle by user input value?
row = int(input('Enter how many lines? '))
print("*") # first empty line
for i in range(1,row+1):
    print("*", end='')
# increase
    for j in range(1,i+1):
        print(j, end='')

#  decreasing  
    for j in range(i-1,0,-1):
        print(j, end='')
    print("*")

# Decrease
for i in range(row-1, 0, -1): # row-1 to avoid repeating the longest row
    print("*", end='')

    for j in range(1,i+1):
        print(j, end='')

    for j in range(i-1,0,-1):
        print(j, end='')
    print("*")
print("*") # last empty line




#Source: https://stackoverflow.com/questions/70580876



for i in range(1,6):
    for j in range(6-i):
        print(" ", end="")
    for j in range(i):
        print("*", end=" ")
    print()







