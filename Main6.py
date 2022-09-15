nombre = input("ingresa tu nombre : ")
print("\n Hola",nombre," Este es un concurso de preguntas y respuestas,responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta \n")


def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Marca (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("Correcto es la respuesta!")
        return 1
    else:
        print("No es la respuesta!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# -------------------------
def play_again():

    response = input("Quieres volver a intentar? (si ó no): ")
    response = response.upper()

    if response == "si":
        return True
    else:
        return False
# -------------------------


questions = {
 "Cuando fue indepencia de Perú?: ": "C",
 "En que año inicio la primera guerra mundial?: ": "C",
 "Que descubrio Einstein?: ": "A",
 "Quien descubrio la bateria electrica?: ": "A"
}

options = [["A. 26 de Julio","B. 27 de Julio","C. 28 de Julio","D. 29 de Julio"],
          ["Ä. 1912","B. 1913","C. 1914","D. 1915"],
          ["A. Teoria de la relatividad","B. Elementos radioactivos","C. Fotografia a color","D. Calculo Integral"],
          ["A.  Alessandro Volta","B. Leonardo Da Vinci","C. Voltaire","D. Issac Newton"]]

new_game()

while play_again():
    new_game()

print("Gacias por participar¡¡")