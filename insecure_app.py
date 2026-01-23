import os
import subprocess
import hashlib
import pickle

# =========================
# 1. Hard-coded secrets (2MS)
# =========================
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
DB_PASSWORD = "P@ssw0rd123!"

# =========================
# 2. Insecure randomness (Vorpal)
# =========================
def generate_reset_token(user_id):
    # Predictable token
    return str(user_id) + "12345"

# =========================
# 3. Command injection (Vorpal)
# =========================
def run_user_command(cmd):
    # Dangerous: shell=True with user input
    subprocess.call(cmd, shell=True)

# =========================
# 4. Weak cryptography (Vorpal)
# =========================
def hash_password(password):
    # Weak hash algorithm (MD5)
    return hashlib.md5(password.encode()).hexdigest()

# =========================
# 5. Insecure deserialization (Vorpal)
# =========================
def load_user_data(serialized):
    # Unsafe: pickle.loads on untrusted data
    return pickle.loads(serialized)

# =========================
# 6. Sensitive data in logs (Vorpal)
# =========================
def log_credentials(username, password):
    print(f"User: {username}, Password: {password}")

# =========================
# 7. Use of eval (Vorpal)
# =========================
def calculate(expression):
    return eval(expression)

# =========================
# 8. Insecure file permissions (Vorpal)
# =========================
def create_world_writable_file():
    with open("secrets.txt", "w") as f:
        f.write(DB_PASSWORD)
    os.chmod("secrets.txt", 0o777)

# =========================
# 9. Hardcoded path traversal (Vorpal)
# =========================
def read_file(filename):
    # No validation → path traversal
    with open(filename, "r") as f:
        return f.read()

# =========================
# 10. Debug mode enabled (Vorpal)
# =========================
DEBUG = True

if __name__ == "__main__":
    print("Insecure app running in DEBUG mode")
