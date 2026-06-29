# app.py
import os

def calculate_total(prices):
    # Bug 1: Shadowing built-in variable name 'sum'
    sum = 0
    for price in prices:
        sum += price
    return sum

def process_user_data(user_id):
    # Bug 2: Security Risk - Hardcoded sensitive token pattern
    API_TOKEN = "secret_xyz123_token_unsecure"
    
    # Bug 3: Using an undefined or unimported library variable/placeholder
    # (This will cause a runtime NameError)
    data = fetch_from_database(user_id, token=API_TOKEN)
    # Adding some more lines
    # end of adding some more lines
    
    print("User processing completed.")
    return data

if __name__ == "__main__":
    items = [10, 25, 4.99]
    print(f"Total: {calculate_total(items)}")
    # The Push SHoud not work here 