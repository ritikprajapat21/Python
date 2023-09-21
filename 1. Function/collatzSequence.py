# Write a function named collatz() that has one parameter named number. If
# number is even, then collatz() should print number // 2 and return this value.
# If number is odd, then collatz() should print and return 3 * number + 1.
# Then write a program that lets the user type in an integer and that keeps
# calling collatz() on that number until the function returns the value 1.
# (Amazingly enough, this sequence actually works for any integer—sooner
# or later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t
# sure why. Your program is exploring what’s called the Collatz sequence, 
# sometimes called “the simplest impossible math problem.”)

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
