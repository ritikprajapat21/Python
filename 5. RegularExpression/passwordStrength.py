import re, pyperclip as pc

# To check the strength of the password
def checkStrength(password):
    # To check password contains small letters
    smallLetter = re.compile('[a-z]+')

    # To check password contains capital letters
    capitalLetter = re.compile('[A-Z]+')

    # To check password contains digits
    digit = re.compile('[0-9]+')

    # To check password contain special letters
    special = re.compile('\W+')

    # A flag to check password passes all the test
    isStrong = True

    if len(password) < 8:
        isStrong = False
        print("Length of password must be 8 or more characters")

    if not smallLetter.search(password):
        isStrong = False
        print("Include small letters")

    if not capitalLetter.search(password):
        isStrong = False
        print("Include capital letters")

    if not digit.search(password):
        isStrong = False
        print("Include digits")

    if not special.search(password):
        isStrong = False
        print("Include special letters")

    if isStrong:
        print("Password is strong")

# Taking password from the user
print("Copy password from clipboard: [Y] Yes [N] No")
ans = input().lower()
if ans == 'y':
    print("Password copied")
    password = pc.paste()
else:
    print("Enter your password:")
    password = input()

checkStrength(password)
