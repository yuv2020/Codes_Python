'''   
#Program to check the palindrome series of any string using reverse function.
n=input("Enter the input to check the palindrome os string: ")

reverse=n[::-1]
if (n==reverse):
    print("yes it is palindrome")
    
else:
    print("no it is snot palindrome")
 
'''
 
'''
#Programt to check the string of palindrome using loops and and math function.
import math
a=input("Enter the input to check the palindrome: ")
isitapalindrome=0
mid=(math.floor(len(a)/2))
for i in range(0,mid):
    if(a[i]!=a[(len(a)-1-i)]):
        isitapalindrome=1
if isitapalindrome == 1:
    print("It's not a palindrome")
    
else:
    print("It is a palindrome")
'''

w=input("Enter the input: ")

def reverse(x):
    return x[::-1]

if(reverse(w)==w):
    print("The given input is a palindrome:")

else:
    print("The given input is not a palindrome")
        
