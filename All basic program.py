#Program to check the number that it is -ve,+ve and zero.
n=int(input("Enter the number: "))
if n<0:
    print("The number is negative")
elif n==0:
    print("The number is zero")
elif n>0:
    print("The number is +ve")
    
print()

#Program to check the number is even or odd.
print("Nocheck is even or odd")
n=int(input("Enter the number: "))
if n%2==0:
    print("True no. is even")
else:
    print("False no. is odd")
    
print()

#Program to prints the number of seconds in a year.
print("Leap year calculate for seconds in a year.")
print("No. of seconds in a year_ _ _ _")
print(60*60*24*366)
print("For non-leap year_")
print(60*60*24*365)