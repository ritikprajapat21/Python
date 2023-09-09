def characterCount(msg):
    count = {}
    for char in msg:
        if char != ' ':
            char = char.lower()
            count.setdefault(char, 0)
            count[char] += 1
    return count

msg = input("Enter a string: ")
count = characterCount(msg)
for k, v in count.items():
    print(f"Character {k} appeared {v} times")