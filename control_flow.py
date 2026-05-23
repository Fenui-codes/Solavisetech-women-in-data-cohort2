# SECTION 3: CONTROL FLOW

print("----- Age Eligibility Checker -----")
age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")

print("\n----- Password Validator -----")
password = input("Enter password: ")

if len(password) >= 8:
    print("Strong password")
else:
    print("Weak password")

print("\n----- Grade Classification -----")
score = float(input("Enter score: "))

if score >= 80:
    print("Grade A")
elif score >= 70:
    print("Grade B")
elif score >= 60:
    print("Grade C")
elif score >= 50:
    print("Grade D")
else:
    print("Fail")

print("\n----- Multiplication Table -----")
num = int(input("Enter a number: "))

for i in range(1, 13):
    print(f"{num} x {i} = {num * i}")

print("\n----- Number Guessing Game -----")
secret = 7
guess = 0

while guess != secret:
    guess = int(input("Guess the number (1-10): "))
    if guess != secret:
        print("Wrong, try again!")

print("Correct! You guessed it.")

print("\n----- Countdown Timer -----")

count = 10
while count > 0:
    print(count)
    count -= 1

print("Go!")

print("\n----- ATM Withdrawal Simulation -----")
balance = 1000
withdraw = float(input("Enter amount to withdraw: "))

if withdraw <= balance:
    balance -= withdraw
    print(f"Withdrawal successful. Remaining balance: {balance}")
else:
    print("Insufficient funds")

print("\n----- Login System -----")
username = "admin"
password = "1234"

user = input("Enter username: ")
pwd = input("Enter password: ")

if user == username and pwd == password:
    print("Login successful")
else:
    print("Invalid credentials")