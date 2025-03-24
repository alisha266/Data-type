# Text type
name = "Alisha"
print("Name :",name.upper())  # using string method

#Numeric Type
age = 24
print ("age after 5 years :", age + 5 )

weight = 45.6
print ("weight :", weight) # float type

z = 4 + 3j
print ( "Complex number :", z)
print ( "real number:", z.real , "imagenary number :", z.imag) # complex type


# sequence type
fruits = ["apple" , "banana" , "cherry"]
fruits.append ("orange")
print ( "Fruits :", fruits) # list type

coordinates = (10.5, 20.8)
print ("Coordinate : " , coordinates[0]) # tuple type

for i in range (3,8):
    print ( "Number in range :", i) # range type

# Mapping Type
student = {"name" : "Alisha", "age" : 21, "Major" : "Computer Science" }
print ( "Student Name :", student ["name"])
student ["age"] += 1
print ("upgrade age of student :", student ["age"] ) # dict type

# Set type
number = {1,3,4}
number.add (2)
print ("Set :", number)

frozen = frozenset([8,7,6])
print ("frozenset :", frozen) # frozenset type

# bool type
is_tired = True
if not is_tired:
    print ( "Let's work more ")

# Binary type
byte_data = b"hello"
print ("Byte :" , byte_data)

#bytearray type
ba = bytearray([65,66,67])
ba[0]= 90
print ("Bytearray :" , ba )

mv = memoryview (byte_data)
print ("first byte in memoryview :", mv[0]) # memoryview type

# None example 1
result = None
if result is None:
    print ("No result yet, still processing")

 # None example 2
logged_in_user = "Alisha"

if logged_in_user is None:
    print("No user is logged in. Please log in first.")
else:
    print(f"Welcome back, {logged_in_user}!")








