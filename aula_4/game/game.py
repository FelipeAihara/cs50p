import random

def main():
    while True:
        try:
            n = int(input("Level: "))

        except ValueError:
            continue

        if n > 0:
            break

    key = random.randint(1, n)

    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            continue

        if guess <= 0:
            continue

        if guess == key:
            print("Just right!")
            break
        elif guess < key:
            print("Too small!")
        else:
            print("Too large!")


if __name__ == "__main__":
    main()
