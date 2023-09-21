import re, pyperclip as pc

# Phone Number RegEx 
phnre = re.compile('''
(\d{3})  # For beginning 3 number
(-)?     # For separator
(\d{3})  # For middle 3 number
(-)?     # For separator
(\d{4})  # For last 4 number
''', re.VERBOSE)

# Email RegEx 
emailre = re.compile('''
[a-zA-Z0-9._%+-]+  # username
@                  # @ symbol
[a-zA-Z._-]+       # domain name
\.[a-zA-Z]{2,4}    # dot something
''', re.VERBOSE)

# Taking input from user 
print("Copy text from clipboard: [Y] Yes [N] No")
ans = input().lower()
if ans == 'y':
    text = pc.paste()
else:
    print("Enter text:")
    text = input()

# Finding matches 
matches = []

# Phone number matches
for groups in phnre.findall(text):
    phoneNumber = '-'.join([groups[0], groups[2], groups[4]])
    matches.append(phoneNumber)
    
# Email matches
for group in emailre.findall(text):
    matches.append(group)

# Printing result
print("Copy to clipboard: [Y] Yes [N] No")
ans = input().lower()

if ans == 'y':
    pc.copy('\n'.join(matches))
    print('\n'.join(matches))
else:
    print('\n'.join(matches))