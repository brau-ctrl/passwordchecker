#
#DecodeLabs – Project 1: Password Strength Checker

import re
import math
import hmac
from typing import Tuple, List

# ------------------------------------------------------------------
#Common leaked passwords

COMMON_PASSWORDS = {
    "password", "123456", "123456789", "qwerty", "abc123",
    "password123", "admin", "iloveyou", "welcome", "admin123",
    "letmein", "dragon", "baseball", "master", "sunshine"
}

#Entropy calculation (bits)

def calculate_entropy(password: str) -> float:
    """Returns approximate entropy in bits (log2 of possible combinations)."""
    charset_size = 0
    if re.search(r'[a-z]', password):
        charset_size += 26
    if re.search(r'[A-Z]', password):
        charset_size += 26
    if re.search(r'[0-9]', password):
        charset_size += 10
    if re.search(r'[^a-zA-Z0-9]', password):
        charset_size += 33   # typical special chars count
    
    if charset_size == 0:
        return 0.0
    return len(password) * math.log2(charset_size)


#Strength evaluation
# ------------------------------------------------------------------
def check_password_strength(password: str) -> Tuple[str, List[str]]:
    """
    Returns (strength_label, list_of_suggestions)
    strength: 'Very Weak', 'Weak', 'Moderate', 'Strong', 'Very Strong'
    """
    suggestions = []
    score = 0

    # --- Length checks (critical) ---
    length = len(password)
    if length < 8:
        suggestions.append("Password is too short – use at least 8 characters.")
        score += 0
    elif length < 12:
        score += 1
    elif length < 16:
        score += 2
    else:
        score += 3

    # --- Character diversity ---
    if re.search(r'[a-z]', password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        suggestions.append("Add digits (0-9).")

    if re.search(r'[^a-zA-Z0-9]', password):
        score += 1
    else:
        suggestions.append("Add special characters (e.g., !@#$%).")

    # --- Blacklist check (case‑insensitive) ---
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        suggestions = ["Password is too common / leaked – choose a unique one."]
        return ("Very Weak", suggestions)

    # --- Entropy bonus ---
    entropy = calculate_entropy(password)
    if entropy > 60:
        score += 2
    elif entropy > 40:
        score += 1

    # --- Final classification ---
    if score <= 2:
        strength = "Very Weak"
    elif score <= 4:
        strength = "Weak"
    elif score <= 6:
        strength = "Moderate"
    elif score <= 8:
        strength = "Strong"
    else:
        strength = "Very Strong"

    # Remove redundant suggestions if password already good
    if strength in ["Strong", "Very Strong"]:
        suggestions = ["Excellent password! Keep using unique passphrases."]

    return (strength, suggestions)

# ------------------------------------------------------------------
# 4. Secure constant‑time verification (if you later store a hash)
#    Not directly used for strength checking, but good defensive practice.
# ------------------------------------------------------------------
def constant_time_compare(a: str, b: str) -> bool:
    """Prevent timing attacks when comparing secrets."""
    return hmac.compare_digest(a.encode(), b.encode())

# ------------------------------------------------------------------
# 5. Main interactive loop
# ------------------------------------------------------------------
def main():
    print("\n" + "=" * 60)
    print("🔒 DecodeLabs – Password Strength Checker (Project 1)")
    print("=" * 60)
    print("Enter a password to analyse its security level.\n")
    
    while True:
        pwd = input("Password (or 'quit' to exit): ").strip()
        if pwd.lower() == 'quit':
            print("Stay secure. Goodbye!")
            break
        if not pwd:
            print("❌ Password cannot be empty.\n")
            continue
        
        strength, tips = check_password_strength(pwd)
        entropy = calculate_entropy(pwd)
        
        print("\n📊 Analysis Result:")
        print(f"   → Strength      : {strength}")
        print(f"   → Entropy (bits): {entropy:.1f}")
        print("   → Suggestions   :")
        for tip in tips:
            print(f"       - {tip}")
        print("-" * 50 + "\n")

if __name__ == "__main__":
    main()