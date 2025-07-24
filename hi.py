import re 
uppercase = "[A-Z]"
lowercase = "[a-z]"
digits = "[0-9]"
special_chars = "[!@#$%^&*]"
patterns =  "[a-zA-Z0-9!@#$%^&*]"

def pass_check(password):
    errors = []
    if len(password) < 8 or len(password) > 25:
        errors.append("Password should be between 8 to 25 characters")
    if not re.search(uppercase, password):
        errors.append("Include one uppercase letter")
    if not re.search(lowercase, password):
        errors.append("Include atleast one lowercase letter")
    if not re.search(digits, password):
        errors.append("Inlcude atleast one digit")
    if not re.search(special_chars, password):
        errors.append("Include atleast one special character")
    if errors:
        for error in errors:
            print(error)
    else:
        print("Valid password")
    if len(errors) >= 2:
        print("Password strength = Weak")
    elif len(errors) == 1:
        print("Password strength = Medium")
    else:
        print("Password strength = Strong")

passw =input("enter password: ")

pass_check(passw)

