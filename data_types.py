# SECTION 1: DATA TYPES EXERCISES

# Personal Bio Generator
name = "Mbogwe Emelda Fenui"
age = 23
height = 1.65
favorite_tech_field = "Data Science"
is_student = True

print("----- Personal Bio Generator -----")
print(f"My name is {name}. I am {age} years old.")
print(f"My height is {height} meters.")
print(f"My favorite tech field is {favorite_tech_field}.")
print(f"Student Status: {is_student}")

# Type Checker
print("\n----- Type Checker -----")
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

# Data Conversion
print("\n----- Data Conversion -----")
integer_num = 100
integer_to_string = str(integer_num)
print(integer_to_string)

float_num = 15.8
float_to_integer = int(float_num)
print(float_to_integer)

string_number = "500"
string_to_integer = int(string_number)
print(string_to_integer)

# User Information
print("\n----- User Information -----")
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
user_country = input("Enter your country: ")

print(f"Hello {user_name}, you are {user_age} years old and you are from {user_country}.")

# Temperature Converter
print("\n----- Temperature Converter -----")
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C is equal to {fahrenheit}°F")