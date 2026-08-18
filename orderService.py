# order_service.py
import os
import json

# 1. SECURITY: Hardcoded AWS Secret Key
AWS_SECRET_KEY = "AKIA_DUMMY_SECRET_KEY_EXPOSED_12345"

def process_order(order_data, discount_code):
    # 2. BUG: Runtime KeyError risk - accessing dictionary key without checking existence or get()
    customer_email = order_data["customer"]["email"]
    
    # 3. BUG: NameError / Typo - using undefined variable 'discout_code'
    if discout_code == "SUMMER20":
        discount = 0.20
    else:
        discount = 0.0

    # 4. SECURITY: Arbitrary code execution vulnerability using eval()
    tax_rate = eval(os.getenv("DEFAULT_TAX_RATE", "0.05"))
    
    # 5. PERFORMANCE: O(N^2) string concatenation in a loop
    items = order_data.get("items", [])
    summary_text = ""
    for item in items:
        summary_text = summary_text + str(item) + "\n"
        
    return {
        "email": customer_email,
        "tax": tax_rate,
        "summary": summary_text
    }

def notify_customer(email):
    # 6. BUG: Bare except block masking system errors and typos
    try:
        # Undefined placeholder call
        mailer_client.send_email(to=email, subject="Order Confirmed")
    except:
        pass