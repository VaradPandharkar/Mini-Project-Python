questions = ("How many elements in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the abundant gas in Earth's atmosphere?: ",
             "How many bones are in human body?: ",
             "Which planet in the solar system is the hottest?: ")

options = (("A. 116","B. 117","C. 118","D. 119"),
           ("A. Whale","B. Crocodile","C. Elephant","D. Ostrich"),
           ("A. Nitrogen","B. Oxygen","C. Carbon-Dioxide","D. Hydrogen"),
           ("A. 206","B. 207","C. 208","D. 209"),
           ("A. Mercury","B. Venus","C. Earth","D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
scores = 0
question_num = 0

for question in questions:
    print("------------")
    print(question)

    for option in options[question_num]:
        print(option)

    guess = input("Enter (A ,B ,C ,D): ").upper()

    guesses.append(guess)

    if guess == answers[question_num]:
        scores += 1
        print("CORRECt!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is  the CORRECT answer")

    question_num += 1

print("answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()
 
scores = int(scores / len(questions) * 100)
print(f"Your scores is: {scores}%")