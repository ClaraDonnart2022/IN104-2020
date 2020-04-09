"""
Module card2.

Definit une classe Card et un petit cas-test qui demontre son utilite.


TODO: 

  - coder la fonction str
  - le init qui prend 0 ou 2 parametres (indication : chercher sur StackOverflow "python optional arguments in initializer of python class")
  - coder points ; d'ailleurs, est-ce une fonction ou un attribut ? 
  - corriger le bug : qui est que le 10 est plus fort que Dame Roi Valet (7 8 9 V D R 10 As) 

  - bonus : ajouter les atouts
  - bonus : ajouter un setter qui empeche couleur = "VERTE"
"""


COEUR, CARREAU, PIQUE, TREFLE = (0, 1, 2, 3)
#valeur : 7, 8, 9, 10, 11, 12, 13, 14 

class Card:
    def __init__(self, valeur, couleur, points):
        self.couleur = couleur
        self.valeur = valeur
        self.points = points

    # def __init__(self, couleur, valeur):
    #     self.couleur = couleur
    #     self.valeur = valeur

    def __str__(self):
        return str(self.valeur) +" de "+ str(self.couleur)




    

# card1 = Card(10, COEUR)

card1 = Card(10,COEUR,10)


# card1.couleur = "VERTE"


card2 = Card(9,COEUR,0)

#
print("Le joueur 1 joue la carte ", card1) 
print("Le joueur 2 joue la carte ", card2) 
print("qui a la meilleure carte ?")

## maintenant on compare des cartes
# atout ? 
A=[0,0,0,0,0,0,0,7,8,9,13,10,11,12,14]

if card1.couleur == card2.couleur:
    if A[card1.valeur] > A[card2.valeur] :
        print("C'est J1 qui gagne avec ", card1) 
    else:
        print("C'est J2 qui gagne avec", card2) 
        

print("Et va vaut ", card1.points + card2.points," points.")
