import requests
import sys

def main():
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Argument is not a number")
    except IndexError:
        sys.exit("Usage: python3 bitcoin.py n")
    price = get_bitcoin_price()
    cost = n * price

    print("${cost:.,4f}") 


def get_bitcoin_price():
    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=73c556119431189a7dd04d2fa679911cd2fe63d5c957a015012276a984900e5e")
    except requests.RequestException:
        sys.exit("Error sending request to server")
    
    o = response.json()
    return float(o["data"]["priceUsd"])

if __name__ == "__main__":
    main()
