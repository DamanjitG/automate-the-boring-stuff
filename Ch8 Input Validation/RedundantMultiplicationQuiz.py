import random, time, re
import pyinputplus as pyip

regexNum = re.compile("\d+")
regexNotNum = re.compile("\D+")
quiz = {}
correctAnswers = 0

for i in range(10):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    quiz[str(num1)+" x "+str(num2)] = num1*num2

for question in quiz:
    print("What is " + question, end="?")
    timeStart = time.perf_counter() # Begin timer
    while True:
        answer = input()
        if regexNum.search(answer) == None or regexNotNum.search(answer) != None:
            print("This input is invalid. Please input a number.")
        else: break
    timeEnd = time.perf_counter()

    inTime = (timeEnd - timeStart) < 8
    correct = (int(answer) == quiz[question])

    if inTime and correct:
        print("Correct!")
        correctAnswers += 1
        time.sleep(1)
    elif inTime and not correct:
        print("Your answer was incorrect.")
        time.sleep(1)
    elif not inTime and correct:
        print("Your answer was correct, but you didn't answer fast enough!")
        time.sleep(1)
    else:
        print("Your answer was incorrect, and you took too long to answer.")

print("The quiz has ended.")
print("Your final score is: "+str(correctAnswers)+"/10")
    

        
    

