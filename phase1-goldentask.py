import string
import secrets
def generate_password(length,use_uppercase,use_lowercase,use_digits,use_special_chars):
    characters= ''

    if use_uppercase:
        characters +=string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    if not any([use_uppercase,use_lowercase,use_digits,use_special_chars]):
        return "Please select at least one character type"
    password=''.join(secrets.choice(characters)for _ in range(length))
    return password
print("Welcome to the Random Password Generator!")
while True:
    try:
        length=int(input("Enter password length:"))
        use_uppercase=input("include uppercase letter?(y/n):").lower()=='y'
        use_lowercase=input("include lowercase letters?(y/n):").lower()=='y'
        use_digits=input("include digits?(y/n):").lower()=='y'
        use_special_chars=input("include special characters?(y/n):").lower()=='y'
        password=generate_password(length,use_uppercase,use_lowercase,use_digits,use_special_chars)
        print("Generated_password:",password)
        break
    except ValueError:
        print("Please enter a valid password length(a positive integer)")

