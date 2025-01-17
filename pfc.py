import random

items = ["P", "F", "C"]
computer_choice = random.choice(items)
player_choice = input("Choisir parmis 'P', 'F', ou 'C': ")


print("Ordinateur:", computer_choice)
print("Joueur:", player_choice)


if computer_choice == player_choice:
    print("Match nul.")
elif (computer_choice == "P" and player_choice == "C") \
    or (computer_choice == "F" and player_choice == "P") \
    or (computer_choice == "C" and player_choice == "F"):
    print("Vous avez perdu !")
else:
    print("Vous avez gagné !")
