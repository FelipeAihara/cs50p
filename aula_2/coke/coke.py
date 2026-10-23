def main():
    amount_due = 50

    while True:
        while True:
            print(f"Amount due: {amount_due}")
            discount = int(input("Insert Coin: "))
            
            if (discount == 25 or discount == 10 or discount == 5):
                break

        amount_due -= discount

        if amount_due <= 0:
            print(f"Change owed: {-amount_due}")
            break  

if __name__ == "__main__":
    main()