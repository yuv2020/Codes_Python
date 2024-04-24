'''
import pyautogui
import time
time.sleep(4)
count=0
while count<=1000:
    pyautogui.typewrite("Hello" + str(count))
    pyautogui.press("enter")
    count=count+1
    
'''
# from numpy import *
# a=linspace(1,16.15)
# print(a)
'''
#Define functions.
def greet(): #define the function
    print("hi")
    print("How are you")
def add():
    return (x,y)

x=int(input("Enter a number:"))
y=int(input("Enter a number:"))
print("Add of two number is:", x+y)
    
greet() #calling the functions.

'''
def update(lst):
    return (lst)

lst=input("Enter the list of elements:")

print("Afer create the list of elements:", lst)
update(lst)

print("lst", lst)
     
