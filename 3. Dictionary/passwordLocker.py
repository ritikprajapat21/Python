#! python3
# An insecure version of password manager

PASSWORDS = {
    'email': 'Hihwq332e',
    'ibm-cloud': 'Hojio23jsadk',
    'gdsc': 'oijdi334',
}

import sys, pyperclip

if len(sys.argv) < 2:
    print("Usage: python passwordLocker.py [account] - copy account password")
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f"Password for {account} has been copied in the clipboard")
else:
    print(f"Password for {account} is not available")