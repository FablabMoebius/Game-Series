# Objectif 1 : Générer le choix de l'ordinateur
- Choisir une des lettres "P", "F" ou "C" aléatoirement
- Afficher le choix de l'ordinateur
  
indices : `choice`, `print`.

# Objectif 2 : Demander le choix du joueur
- Demander le choix du joueur ("P", "F", ou "C")
- Afficher le choix du joueur
  
indices : `input`, `print`.

# Objectif 3 : Comparer les choix (match nul)
- Afficher "match nul" si le joueur et l'ordinateur ont le même choix
  
indices : `if`, `==`.

# Objectif 4 : Comparer les choix (défaite)
- Afficher "Perdu" si :
  - L'ordinateur a choisi "P" et le joueur "C"
  - OU l'ordinateur a choisi "F" et le joueur "P"
  - OU l'ordinateur a choisi "C" et le joueur "F"
  
indices : `if`, `and`, (optionel) `or`.

# Objectif 5 : Comparer les choix (réussite)
- Afficher "Gagné !" si :
  - le joueur a choisi "P" et l'ordinateur "C"
  - OU le joueur a choisi "F" et l'ordinateur "P"
  - OU le joueur a choisi "C" et l'ordinateur "F"

indices : `if`, `and`, (optionel) `or`.

# Objectif 6 : Répéter le jeu
- Tant que le joueur gagne, rejouer une partie
  
indices : `if`, (optionel) `break`, `while`

# Objectif 7 : Gérer les vies
- Définir un nombre de vies de départ
- Répéter le jeu tant que le joueur a des vies
- Le joueur perd une vie quand il perd une partie contre l'ordinateur
  
indices : `if`, `-=`, `while`, (optionel) `break`, `>=` ou `<=` ou `>` ou `<`
