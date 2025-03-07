class Rabbit:
    """Définit la classe Rabbit."""

    def __init__(self, name) -> None:
        """Définit le constructeur de l'objet Rabbit.
        
        Les paramètres de la méthode __init__() seront utilisés
        pour valoriser les attributs :
          - name,
          - et color.
        """
        self.name = name
        self.weight = 150  # Définit un attribut avec une valeur fixe

    def jump(self, other):
        """Définit une méthode de la classe Rabbit.

        Prend en paramètre :
          - other : qui représente une autre instance de la classe Rabbit.
        """
        print(f"{self.name} sautille vers {other.name} qui pèse {other.weight} !")


# Instancie les objets de la classe Rabbit.
potilapin = Rabbit("Potilapin")
grolapin = Rabbit("Grolapin")

# Appel de la méthode jump de potilapin.
potilapin.jump(grolapin)
# Output: Potilapin sautille vers Grolapin qui pèse 150g !

# On écrase la valeur 150 par la valeur 50 de l'objet grolapin
grolapin.weight = 50

# Appel de la méthode jump de potilapin.
potilapin.jump(grolapin)
# Output: Potilapin sautille vers Grolapin qui pèse 50g !
