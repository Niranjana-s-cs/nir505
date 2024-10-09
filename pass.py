import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Criteria 1: Length
    if len(password) < 8:
        feedback.append("Password should be at least 8 characters long.")
    elif len(password) <= 12:
        strength += 1
    else:
        strength += 2

    # Criteria 2: Uppercase Letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
    
    # Criteria 3: Lowercase Letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")
    
    # Criteria 4: Numbers
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")
    
    # Criteria 5: Special Characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")
    
    # Criteria 6: Uniqueness
    common_passwords = ['password', '123456', 'qwerty', 'letmein', 'admin']
    if password in common_passwords:
        feedback.append("Password is too common. Choose a more unique one.")
    else:
        strength += 1
    
    # Final Feedback
    if strength < 3:
        feedback.append("Password strength: Weak.")
    elif strength < 5:
        feedback.append("Password strength: Moderate.")
    else:
        feedback.append("Password strength: Strong.")

    return '\n'.join(feedback)

# Test the function
user_password = input("Enter a password to check: ")
print(check_password_strength(user_password))
