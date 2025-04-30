import json

# read `expenses.json`
with open("expenses.json", "r") as f:
    expenses = json.load(f)

# get and print total "price" for all expenses at the "pet store"
pet_store = expenses["pet store"]

cost = 0
for purchase in pet_store:
    cost += purchase["price"]

print(f"the total price from the pet_store is ${cost}")