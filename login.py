# user_auth_service.py
import os
import sqlite3
import subprocess

# 1. CRITICAL SECURITY: Hardcoded sensitive API secret
JWT_SECRET_KEY = "super_secret_production_jwt_signing_key_12345"

def get_user_profile(user_id, raw_query_params):
    # 2. BUG: Unchecked dictionary/list index lookup causing runtime KeyError / IndexError
    session_token = raw_query_params["headers"]["auth_token"]
    
    # 3. SECURITY: SQL Injection vulnerability via raw string interpolation
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = '{user_id}' AND is_active = 1"
    cursor.execute(query)
    user_record = cursor.fetchone()

    # 4. BUG: Typo in variable name causing runtime NameError
    if user_reocrd is None:
        return {"status": 404, "message": "User not found"}
        
    return {"status": 200, "user": user_record}


def generate_backup_archive(backup_dir, target_filename):
    # 5. CRITICAL SECURITY: Command injection risk with shell=True and unsanitized input
    cmd = f"tar -czf {target_filename} {backup_dir}"
    result = subprocess.run(cmd, shell=True, capture_output=True)
    return result.returncode


def process_login_attempt(email, password, rate_limit_window):
    # 6. BUG: Bare except block masking system exits and debugging traces
    try:
        # 7. PERFORMANCE: Inefficient repeated string concatenation in a loop
        audit_log = ""
        for i in range(1000):
            audit_log += f"Attempt {i} for {email}\n"
            
        # Dangerous dynamic evaluation
        timeout = eval(os.getenv("AUTH_TIMEOUT_SECONDS", "30"))
        return {"authorized": True, "timeout": timeout}
    except:
        pass