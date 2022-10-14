from lazyme.string import color_print # importing the module that helps display colors

print("Hi there! Welcome to this Trivia.")

score = 0 # the score that will increase by 1 everytime the user answers correctly
questions = 5 # the number of questions

while True:
    question = input("\n1. Is Python a creature or a programming language? \na) Programming language\nb) Creature\nAnswer: ").lower()
    if question == "programming language":
        color_print("Correct! It is both actually 1+", color = 'green')
        score += 1 # increasing the score value by 1
        break
    elif question == "creature":
        color_print("Correct! It is both actually 1+", color = 'green')
        score += 1 # increasing the score value by 1
        break # breaking out of the loop if answered correctly
    else:
        color_print("Invalid Input", color = 'yellow')
        continue # continuing the loop if entered an invalid input

while True:
    question = input("\n2. What is a float in Python, JavaScript, Java, and Ruby? \na) Even number\nb) Decimal number\nAnswer: ").lower()
    if question == "decimal number":
        color_print("Correct! 1+ ", color='green')
        score += 1
        break
    elif question == "even number":
        color_print("Incorrect! It is decimal number.", color='red')
        break
    else:
        color_print("Invalid Input", color = 'yellow')
        continue

while True:
    question = input("\n3. What is HTML used for? \na) Game development\nb) Web development\nc) App development\nAnswer: ").lower()
    if question == "web development":
        color_print("Correct! 1+", color='green')
        score += 1
        break
    elif question == "game development":
        color_print("Incorrect! It is Web development. ", color='red')
        break
    elif question == "app development":
        color_print("Incorrect! It is Web development. ", color='red')
        break
    else:
        color_print("Invalid Input", color = 'yellow')
        continue

while True:
    question = input("\n4. What does OOP stand for in programming? \na) Out of print\nb) Object oriented programming\nc) Out of place\nAnswer: ").lower()
    if question == "object oriented programming":
        color_print("Correct! 1+", color='green')
        score += 1
        break
    elif question == "out of print":
        color_print("Incorrect! It is Object Oriented Programming.", color='red')
        break
    elif question == "out of place":
        color_print("Incorrect! It is Object Oriented Programming.", color='red')
        break
    else:
        color_print("Invalid Input", color = 'yellow')
        continue

while True:
    question = input("\n5. How should you pronounce C#? \na) See hashtag\nb) See sharp\nAnswer: ").lower()
    if question == "see sharp":
        color_print("Correct! 1+", color='green')
        score += 1
        break
    elif question == "see hashtag":
        color_print("Incorrect! It's see-sharp.", color='red')
        break
    else:
        color_print("Invalid Input", color = 'yellow')
        continue

# printing out the scores in numbers and percentage

if score >= 3:
  # green
  color_print("\nYou have got " + str(score) + "/" + str(questions) + " correct.", color='green')
  color_print("You have got " + str(questions - score) + "/" + str(questions) + " incorrect. ", color='green')
  color_print("You have got {:.1f}% of the questions correct.".format(score / questions * 100), color='green')
else:
  # red
  color_print("\nYou have got " + str(score) + "/" + str(questions) + " correct.", color='red')
  color_print("You have got " + str(questions - score) + "/" + str(questions) + " incorrect. ", color='red')
  color_print("You have got {:.1f}% of the questions correct.".format(score / questions * 100), color='red')
