fruits = {
    "apple": "130",
    "avocado": "50",
    "sweet cherries": "100"
}

fruit = input("Item: ")
fruit = fruit.lower()
if fruit in fruits:
    print(f"Calories {fruits[fruit]}")