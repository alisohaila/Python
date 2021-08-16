print("Hi there! Welcome to Sohaila Ali's official game:) ")
play = input("Do you want to play? ").lower()
answer = "yes"
if play == answer:
    print("Okay, let's go! ")
else:
    print("Alright, bye! ")
    quit()

score = 0
num_of_questions = 5

while True:
    question = input("1. Is Python a creature or a programming language? ").lower()
    if question == "programming language":
        print("Correct! It's both actually 1+")
        score += 1
        break
    elif question == "creature":
        print("Correct! It's both actually 1+")
        score += 1
        break
    else:
        print("Invalid Input")
        continue

while True:
    answer = "decimal number"
    question = input("2. What is a float in Python, JavaScript, Java, and Ruby? (even number/decimal number)  ").lower()
    if question == answer:
        print("Correct! 1+ ")
        score += 1
        break
    elif question == "even number":
        print("Incorrect! It is decimal number")
        break
    else:
        print("Invalid Input")
        continue

while True:
    answer = "web development"
    question = input("3. What is HTML used for? (Game development/web development/app development) ").lower()
    if question == answer:
        print("Correct! 1+")
        score += 1
        break
    elif question == "game development":
        print("Incorrect! It is Web development! ")
        break
    elif question == "app development":
        print("Incorrect! It is Web development! ")
        break
    else:
        print("Invalid Input")
        continue

while True:
    answer = "object oriented programming"
    question = input("4. What does OOP stand for? (Out of Print/Object Oriented Programming/Out Of Place) ").lower()
    if question == answer:
        print("Correct! 1+")
        score += 1
        break
    elif question == "out of print":
        print("Incorrect! It is Object Oriented Programming")
        break
    elif question == "out of place":
        print("Incorrect! It is Object Oriented Programming")
        break
    else:
        print("Invalid Input")
        continue

while True:
    answer = "see-sharp"
    question = input("5. How do you pronounce C#? (see-hashtag/see-sharp) ").lower()
    if question == answer:
        print("Correct! 1+")
        score += 1
        break
    elif question == "see-hashtag":
        print("Incorrect! It's see-sharp")
        break
    else:
        print("Invalid Input")
        continue


print("You've got " + str(score) + "/" + str(num_of_questions))
