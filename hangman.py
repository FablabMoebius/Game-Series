def display_incomplete_word(word, guessed_letters, bad_letters, attempts_left):
    display_word = []
    for letter in word:
        if letter in guessed_letters:
            display_word.append(letter)
        else:
            display_word.append('_ ')
    print("-" * 20)
    print(f"essais restants : {attempts_left}")
    print(' '.join(display_word))
    print(f"Lettres éliminées : {' '.join(bad_letters) if bad_letters else 'Aucune'}")
