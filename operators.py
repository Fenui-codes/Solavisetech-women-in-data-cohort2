# SECTION 2: BASIC OPERATIONS & MATHEMATICAL OPERATORS

print("----- Simple Calculator -----")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
print(f"Division: {num1 / num2}")

print("\n----- Area of Shapes -----")

# Circle
radius = float(input("Enter radius of circle: "))
circle_area = 3.1416 * radius * radius
print(f"Area of circle: {circle_area}")

# Rectangle
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
rectangle_area = length * width
print(f"Area of rectangle: {rectangle_area}")

# Triangle
base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))
triangle_area = 0.5 * base * height
print(f"Area of triangle: {triangle_area}")

print("\n----- Even or Odd -----")
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

print("\n----- Student Grade Percentage -----")
score = float(input("Enter total score: "))
total = float(input("Enter total possible score: "))

percentage = (score / total) * 100
print(f"Percentage: {percentage}%")

print("\n----- BMI Calculator -----")
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)
print(f"BMI: {bmi}")

print("\n----- Power & Modulus -----")
base = int(input("Enter base number: "))
exponent = int(input("Enter exponent: "))

print(f"Power result: {base ** exponent}")

mod_num1 = int(input("Enter first number: "))
mod_num2 = int(input("Enter second number: "))

print(f"Modulus result: {mod_num1 % mod_num2}")