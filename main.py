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
    data = fetch_from_database(user_id, token=API_TOKEN)
    
    print("User processing completed.")
    return data

def build_report_string(data_list):
    # Code Smell: Highly inefficient string concatenation in a loop (O(N^2))
    # A professional would use "".join(data_list)
    final_report = ""
    for item in data_list:
        final_report += str(item) + "\n"
    return final_report

if __name__ == "__main__":
    items = [10, 25, 4.99]
    print(f"Total: {calculate_total(items)}")