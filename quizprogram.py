questions=(" What is the capital of France?",
           "What is the largest planet in our solar system?",
           " Who wrote the play Romeo and Juliet?",
           "What is the chemical symbol for water?",
           "What year did the first moon landing occur?")

options = [
    ["a. Berlin", "b. Madrid", "c. Paris", "d. Rome"],
    ["a. Earth", "b. Saturn", "c. Jupiter", "d. Mars"],
    ["a. Charles Dickens", "b. Mark Twain", "c. William Shakespeare", "d. Jane Austen"],
    ["a. CO₂", "b. O₂", "c. H₂O", "d. NaCl"],
    ["a. 1965", "b. 1969", "c. 1972", "d. 1980"]]

answers=("C","C","C","C","B")
guesses=[]
score=0
question_num=0

for question in questions:
    print("------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("Enter(A,B,C,D):  ").upper()
    guesses.append(guess)
    if guess ==answers[question_num]:
        score+=1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num+=1


print("---------------------")
print("    RESULTS")
print("---------------------")

print("answers: ",end="")
for answer in answers:
    print(answer,end=" ")
print()

print("guesses: ",end="")
for guess in guesses:
    print(guess,end=" ")
print()

score=int(score/len(questions)*100)
print(f"your score is :{score}%")
