# Challenges Bomb

# Table des matières

- [Partie 1](#partie-1)
- [Partie 2](#partie-2)
- [Partie 3](#partie-3)
- [Partie 4](#partie-4)
- [Partie 5](#partie-5)

# Partie 1

1. Créer une classe nommée **Player** qui possède 2 attributs :
   - **life** (défaut : 100 PV)
   - **position_x** (défaut : 20)
2. Instancier votre personnage en lui trouvant un joli nom (ex: Mario, Peach).
3. Afficher la valeur de ses attributs.

# Partie 2

1. Récupérer la fonction **print_map** (tinyurl)
2. Visualiser la position de votre personnage en 1D en appelant cette fonction :  
   `print_map(player=<votre_personnage>)`
3. Changer sa position puis revisualisez-la.

# Partie 3

1. Créer une classe **Bomb** qui a les attributs :  
    - **position_x** (défaut : aléatoire entre 0 et 79)
    - **damage** (défaut : 10).
2. Instancier 3 bombes
3. Visualiser leurs positions en grâce à un seul appel **print_map** :    
  `print_map(bombs=<liste_de_bombes>)`

# Partie 4

1. Modifier la classe **Bomb** pour y ajouter une méthode **move_to** :
    - qui prend en paramètre le **personnage**
    - qui déplace de 1 la bombe en **direction du personnage**.
2. Appeler cette nouvelle méthode sur chaque des bombes.
3. Viualiser le rendu avant et après les déplacements :
   `print_map(player=<perso>, bombs=<bombes>)`

# Partie 5

 1. Récupérer la méthode **is_colliding** https://tinyurl.com/iscolliding et modifier la classe Bomb pour l’intégrer.
 2. Appeler la méthode **is_colliding** après chaque move_to.
 `exploded = is_colliding(<player>)`
3. Détruire la bombe une fois qu’elle a “explosée” (la retirer de votre liste de bombes).
1. Faire se déplacer les bombes toutes les secondes vers votre personnage (en gardant l’affichage du rendu entre chaque itération) jusqu’à ce que:
    - le **personnage meurt**
    - ou qu’il n’y ait **plus de bombes**
2. Changer le nombre de bombes ou les dégats des bombes pour observer le changement.
