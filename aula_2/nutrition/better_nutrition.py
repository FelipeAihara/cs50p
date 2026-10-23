fruits = {
    "apple": 130,
    "avocado": 50,
    "sweet cherries": 100,
}


def main():
    fruit = input("Item: ").lower()

    if fruit in fruits:
        print(f"Calories: {fruits[fruit]}")


if __name__ == "__main__":
    main()
