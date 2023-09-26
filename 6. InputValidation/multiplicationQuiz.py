import pyinputplus as pyip
import random, time

numberOfQuestion = 10
correctAnswer = 0

for questionNumber in range(1, numberOfQuestion + 1):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    prompt = f"#{questionNumber} {num1} X {num2} = "

    try:
        ans = pyip.inputStr(prompt=prompt, allowRegexes=['^%s$' % (num1 * num2)], blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct!')
        correctAnswer += 1
        time.sleep(1)

print(f"You answered: {correctAnswer}/{numberOfQuestion}")