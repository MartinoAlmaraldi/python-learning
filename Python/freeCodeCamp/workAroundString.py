my_str_1 = 'Hello'
my_str_2 = "World"

str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str) # Hello World

name = 'John Doe'
age = 26

name_and_age = name + age
print(name_and_age) # TypeError: can only concatenate str (not "int") to str
# To fix the error, we need to convert 'age' to a string using the str() function
name_and_age_fixed = name + ' ' + str(age)

# += eperator example
name_and_age = name  # Start with the name
name_and_age += str(age)  # Append the age as string

print(name_and_age)  # John Doe26

name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age) # My name is John Doe and I am 26 years old

num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}') # The sum of 5 and 10 is 15

my_str = 'Hello world'
print(len(my_str))  # 11, check the length of the string

print(my_str[0])  # H
print(my_str[6])  # w

print(my_str[-1])  # d
print(my_str[-2]) # l, from backwards

# string[start:stop]
print(my_str[1:4]) # ello, from index 1 to 3
print(my_str[0:5]) # Hello, from index 0 to 4

print(my_str[:7])  # Hello w, up to index 6
print(my_str[8:])  # rld, starting from index 8 to the end

print(my_str[:])  # Hello world, whole string

# string[start:stop:step]
my_str = 'Hello world'
print(my_str[0:11:2])  # Hlowrd, every second character from index 0 to 10 because it stops before 11
print(my_str[::3])  # Hl r, every third character in the whole string, can be from reverse too with negative step like -1/-2

#Check if substring exists in string, using 'in' operator
print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False