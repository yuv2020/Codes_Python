n=int(input("Entter a number:"))
x=n%2
if x==0:
    print("Number is even")
    if n>x: # Nested if statement
        print("N is greater than x ")
    else:
        print("Number is less than x")
else:
    print("Number is odd")