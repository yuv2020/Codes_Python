#Program to create the bodmas to calculate two no. by user mind.
#This function is to add two no.
def add(num1,num2):
    return num1+num2

#This function is to subtract two no.
def subtract(num1,num2):
    return num1-num2

#This function is to multiply two no.
def multiply(num1,num2):
    return num1*num2

#This function is to divide two no.
def divide(num1,num2):
    return num1/num2

print("Please select the operation:")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")
print("5.Input value is invalid:")

while True:
    #Take the input value from teh user.
    choice=input("Enter the choice of your operation:1 /2 /3 /4 /5: ")
    
    #Check if the choice is one of our choicesfrom five options.
    if choice in('1','2','3','4','5'):
        try:
            num1=float(input("Enter first number:"))
            num2=float(input("Enter second number:"))
        except ValueError:
            print("Invalid input. Please input a number:")
            continue
        if choice=='1':
            print(num1, "+", num2, "=", add(num1+num2))
            
        elif choice=='2':
            print(num1, "-", num2, "=", subtract(num1-num2))
            
        elif choice=='3':
            print(num1, "*", num2, "=", multiply(num1*num2))
            
        elif choice=='4':
            print(num1, "/", num2, "=", divide(num1/num2))
            
        else:
            print("You input invalid number")
'''            
#Check if user wants to do anoter calculation.
#break the while loop if user don't want to do.
next_calculaton=input("Let's do another calculation? (Yes/No):")
if(next_caculation == "No"):
    b
else:
    print("Input is invalid")        
    
'''