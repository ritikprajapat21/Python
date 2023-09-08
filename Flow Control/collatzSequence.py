def collatz(number):
    if number == 1:
        return
    if number % 2 == 0:
        print(number // 2)
        collatz(number // 2)
    else:
        print(3 * number + 1)
        collatz(3*number + 1)


try:
    print("Enter a number:")
    number = int(input())
    if number > 0:
        collatz(number)
    else:
        print("Enter a positive number")
except ValueError:
    print("Invalid Input! Enter a integer value")
