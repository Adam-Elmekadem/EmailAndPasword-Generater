questions = (("What is the chemical symbol for gold?"),
             ("Who painted the famous artwork 'Starry Night'"),
             ("Which planet in our solar system is known as the Red Planet?"),
             ("In which year did the Titanic sink?"))

options = (("A. Paris", "B. Canberra", "C. London", "D. Rabat"), 
           ("A. Leonardo da Vinci", "B. Pablo Picasso", "C. Vincent van Gogh", "D. Claude Monet"),
           ("A.Saturn", "B. Jupiter", "C. Mars", "D. Venus"),
           ("D. 1912", "B. 1914", "C. 1916", "D. 1918"))

answers = ("B", "C", "C", "A")
guesses = []
score = 0
question_num = 0

for question in questions :
    print("--------------------------------------")
    print(question)
    for option in options[question_num] :
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("WRONG!")
        print("The correct answer is: ", answers[question_num])
    question_num += 1
    print("--------------------------------------")

print("Your  answers: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()
print("answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
    
print("\nYour score is: ", score/len(questions)*100, "%")