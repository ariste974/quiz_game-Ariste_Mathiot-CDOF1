# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 13:58:18 2025

@author: arist
"""
questions_capitales = (
    "Quelle est la capitale de la France?: ",
    "Quelle est la capitale du Japon?: ",
    "Quelle est la capitale du Brésil?: ",
    "Quelle est la capitale du Canada?: "
)

options_capitales = (
    ("A. Paris", "B. Berlin", "C. Madrid", "D. Rome"),
    ("A. Tokyo", "B. Séoul", "C. Beijing", "D. Bangkok"),
    ("A. Brasília", "B. Rio de Janeiro", "C. Santiago", "D. Lima"),
    ("A. Ottawa", "B. Toronto", "C. Vancouver", "D. Montréal")
)

answers_capitales = ("A", "A", "A", "A")

questions_histoire = (
    "En quelle année a eu lieu la Révolution française?: ",
    "Qui a été le premier président des États-Unis?: ",
    "Quel empire a construit le Colisée?: ",
    "Quelle guerre a eu lieu entre 1939 et 1945?: "
)

options_histoire = (
    ("A. 1789", "B. 1776", "C. 1812", "D. 1914"),
    ("A. George Washington", "B. Abraham Lincoln", "C. Thomas Jefferson", "D. John Adams"),
    ("A. Empire romain", "B. Empire grec", "C. Empire byzantin", "D. Empire ottoman"),
    ("A. Seconde Guerre mondiale", "B. Première Guerre mondiale", "C. Guerre de Sécession", "D. Guerre froide")
)

answers_histoire = ("A", "A", "A", "A")

questions_calcul = (
    "Combien font 7 x 8 ?: ",
    "Si tu as 100 et que tu enlèves 35, combien reste-t-il ?: ",
    "Combien font 12 + 15 ?: ",
    "Combien font 144 ÷ 12 ?: "
)

options_calcul = (
    ("A. 56", "B. 49", "C. 64", "D. 48"),
    ("A. 65", "B. 75", "C. 60", "D. 70"),
    ("A. 27", "B. 25", "C. 30", "D. 22"),
    ("A. 12", "B. 14", "C. 10", "D. 16")
)

answers_calcul = ("A", "A", "A", "A")

questions_biologie = ("How many elements are in the periodic table?: ",
                       "Which animal lays the largest eggs?: ",
                       "What is the most abundant gas in Earth's atmosphere?: ",
                       "How many bones are in the human body?: ",
                       "Which planet in the solar system is the hottest?: ")

options_biologie = (("A. 116", "B. 117", "C. 118", "D. 119"),
                   ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
                   ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
                   ("A. 206", "B. 207", "C. 208", "D. 209"),
                   ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers_biologie = ("C", "D", "A", "A", "B")

thèmes=["capitale","calcul","histoire","biologie"]
print("Choisis ton thème de QCM: ")
for thème in thèmes:
    print(thème, end=", ")
print()
sujet = input("Votre choix: ").lower()
a=0
while a<1:
    # Sélectionner les questions, options et réponses en fonction du thème choisi
    if sujet == "capitale":
        questions = questions_capitales
        options = options_capitales
        answers = answers_capitales
        a+=1
    elif sujet == "calcul":
        questions = questions_calcul
        options = options_calcul
        answers = answers_calcul
        a+=1
    elif sujet == "histoire":
        questions = questions_histoire
        options = options_histoire
        answers = answers_histoire
        a+=1
    elif sujet == "biologie":
        questions = questions_biologie
        options = options_biologie
        answers = answers_biologie
        a+=1
    else:
        print("Thème non valide.")
        sujet = input("Refaites votre choix: ").lower()
        


guesses = []
score = 0
question_num = 0

    
for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
input("Cliquez sur entrée pour fermer la page")