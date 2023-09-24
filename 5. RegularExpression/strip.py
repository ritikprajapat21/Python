import re, pyperclip as pc

# Strip function
# Valid for one line only
def strip(str):
    stripre = re.compile('''
                        \S+ # For first word
                        .*  # For separator
                        \S+ # For Another word
                        ''', re.VERBOSE)
    return stripre.search(str).group()

# Taking input
print("Copy password from clipboard: [Y] Yes [N] No")
ans = input().lower()
if ans == 'y':
    print("String copied")
    string = str(pc.paste())
    print(string)
else:
    print("Enter your password:")
    string = input()

print(strip(string))