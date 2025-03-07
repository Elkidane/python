#Menu 

menu={"pizza": 3.00,
       "burger": 4.00,
       "popcorn": 2.00,
       "chips": 1.75,
       "soda": 1.50,
       "coffe": 2.00,}

cart=[]
total=0

print("--------MENU----------")

for key, value in menu.items():
    print(f"{key:10}: ${value: .2f}")
print("----------------")
print()

while True:
    food=input("select an item (q to quit): ").lower()
    if food =="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total: .2f}")