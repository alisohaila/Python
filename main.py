print("HEYYY!! Welcome to Sohaila Ali's official game:) ")
play = input("Do you want to play? ").lower()
answer = "yes"
if play == answer:
    print("Okay, let's go! ")

else:
    print("Alright, bye! ")
    quit()

score = 0
num_of_questions = 3

question = input("1. Is Python a creature or a programming language? ").lower()
if question == "programming language":
    print("Correct! It's both actually 1+")
    score += 1
elif question == "creature":
    print("Correct! It's both actually 1+")
    score += 1
else:
    print("Invalid Input")
    quit()

answer = "decimal number"
question = input("2. What is a float in Python, JavaScript, Java, and Ruby? (even number/decimal number)  ").lower()
if question != answer:
    print("Incorrect! It is decimal number")
else:
    print("Correct! 1+")
    score += 1

answer = 'web development'
question = input("3. What is HTML used for? (Game development/web development/app development) ").lower()
if question == answer:
    print("Correct! 1+")
    score += 1
else:
    print("Incorrect! It is Web development! ")

print("You've got " + str(score) + "/" + str(num_of_questions))
