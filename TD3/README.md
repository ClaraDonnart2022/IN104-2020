# Intro

- Quiz : quelle est la bonne plage de valeurs pour "age" ?
  ça dépend de l'appli : 
      - humain : int entre 0 et 122? 200? 
      - Benjamin Button ?  int négatif ?
      - un enfant de <5 ans ? il utilise 3 ans et demi, 18 mois, ... : float ? fraction ? 
      - un arbre : 0 < int < 2000
      - un composé radiactif (float)
      - un git lg ?

- Droits d'écriture sur https://github.com/JDGaraudEnsta/IN104-2020
  est-ce une bonne idée de donner les droits d'écriture sur la branche dev et sous-branches ; et me réserver master ?

- Autonomie : 
  Stack Overflow
  Dive into Python
  Fluent Python - Ramalho, Luciano
  
  Revue de code (par votre binome, puis par moi)

- résoudre un conflit : https://github.com/JDGaraudEnsta/misc/pulls


# Bilan du cours

Avez-vous déjà développé en faisant du TDD ? (oui: Gradescope, et un peu card2.py la semaine dernière)

Les 3 messages importants :
- p4 : c'est le client qui écrit les tests scenarios. 2 bonnes raisons : 
  - le client fait ce qu'il veut, 
  - le programmeur a moins de boulot
  Le programmeur écrit aussi des tests unitaires.

- p7 : je modulerais le message, écrire plusieurs tests scenarios permet de converger plus rapidement sur une interface de l'objet
  TDD to design a great interface

- p30 : unittest, les 3 trucs à savoir faire à la fin du TD3

- p31 : 
  TDD -> doc -> rapid prototyping
  maintenir une TODO-list.md


# Discussions

- git workflow -> quel va être le workflow pour TD3 ? et pour TD4+ ?
  - dépôt centralisé ? intégrateur, fork, 
  - la bonne idée, ça va être de faire celui que je leur conseille par la suite (centralisé, master + dev_user, pas de fork).
  - ou alors, ceux qui ne sentent pas trop les branches peuvent tout faire dans master, et merger les branches le plus vite possible.

- correction TD2 : 
  - démo diff + patch (méthode 1985-)
  - démonstration du pull-request

- gradescope : c'est un exemple d'intégration continue (et c'est pour ça qu'on vous embête avec)

- ce qu'on veut, c'est du code juste, testé, maintenu, couvert

- pour arriver à cela, on veut du code simple et lisible

        # good
        if card1 > card2 : ...
        
        # probably not good (will be hard to add trumps):
        if card1.couleur == card2.couleur:
            if card1.valeur > card2.valeur :
            print("C'est J1 qui gagne avec", card1)
        else:
            print("C'est J2 qui gagne avec", card2)
        

- et réutiliser au mieux les bonnes fonctions existantes. Ex:
    
        # good:
        winner = max([card1, card2, card3, card4])
        
        # bad
        if (card1 > card2) and (card1 > card3) and ...: 
        ...
        winner = card1

        # maybe even better:
        winner = max([card1, card2, card3, card4], key=couleur)
        
        
- croquis self (dans la classe) vs. card (hors de la classe) : en fait c'est la même chose.
  

# TD 3 

https://diveinto.org/python3/unit-testing.html
https://realpython.com/python-testing/





# Travail demandé

(fixme: c'est pas bon, faire les classes Deck, Players, Hand, Game sont plus compliquées que compléter Card)


- chaque groupe a une mission différente : ajouter des fonctionnalité à la classe Card
  - 1: atouts à la belote
  - 2: bridge
  - 3: tarot
  - 4: syntaxe  card1 < card2
  - 5: correction du bug du 10
  - 6: tests unitaires de couverture de l'existant
  - 7: Deck : shuffle() et deal()
  - 8: Players, Game, ... ? architecure globale du jeu
Le groupe 5 qui a le truc le plus simple devient aussi intégrateur !


