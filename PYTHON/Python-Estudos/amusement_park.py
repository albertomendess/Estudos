# SINTAXE if-elif-else
age = 19

if age < 4:
    price = 0
elif age < 18 or age > 64:
    price = 5
elif age < 65:
    price = 10

print("Your admission cost in $" + str(price) + "!")