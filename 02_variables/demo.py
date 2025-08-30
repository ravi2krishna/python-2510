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