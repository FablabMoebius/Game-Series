# Challenges Bomb

# Table des matières

- [Partie 1](#partie-1)
- [Partie 2](#partie-2)
- [Partie 3](#partie-3)
- [Partie 4](#partie-4)
- [Partie 5](#partie-5)
- [Partie 6](#partie-6)

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
  `print_map(bombs=<liste_de_bombes>)`c

# Partie 4

1. Modifier la classe **Bomb** pour y ajouter une méthode **move_to** :
    - qui prend en paramètre le **personnage**
    - qui déplace de 1 la bombe en **direction du personnage**.
2. Appeler cette nouvelle méthode sur chaque des bombes.
3. Viualiser le rendu avant et après les déplacements :
   `print_map(player=<perso>, bombs=<bombes>)`

# Partie 5

1. Modifier la classe **Bomb** pour y ajouter une méthode **is_collision** :
    - qui prend en paramètre le **personnage**
    - qui réduit la vie du personnage si la bombe et le personnage se touche (la bombe explose). Les dégâts subits = montant l’attribut damage.
    - qui retourne **True/False** (booléen) : si collision ou non
2. Appeler la méthode **is_collision** après chaque move_to.
3. Détruire la bombe une fois qu’elle a “explosée” (la retirer de votre liste de bombes).
4. Modifier temporairement la position de votre personnage pour le placer sur l’une des bombes. 
5. Visualiser le rendu du jeu grâce à **print_map**.

# Partie 6

1. Faire se déplacer les bombes toutes les secondes vers votre personnage (en gardant l’affichage du rendu entre chaque itération) jusqu’à ce que:
    - le **personnage meurt**
    - ou qu’il n’y ait **plus de bombes**
2. Changer le nombre de bombes ou les dégats des bombes pour observer le changement.
