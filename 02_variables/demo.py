# Variables

student_age = 20
student_gpa = 8.5
student_name = "Ravi"
student_passed = True
student_attendance = 20

student_one_marks = [80,90,100]
student_two_marks = [80,90,100]

print(student_age)
print(student_gpa)
print(student_name)
print(student_passed)
print(student_attendance)

print(id(student_age))
print(id(student_gpa))
print(id(student_name))
print(id(student_passed))
print(id(student_attendance))

print(id(student_one_marks))
print(id(student_two_marks))

print(type(student_age))
print(type(student_gpa))
print(type(student_name))
print(type(student_passed))
print(type(student_attendance))
print(type(student_one_marks))

data_one = "Good"
data_two = " Morning"
# Concatenation : Is joining multiple strings together, using + operator
print(data_one + data_two)

num1 = 10
num2 = 20
# Addition : perform mathematical addition operation
print(num1 + num2)

# print(num1 + data_two) # TypeError: unsupported operand type(s) for +: 'int' and 'str'

name = "Ravi"
age = 28
cibl = 8.8
# print("My name is "+name + " my age is "+age) # TypeError: can only concatenate str (not "int") to str
# Interpolation : Is replacing placeholders with actual values
print(f"My name is {name} my age is {age} and my cibl score us {cibl}")

x = 10
y = 20
z = 30

print(x)
print(y)
print(z)

# x,y,z = 10,20,30,40 # ValueError: too many values to unpack (expected 3) --> LHS == RHS
x,y,z = 10,20,30
print(x,y,z)

x = 10
y = 10
z = 10

print(x,y,z)

x = y = z = 10
print(x,y,z)

# Arithmetic Operators
n1 = 3
n2 = 2
print(f"Sum of n1 and n2 is: {n1+n2}")
print(f"Difference of n1 and n2 is: {n1-n2}")
print(f"Product of n1 and n2 is: {n1*n2}")
print(f"Division of n1 and n2 is: {n1/n2}")
print(f"Modulus of n1 and n2 is: {n1%n2}")
print(f"Floor Division of n1 and n2 is: {n1//n2}")
print(f"exponentiation of n1 and n2 is: {n1**n2}")

# Without Compound Assignment Operators
x = 10
x = x + 5
print(x)

# With Compound Assignment Operators
x = 10
print(id(x))
x+= 5 # x = 10 + 5 = 15
print(id(x))
print(x)

f = 10
print(id(x))
x*= 5 # 15 * 5
print(f)

# Comparison Operators 
n1 = 3
n2 = 2
n3 = 3
print(n1 == n2)
print(n1 == n3)
print(n1 != n3)
print(n1 > n2)

# Logical Operators
x = 5
y = 7
a = 10
b = 8
resultAND = x < y and a > b # T and T -> T
print(resultAND)
resultAND = x < y and a < b # T and F -> F
print(resultAND)

resultOR =  x < y or a < b # T or F -> T
print(resultOR)
resultOR =  x > y or a < b # F or F -> F
print(resultOR)

resultNOT = x < y or a < b # T or F -> T
print(not resultNOT)

# List is a sequence data type
list_nums = [10,20,30,40,50] 
is_present = 10 in list_nums
print(is_present)
is_present = 100 in list_nums
print(is_present)

# string is also a sequence data type
msg = "hello"
is_present = "a" not in msg
print(is_present)
is_present = "e" in msg
print(is_present)

# Identity Operators
n1 = 10
n2 = 10
n3 = 10.0

print(n1 == n2) # compare values
print(n1 is n2) # compare addresses
print(n1 is n3) # compare addresses

# NOTE : Numbers are Immutable(Not Changeable) Data Types
# LIST : Lists are Mutable(Changeable) Data Types
l1 = [10,20,30] # [], 10, 20, 30 
l2 = [10,20,30]
print(l1 == l2) # compare values
print(l1 is l2) # compare addresses
print(l1 is not l2) # compare addresses
print(id(l1))
print(id(l2))
print(id(n1))
print(id(n2))
print(id(l1[0]))
print(id(l2[0]))

# Bitwise Operators
a = 5 # 0000000000000101
b = 3 # 0000000000000011 
#|    # 0000000000000111
#&    # 0000000000000001

# a = "a"

print(a & b)
print(a | b)

# Data Types
brand = "THE BEAR HOUSE"
desc =  "Men Maroon & Navy Blue Slim Fit Checked Flannel Casual Shirt"
rating = 4.3
price = 923

print(type(brand))
print(type(desc))
print(type(rating))
print(type(price))

com_num =  1 + 2j
print(type(com_num))

list_nums = [10,20,30] 
print(type(list_nums))

tuple_nums = (10,20,30)
print(type(tuple_nums))

set_nums = {10,20,30}
print(type(set_nums))

dict_data = {"name":"Ravi", "age":25}
print(type(dict_data))

x = None
print(type(x))

# Create your own data types - OOPS
class Student:
    pass # skip - do nothing 

lync_student = Student()
print(type(lync_student))
print(id(lync_student))