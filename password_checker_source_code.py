import re

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    strength_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])
    
    feedback = []

    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not digit_criteria:
        feedback.append("Password should include at least one digit.")
    if not special_char_criteria:
        feedback.append("Password should include at least one special character.")

    strength_description = {
        5: "Very Strong",
        4: "Strong",
        3: "Moderate",
        2: "Weak",
        1: "Very Weak",
        0: "Very Weak"
    }

    return strength_description[strength_score], feedback

def main():
    password = input("Enter your password: ").strip()
    strength, feedback = assess_password_strength(password)
    
    print(f"Password Strength: {strength}")
    if feedback:
        print("Feedback:")
        for f in feedback:
            print(f"- {f}")

if __name__ == "__main__":
    main()
