"""
Cartes 
"""


COEUR, CARREAU, PIQUE, TREFLE = (0, 1, 2, 3)
#valeur : 7, 8, 9, 10, 11, 12, 13, 14 

class Card:
    def __init__(self):
        self.couleur = None
        self.valeur = None
        self.points = 0

        
    # def __init__(self, couleur, valeur):
    #     self.couleur = couleur
    #     self.valeur = valeur
    


card1 = Card()
card1.couleur = COEUR
card1.valeur = 10

card2 = Card()
card2.valeur = 9
card2.couleur = COEUR

#
print("Le joueur 1 joue la carte", card1) 
print("Le joueur 2 joue la carte", card2)
print("qui a la meilleure carte ?")

## maintenant on compare des cartes
# atout ? 

if card1.couleur == card2.couleur:
    if card1.valeur > card2.valeur :
        print("C'est J1 qui gagne avec", card1)
    else:
        print("C'est J2 qui gagne avec", card2)
else:
    print("FIXME")
        

print("Et va vaut ", card1.points + card2.points)
