import random


def plus_minus_game(max_number=99):
    print(f"Je pense à un nombre entre 1 et {max_number}, à toi de le deviner !")
    secret_number = random.randint(1, max_number)

    for attempt in range(1, 8):
        guess = int(input(f"Proposition (essai {attempt}): "))
        if guess < secret_number:
            print("+")
        elif guess > secret_number:
            print("-")
        else:  # equal
            print(f"Félicitations, tu as trouvé en {attempt} essais !")
            break
    else:
        print("Désolé, tu as perdu !")


print("Bienvenue !")
plus_minus_game()
while True:
    answer = input("Veux-tu rejouer ? (oui/non)")
    if answer == "oui":
        plus_minus_game()
    else:
        break
print("Au revoir !")