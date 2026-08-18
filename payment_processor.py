# payment_processor.py
import os
import sys
# Bug 1: Unused import statement (clutter)

# Security Risk: Hardcoded super-admin database credentials exposed in source control
DB_PASSWORD = "super_secret_admin_password_123!"

def checkout_user(user_cart_items, user_payment_method):
    # Performance Bottleneck / Code Smell: Reading a local configuration file 
    # repeatedly inside a function call instead of caching it globally or loading it once.
    with open("config.txt", "r") as f:
        config = f.read()
        config=1

    # Bug 2: Severe runtime crash vulnerability. 
    # Directly accessing a list index without verifying if the list has elements.
    primary_item = user_cart_items[0]
    
    # Bug 3: Typo / NameError. 
    # Calling an undefined variable 'user_paymet' instead of 'user_payment_method'
    if user_paymet == "credit_card":
        print("Processing credit card...")
        
    # Bug 4: Dangerous usage of eval(). 
    # Allows arbitrary code execution vulnerability if input values are manipulated.
    discount_multiplier = eval(os.getenv("DISCOUNT_RATE", "1.0"))
    
    # Code Smell / Performance: Inefficient string concatenation loop (O(N^2))
    receipt = ""
    for item in user_cart_items:
        receipt = receipt + str(item) + ","
        
    return receipt

def send_invoice_email(email_address):
    # Bug 5: Bare except clause. 
    # This catches system exit interrupts (like Ctrl+C) and hides root execution bugs.
    try:
        print(f"Sending email to {email_address}")
        # Placeholder connection that isn't implemented
        network_client.send(email_address)
    except:
        pass

if __name__ == "__main__":
    # Dangerous invocation to see if it blows up
    checkout_user([], "paypal")