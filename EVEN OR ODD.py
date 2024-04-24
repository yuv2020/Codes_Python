# Program to check whether it's even or odd.
def evenodd(a):
    if(a%2==0):
        return 1
    else:
        return -1

a=int(input("Enter a number:"))
flag = evenodd(a)
if(flag == 1):
    print("Number is even")
if(flag == -1):
    print("Number is odd")

          
print("PROGRAM TO CALCULATE VOLUME OF CUBOID")

# Program to calculate the volume of cuboid.
def volume(l,w,h):
    print("Length : ", l,"\tWidth : ", w,"\tHeight : ",h)
    return l*w*h

l=int(input("Enter the Length of Cuboid:"))
w=int(input("Enter the Width of Cuboid:"))
h=int(input("Enter the Height of Cuboid:"))

print("Volume of cuboid is:" , l*w*h)


print("PROGRAM TO DESIGN THE PATTERN:")

#Program to print the pattern.
def pattern(a='%', b=6, r=1):
    for i in range(r):
        print()
        for j in range(b):
            print(a, end = ' ')

a=input("Enter the character to be displayed :")
x=int(input("Enter the number of Rows:"))
y=int(input("Enter the number of Columns:"))
pattern()
pattern(a)
pattern(a,x)
pattern(a,x-y)



print()
          
          
