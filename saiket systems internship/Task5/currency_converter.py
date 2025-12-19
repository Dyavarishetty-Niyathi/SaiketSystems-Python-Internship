import requests


def convert_currency(amount, from_currency, to_currency):
    url = "https://api.frankfurter.app/latest"  #Used a free working currency conversion API

    params = {
        "amount": amount,
        "from": from_currency,
        "to": to_currency
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()

        if "rates" not in data or to_currency not in data["rates"]:
            print(" Invalid currency code. Please try again.")
            return

        converted_amount = data["rates"][to_currency]

        print(f"\n💱 {amount} {from_currency} = {converted_amount:.2f} {to_currency}")

    except requests.exceptions.RequestException:
        print(" Network error. Please check your internet connection.")

    except ValueError:
        print(" Invalid input.")


def main():
    print("Common currency codes: USD, INR, EUR, GBP, JPY\n")

    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print(" Amount must be greater than zero.")
            return

        from_currency = input("From currency: ").strip().upper()
        to_currency = input("To currency: ").strip().upper()

        convert_currency(amount, from_currency, to_currency)

    except ValueError:
        print(" Please enter a valid number.")


if __name__ == "__main__":
    main()
