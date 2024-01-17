import re

# Utility Methods:
# -------------------

def calculate_product_purchase_total(entries, currency_symbol):
    currency_total = 0.0
    transaction_count = 0
    current_transaction_type = None

    for entry in entries:
        lines = entry.split('\n')

        for line in lines:
            if re.match(r'\d{2}/\d{2}/\d{4}', line):
                # Check if the line starts with a date - this marks a new transaction
                continue
            elif line.strip().lower() == 'product purchase':
                current_transaction_type = 'product_purchase'
                # Ensures only 'product purchase' transactions are counted
                # 'wallet funding' transactions are not counted, as this would result in the doubling of certain purchase totals
            elif line.startswith(currency_symbol):
                if current_transaction_type == 'product_purchase':
                    # For currencies that use commas to separate thousands, remove the commas
                    number_without_comma = line[1:].replace(",", "")
                    currency_total += float(number_without_comma)
                    transaction_count += 1
                    current_transaction_type = None

    return currency_total, transaction_count

def get_currency():
    currency_symbol = input("Enter the current associated with your PSN purchases (e.g., £, $, €): ")
    return currency_symbol

# Main Method:
# -------------------

user_prompt = """
This program will provide you with your total amount spent, as well as your total number of purchases on PSN over a defined period.
Please complete the following steps:

1: Go to https://www.playstation.com
2: Sign in with your PSN details (if not signed in already) and click your profile picture (top right of the web page)
3: Click 'Account Settings'
4: On the new screen, click 'Transaction History' on the left-hand pane
5: Press 'Continue' when the prompt to open another page appears
6: In the 'Transaction History' pane that's now open, select the period for which you want to total your account spending (e.g., 01/01/2009 - 01/01/2024)
7: Now, copy all of the results that appear, starting from the date of the first item.

   For example, for a history of 3 purchases, this copied text might look like:
   01/12/2024
   Product Purchase
   £10.00
   01/12/2024
   Wallet Funding
   £15.00
   01/12/2024
   Product Purchase
   £0.00

8: Paste this copied text into this program ONCE - do not worry if your pasted text does not appear on screen.

9: Press enter TWICE
"""

# Text pasted from the Playstation website results in multiple user-inputs into terminal.
# Therefore one normal terminal input prompt won't work.
# This is why the below user-input code is a bit unconventional.
entries = []
while True:
    entry = input(user_prompt)
    if not entry:
        break

    entries.append(entry)

currency_symbol = get_currency()
currency_total, transaction_count = calculate_product_purchase_total(entries, currency_symbol)

print(f"Total for product purchases: {currency_symbol}{currency_total:.2f}")
print(f"Total number of purchases: {transaction_count}")
