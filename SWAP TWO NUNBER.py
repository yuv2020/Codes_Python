#Program to swap the two no.s without using third variable.
a=int(input("Enter first no.:"))
b=int(input("Enter second no.:"))
print("Before swapping two no. is :",a,b)
c=a
a=b
b=c
print("After swapping teh two no.:", a,b)

print()

#Program to swap the two no.s using third variable.
a=int(input("Enter first no.:"))
b=int(input("Enter second no.:"))
print("Before swapping two no. is :",a,b)
a=a+b
b=a-b
a=a-b
print("After swapping teh two no.:", a,b)
