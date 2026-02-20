name = 'john doe'
age = 25 
#Python automatically knows that 'name' is a string and 'age' is an integer based on the assigned values.

my_integer_var = 10
print ('Integer:', my_integer_var)

my_float_var = 4.50
print('Float:', my_float_var)

my_complex_var = 3 + 5j #Complex Number: A number with a real and imaginary part
print('Complex Number:', my_complex_var)

my_string_var = 'Hello'
print('String:', my_string_var)

my_boolean_var = True
print('Booelan:', my_boolean_var)

my_set_var = {7, 5, 8} #Set: An unordered collection of unique elements
print('Set:', my_set_var)

my_dictionary_var = {'name': 'Alice', 'age': 30} #Dictionary: A collection of key-value pairs
print('Dictionary:', my_dictionary_var)

my_tuple_var = (1, 2, 3) #Tuple: An ordered, immutable collection of elements
print('Tuple:', my_tuple_var)

my_range_var = range(5) #Range: A sequence of numbers
print(my_range_var)

my_list = [22, 'hello world', 3.14, True]
print('List:', my_list)

my_none_var = None #NoneType: Represents the absence of a value
print('None:', my_none_var)


nums = [0, 1, 2]
nums[0] = 4
print(nums) # Output: [4, 1, 2]

#To get the data type of a variable, you can use the type() function:
my_var_1 = 'world'
my_var_2 = 42
print(type(my_var_1))  # Output: <class 'str'>
print(type(my_var_2))  # Output: <class 'int'>

def greet(name: str, age: int) -> str:
    return f'Hello, {name}, age {age}.'

user_name: str = 'John Doe'
user_age: int = 24

print(greet(user_name, user_age)) # Hello, John Doe, age 24.
