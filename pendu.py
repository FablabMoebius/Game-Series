word_to_guess = input("Saisissez le mot à deviner : ")
print("\n"*50)
bad_letters = set()
good_letters = set()
life = 11
while True:
    proposed_letter = input("Propose une lettre :")
    if proposed_letter in word_to_guess:
        print("bien vu !")
        good_letters.add(proposed_letter)
        if good_letters == set(word_to_guess):
            print("GG")
            break
    else:
        print("perdu")
        bad_letters.add(proposed_letter)
        life -= 1
        if life == 0:
            print("game over")
            break
    print("bonnes lettres :", good_letters)
    print("lettres éliminées :", bad_letters)
    print("vie restante:", life)
    for letter in word_to_guess:
        if letter in good_letters:
            print(letter, end="")
        else:
            print("-", end="")
    print()
