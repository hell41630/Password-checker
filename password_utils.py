def check_password_strength(password):
    # Define criteria
    min_length = 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in password)
    
    is_strong = (
        len(password) >= min_length and has_upper and has_lower and has_digit and has_special
    )
    
    feedback = []
    if len(password) < min_length:
        feedback.append("Add at least 8 characters.")
    if not has_upper:
        feedback.append("Include at least one uppercase letter.")
    if not has_lower:
        feedback.append("Include at least one lowercase letter.")
    if not has_digit:
        feedback.append("Include at least one number.")
    if not has_special:
        feedback.append("Include at least one special character (e.g., !, @, #, etc.).")
    
    # Join feedback suggestions with a line break
    feedback_message = " ".join(feedback) if feedback else "Your password is strong!"
    
    return is_strong, feedback_message
