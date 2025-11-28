import re

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None

    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])

    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Medium"
    else:
        strength = "Weak"

    feedback = {
        "length": "Password length is sufficient" if length_criteria else "Password is too short",
        "uppercase": "Contains uppercase letters" if uppercase_criteria else "Missing uppercase letters",
        "lowercase": "Contains lowercase letters" if lowercase_criteria else "Missing lowercase letters",
        "digit": "Contains digits" if digit_criteria else "Missing digits",
        "special_char": "Contains special characters" if special_char_criteria else "Missing special characters",
        "strength": strength
    }

    return feedback

def main():
    password = input("Enter your password: ")
    feedback = assess_password_strength(password)

    print("\nPassword Strength Feedback:")
    print(f"Length: {feedback['length']}")
    print(f"Uppercase: {feedback['uppercase']}")
    print(f"Lowercase: {feedback['lowercase']}")
    print(f"Digit: {feedback['digit']}")
    print(f"Special Character: {feedback['special_char']}")
    print(f"Overall Strength: {feedback['strength']}")

if __name__ == "__main__":
    main()