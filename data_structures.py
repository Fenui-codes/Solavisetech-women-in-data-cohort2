# SECTION 4: DATA STRUCTURES

print("----- Favorite Tools List -----")
tools = ["VS Code", "GitHub", "Jupyter"]

tools.append("Python")
tools.remove("Jupyter")

print(tools)

print("\n----- Student Scores -----")
scores = [78, 85, 90, 66, 88]

print(f"Highest: {max(scores)}")
print(f"Lowest: {min(scores)}")
print(f"Average: {sum(scores) / len(scores)}")

print("\n----- Shopping List Manager -----")
shopping_list = ["Rice", "Oil", "Milk"]

shopping_list.append("Bread")
shopping_list.remove("Oil")

print(shopping_list)

print("\n----- Country Capitals -----")
country_capitals = (
    ("Cameroon", "Yaounde"),
    ("Nigeria", "Abuja"),
    ("Ghana", "Accra")
)

for country, capital in country_capitals:
    print(f"{country}: {capital}")

print("\n----- Unique Visitors -----")
visitors = [1, 2, 2, 3, 4, 4, 5]
unique_visitors = set(visitors)

print(unique_visitors)

print("\n----- Common Skills -----")
set1 = {"Python", "SQL", "Excel"}
set2 = {"Python", "Java", "Excel"}

print(set1 & set2)

print("\n----- Student Record -----")
student = {
    "name": "Emelda",
    "age": 22,
    "course": "Data Science"
}

print(student)

print("\n----- Mini Contact Book -----")
contacts = {
    "Alice": "123456789",
    "Bob": "987654321"
}

search = input("Search contact name: ")

if search in contacts:
    print(f"{search}: {contacts[search]}")
else:
    print("Contact not found")