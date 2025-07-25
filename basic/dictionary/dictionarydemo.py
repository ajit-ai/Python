# Creating a Dictionary
d = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("Creating Dictionary: ")
print(d)

# accessing a element using key 
print("Accessing a element using key:") 
print(d['Name']) 

# accessing a element using get() 
# method 
print("Accessing a element using get:") 
print(d.get(1)) 

# creation using Dictionary comprehension
myDict = {x: x**2 for x in [1,2,3,4,5]}
print(myDict)
