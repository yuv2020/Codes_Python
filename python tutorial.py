'''
age = [68,67]
print(age)
print(type(age))


age1 = [67]
print(age1)
print(type(age1))
age2 = list((76,75)) 
print(age2)
print(type(age2))


tup = tuple((20,30,76,45))
print(tup)
print("\ntype of tup variable ") 
print(type(tup))


my_information = list(("Dionysia",27,True,"Lemonaki",7,"Python",False))
print(my_information)
print("\ntype of my_information variable ") 
print(type(my_information))

my_info = list["Dionysia",27,True,"Lemonaki",7,"Python",False]
print(my_info)
print("\ntype of my_info variable ") 
print(type(my_info))
'''
'''
Tuple1 = tuple((28,) )
print("\nTuple1 type ") 
print(Tuple1) 

Tuple2 = ('Geeks','For') 
print("\nTuple2 type ") 
print(Tuple2) 

Tuple3 = tuple(('Geeks')) 
print("\nTuple with the use of String: ") 
print(Tuple3) 
print(type(Tuple3))

Tuple4 = ('algotechpc') 
print(Tuple4) 
print("\nTuple4 type ") 
print(type(Tuple4))

Tuple5 = tuple(('algotechpc','apc')) 
print(Tuple5) 
print("\nTuple5 type ") 
print(type(Tuple5))

Tuple4a = ('algotechpc') 
print(Tuple4a) 
print("\nTuple4a type ") 
print(type(Tuple4a))

tup5 = tuple((20,30,76,45))
print(tup5)
print(type(tup5))
'''

t =tuple(input("Enter tupele element: ").split())
print("Tuple: ",t)
print(type(t))
