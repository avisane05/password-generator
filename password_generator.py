import string, random

def generate_password(min_length, number=True, special_charactors=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    charactors = letters
    if number:
        charactors += digits
    if special_charactors:
        charactors += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(charactors)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if number:
            meets_criteria = has_number
        if special_charactors:
            meets_criteria = meets_criteria and has_special

    return pwd

min_length = int(input("Enter the minimum lenght: "))
has_number = input("Do you want to include numbers (y/n): ").lower() == "y"
has_special = input("Do you want to include special charactors (y/n): ").lower() == "y"

pwd = generate_password(min_length, has_number, has_special)
print("The generated password is:", pwd)



