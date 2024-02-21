import random
import string

def generate_password(length = 12, complexity = "medium"):
    if complexity == "low":
        charset = string.ascii_letters + string.digits
    elif complexity == "medium":
        charset = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "high":
        charset = charset = string.ascii_letters + string.digits + string.punctuation + "£$€¥"
    else: 
        raise ValueError("Complexity level has to be 'low', 'medium', or 'high'")

    password = ''.join(random.choice(charset) for _ in range(length))
    return generate_password

if __name__ == "__main__":
    length = int(input("Enter the desired length of the password: "))
    complexity = input("Enter the complexity level ('low', 'medium', or 'high'): ").lower()

    try:
        password = generate_password(length, complexity)
        print("Generated password:", password)
    except ValueError as e:
        print("Error:", e)