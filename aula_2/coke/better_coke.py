def main():
    amount_due = 50

    while amount_due > 0:
        print(f"Amount due: {amount_due}")
        coin = int(input("Insert Coin: "))

        if is_valid_coin(coin):
            amount_due -= coin

    print(f"Change owed: {-amount_due}")


# Checks if the inserted coin is one of the accepted values
def is_valid_coin(coin):
    return coin in (25, 10, 5)


if __name__ == "__main__":
    main()
