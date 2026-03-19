foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy(q to quite): ")
    if food.lower() == "q":                  # food.lower() = use for q to Q to quit it
        break
    else:
        price = float(input(f"Enter the price of a {food}: $ "))
        foods.append(food)
        prices.append(price)

print("____YOUR CART_____")

for food in foods:
    print(food, end=" ")

for price in prices:
   total += price

print()
print(f"Your Total is: ${total}")