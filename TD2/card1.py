
# enum Couleurs : ...
# dict couleurs = { ... }

class Card:
    couleur = ...
    hauteur = ...
    points = ...

    # def is_atout():
    #     ...

    # def a_ete_jouee():
    #     ...

    

COEUR, CARREAU, PIQUE, TREFLE = (0, 1, 2, 3)

card1 = Card()
card1.couleur = 'coeur'
card1.couleur = COEUR
card1.couleur = 'C'
card1.couleur = Couleurs.COEUR
# fixme : décider ce que je fais pour couleur


VALET, DAME, ROI = 11, 12, 13  # et on ne ferait que des entiers
card1.valeur = 'As'
card1.valeur = 'Roi'
card1.valeur = REINE
card1.valeur = 10
card1.valeur = '10'
# fixme: décider ce que je fais pour valeur
# fixme: hauteur ou valeur
# fixme: As=1 ou As=14 ?


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
        

