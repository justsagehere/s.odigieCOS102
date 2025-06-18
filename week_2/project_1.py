#Pseudocode

START
Display "Welcome to Store"
Initialize total = 0
WHILE more items to scan:
    Input item price
    Add item price to total
Display total
Input payment amount
IF payment >= total:
    Calculate change = payment - total
    Display change
ELSE:
    Display "Insufficient payment"
END


#flowchart

Start → Wake Up → Brush Teeth → Shower → Dress → Eat → Go to Class → End


#swap ages

name1 = input("Enter first name: ")
age1 = input(f"Enter age of {name1}: ")

name2 = input("Enter second name: ")
age2 = input(f"Enter age of {name2}: ")

# Swap
age1, age2 = age2, age1

print(f"{name1}'s new age is: {age1}")
print(f"{name2}'s new age is: {age2}")
