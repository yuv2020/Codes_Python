#Progran to check any number which remainder is 0 on dividing any number.
'''
n=int(input("Enter the number of elements: "))
l=list(map(int,input("\nEnter the number elements in the list: ").strip().split()))
user=int(input("enter the number to check the remainder of list: "))
print("\nList is - ", l)
for num in l:
    if num%user==0:
        print(num)
        break
else:
    print("not found")
    
'''

#Program to check whether any number is prime or not.
'''
p=int(input("Enter any number to be checked is prime or not: "))
for i in range(2,p):
    if p%i==0:
        print("number is not prime")
        break
else:
    print("Number is prime")

'''

'''
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
a=b+a*b
print('a', a)
'''

# Create the array.
#from array import *
'''
vals=array('i',[5,7,9,71,36])

new_arr=array(vals.typecode,(a*a for a in vals))

# for e in new_arr:
#     print(e)

# for i in range(5):
#     print('\n',vals[i])

i=0
while i<len(new_arr):
    print("new_arr is :",new_arr[i])
    i+=1
        
print("size of the araay is:", vals.buffer_info()) 
print("type os array is:",vals.typecode)
vals.reverse()
print("reverse of array is :", vals)

'''
'''
arr=array('i',[])

n=int(input("Enter the length of array: "))
for i in range (n):
    x=int(input("Enter the next value of array: "))
    arr.append(x)
    
print("After create the array is:",arr)

val=int(input("Enter the value for search: "))

k=0
for e in arr:
    if e==val:
        print("Index no. of array is:", k)
        break
    
    k+=1
print(arr.index(val))

'''

'''
def person(name, **data):
    print(name)
    #print(data)
    for i ,j  in data.items():
        print(i,j)
person('navin', age=80, city='mumbai', mob=765490)

'''

'''
#function to reverse the order of numbers using function
a=int(input("Enter the number of first variable:")) #define the global variable.
def someting():
    a=int(input("Enter the number of second variable:")) #define the local variable.
    print("In fun:",a)
    
someting()

print("Outside of fun:", a)
'''

'''
#def function to pass the list.
def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
lst=[25,78,36,45,78,4]

even, odd=count(lst)

print("even: {} and odd: {}".format (even,odd))
# print(even)
# print(odd)
'''
'''
#Program to create the fionacc series.
def fib(n):
    a=int(input("Enter a number: "))
    b=int(input("Enter b number: "))
    
    if n==1:
        print(a)
        
    else:
        print(a)
        print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
        
fib(int(input("Enter a number up to fibonacci want to continue: ")))
'''

'''
#Program to generate the factorial of given number.
def fact(n):
    f=1
    
    for i in range(1,n+1):
        f=f*i
    return f

a=int(input("Enter a number to factorial: "))
print("The factorial of no. is: ",fact(a))
'''
 
'''
#Program to use the recursion data type.
import sys # Auto type recursin function
sys.setrecursionlimit(2000) #give the limi 
print(sys.getrecursionlimit()) #till the imit of loop of recursion

i=0
def greet():
    global i
    i+=1
    print("This is the recursion data type",i)
    greet()
    
greet()

'''        

'''
#Pogram to create the factorial using functions.
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

f=int(input("Enter the number to do the factorial :"))
result=fact(f)
print("The factorialof givn no. is :",result)
'''

'''
#Program to check the even or odd by if and else command.
import sys
n=int(input().strip())
if n%2!=0:
    print("Weird")
else:
    if n>=2 and n<=5:
        print("Not Weird")
    elif n>=6 and n<=20:
        print("Weird")
    elif n>20:
        print("Not Weird")
'''

#Anonyms define function.
'''def square(a):
    return a**2 '''
''' 
f=lambda a,b:a+b #define the lambda function without using def function.

a=int(input("Enter the value to be square:"))
b=int(input("Enter the value to be square:"))
result=f(a,b)
print(result)
'''

'''
#Using the Map,Reduce and Filter function.
# def is_even(n):
#     return n%2==0

from functools import reduce
lt=[4,5,78,34]
#lst=input("Enter the elements of a list: ")
# lt.append(lst)
even=list(filter(lambda n:n%2==0,lt)) #Using of filter function
doubles=list(map(lambda n:n*2,even)) #Using of map function 

sum = reduce(lambda a,b:a+b,doubles)
# print("List before even: ",lt)
print("After even: ",even)
print("Double of even: ", doubles)
print("Sum of all doubles: ", sum)

'''

'''
# Decorators function.
def div(a,b):
    print(a/b)
    
def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
            return func(a,b)
    return inner

div=smart_div(div)
div(2,4)
'''

"""
class car:
    wheels=4
    def __init__(self):
        self.mil=4
        self.com="BMW"
        
c1=car()
c2=car()

c1.mil=8

print(c1.mil, c1.com, c1.wheels)
print(c1.mil, c1.com, c1.wheels)

"""

"""
#how to add two numbers using class?
def solveMeFirst(a,b):

   return a+b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
res = solveMeFirst(num1,num2)
print(f"Sum of two number: {res}")
"""

'''

class student:
    school=str(input("Enter the name of school: "))
        
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        
    def get_m1(self):
        return self.m1 
        
    # def avg(self):
    #     return (self.m1+self.m2+self.m3)/3
    
    def set_m1(self,value):
        self.m1=value
        
    @classmethod
    def getschool(cls):
        return cls.school
    
    @staticmethod
    def info():
        print("This is the static method")
    
 
# m1=int(input("Enter the value of m1: "))
# m2=int(input("Enter the value of m2: "))
# m3=int(input("Enter the value of m3: "))
   

s1=student(23,45,34)
s2=student(51,92,3)

student.info()
print(student.getschool())
#print(s1.avg())

'''    
'''        
class students:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno =rollno
        self.lap=self.laptop()
        
    def show(self):
        print(self.name,self.rollno)
        
    class laptop:
        def __init__(self):
            self.brand='HP'
            self.cpu='i5'
            self.ram=300
            
        def show(self):
            print(self.brand, self.cpu, self.ram)
            
s1=students('Ram', 3)
s2=students('seeta',4)

s1.show()

l1=students.laptop()        

'''

'''
class fea:
    def feature(self):
        print("Feature 1 is working")
        
    def feature2(self):
        print("Feature 2 is working")
        
class fea1(fea):
    def feature3(self):
        print("Feature 3 is working")
        
    def feature4(self):
        print("Feature 4 is working")

    
a1=fea1()

# a1.feature()
# a1.feature2()

# b1=fea()

# b1.feature3()
# b1.feature4()
'''
'''
class Pycharm:
    def execute(self):
        print("compiling")
        print("Running")
        
class editor:
    def execute(self):
        print("Spell check")
        print("Convention check")
        print("Compile")
        print("Running the code")
        
        
class laptop:
    def code(self,ide):
        ide.execute()
        
ide=editor()
lap1=laptop()
lap1.code(ide)
'''

'''
#Program to add th efunction using operator overloading.
a=input("Enter something 1: ")
b=input("Enter something 2: ")

x=int(input("Enter value of x: "))
y=int(input("Enter value of y: "))

print(f"The addition of {a} and {b} is: ",a+b)
print(f"The sum of {x} and {y} is: ",int.__add__(x,y))

'''

"""
class std:
    def __init__(self,m1,m2) -> None:
        self.m1=m2
        self.m2=m2
    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        
        s3=std(m1,m2)
        return s3
    
s1=std(34,56)
s2=std(34,78)

s3=s1+s2

print(s3.m1)
"""

class Animal:
    def speak(self):
        print("Animal is parent class")

class Dog(Animal):
    def bark(self):
        print("dog belongs to animal class")
float=Dog()
float.bark()
float.speak()
    