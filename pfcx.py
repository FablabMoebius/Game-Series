win_map = {
    "P": ["C", "L"],
    "F": ["P", "S"],
    "C": ["F", "L"],
    "S": ["P", "C"],
    "L": ["P", "S"]
}
player_one = input("Choix du joueur 1 : ")
print("\n" * 200)
player_two = input("Choix du joueur 2 : ")

print("Joueur 1 :", player_one)
print("Joueur 2 :", player_two)

if player_one == player_two:
    print("Match nul")
elif player_two in win_map[player_one]:
    print("Jouer 1 a gagné !")
else:
    print("Joueur 2 a gagné !")
