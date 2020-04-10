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
from enum import Enum


Color = Enum("Color", "coeur carreau pique trefle")
	
Valeur = Enum("Valeur", "SEPT HUIT NEUF VALET DAME ROI DIX AS")

class Card:
	def __init__(self, valeur = None, couleur = None):
		self.couleur = couleur
		self.valeur = valeur


	def __str__(self):
		p = str(Color(self.couleur).name)
		q = str(Valeur(self.valeur).name)
		return (q + " de " + p)
        
	def points_carte (self):
		if (self.valeur == Valeur.SEPT) or (self.valeur == Valeur.HUIT) or (self.valeur == Valeur.NEUF):
			self.points = 0
		if self.valeur == Valeur.DIX :
			self.points = 10
		if self.valeur == Valeur.VALET:
			self.points = 2
		if self.valeur == Valeur.DAME :
			self.points = 3
		if self.valeur == Valeur.ROI :
			self.points = 4
		if self.valeur ==  Valeur.AS :
			self.points = 11
	def strength(self):
		return self.valeur.value
card1 = Card(Valeur.ROI, Color.PIQUE)
card2 = Card(Valeur.DIX, Color.PIQUE)
print("Le joueur 1 joue la carte", card1) 
print("Le joueur 2 joue la carte", card2)
print("qui a la meilleure carte ?")

## maintenant on compare des cartes
# atout ? 
p1 = card1.points
p2 = card2.points

if p1 == p2:
    print("Égalité") # Ce cas n'est pas censé se produire dans le cadre de la belotte
elif p1 > p2:
    print("C'est J1 qui gagne avec", card1)
else:
    print("C'est J2 qui gagne avec",card2)
			
		
else:
	print("FIXME")
        

print("Et ça vaut ", card1.points + card2.points)

 
