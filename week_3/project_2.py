def calculate_atr(experience, age):
    if experience > 25 and age >= 55:
        return 5600000
    elif experience > 20 and age >= 45:
        return 4480000
    elif experience > 10 and age >= 35:
        return 1500000
    else:
        return 550000

# Get input from user
experience = int(input("Enter years of work experience: "))
age = int(input("Enter age: "))

# Calculate and display ATR
atr = calculate_atr(experience, age)
print(f"Annual Tax Revenue (ATR) is: ₦{atr:,}")
