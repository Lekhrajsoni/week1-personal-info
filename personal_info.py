# Project: Personal Information Manager 

# Welcome message
print("=" * 40)
print("   PERSONAL INFORMATION MANAGER   ")
print("=" * 40)
print()

# Store static information (fixed info)
name = "Lekh Raj Soni"
age = 19           
city = "Jamshedpur"
hobby = "Travelling"

# Get user input
print("Describe Yourself")
print("-" * 30)

fav_food = input("What's your favorite food? ").strip()
while fav_food == "":
    print("Please enter a valid food!")
    fav_food = input("What's your favorite food? ").strip()

fav_color = input("What's your favorite color? ").strip()
while fav_color == "":
    print("Please enter a valid color!")
    fav_color = input("What's your favorite color? ").strip()

# Calculate age in months
age_in_months = age * 12

# Display all information
print()
print("=" * 40)
print("    YOUR INFORMATION    ")
print("=" * 40)
print()

print(f"Name: {name}")
print(f"Age: {age} years ({age_in_months} months old)")
print(f"City: {city}")
print(f"Hobby: {hobby}")
print()
print(f"Favorite Food: {fav_food}")
print(f"Favorite Color: {fav_color}")
print()

# Goodbye message
print("=" * 40)
print("Thanks for using this program!")
print("=" * 40)