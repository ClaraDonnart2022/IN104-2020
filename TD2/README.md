# Questions git ?




# Questions cours OO ?

- quels sont les 3 messages importants ? 
- et le 4e mousquetaire : PEP-8 !!!


# TD 2 - 1e partie (30 min)

- faire tutorial.zip (cf. lien dans le cours)

- Faire tout de suite l'inscription Gradescope, ça peut prendre du temps.
  access code dans les diapos du cours

- Sous Linux, ne pas faire le tuto Unix (vous savez déjà faire) ; ne pas installer Anaconda ou WinPython : le python système est largement suffisant.
- Sous Windows : 
  - soit vous avez déjà un python d'installé, 
  - sinon je recommande le "noyau Linux embarqué" :  https://www.numerama.com/tech/158150-le-shell-bash-sous-windows-10-ce-quil-faut-savoir.html 

- Attaquer directement page 21, avec les Classes et Objects ; les exercices commencent page 25 !

Le TP est un texte à trou. Le script pour vérifier qu'on a juste :

    python3 autograder.py

et chacun des .py est executable, pour être testé individuellement : 

    python3 shopSmart.py 


(on verra la semaine prochaine que ça s'appelle du TDD).

## mise en jambe : 

- addition.py
- buyLotsOfFruit.py

## les classes : 

- shopSmart.py et shop.py



# TD 2 - 2e partie (80 min)

- on crée un (brouillon) de cas test (card1.py)
- on en déduit un cas test qu'on estime suffisamment intéressant à implémenter (card2.py)

- point important discuté, le triptyque (variable, valeurs, type), ou (instance, valeur, classe). Par exemple :

------------------------ | ----------------------------- | --------------
variable ou instance     | valeurs                       | type ou classe
------------------------ | ----------------------------- | --------------
age                      |   27                          | int
pression                 |   2.1e5                       | float
pi                       |   3.14                        | float
math.pi                  |   3.141592653589793           | float
card1                    |   ♠ (as de pique)             | Card
card2                    |   u"\U0001F0B1" (as de coeur) | Card
------------------------ | ----------------------------- | --------------

(on pourrait ajouter "plage de valeurs autorisées" mais je n'en ai pas vraiment parlé ce matin. À titre d'exo, vous pouvez réfléchir à ces plages.  Pour "age" c'est plus compliqué qu'il n'y parait, faites-moi penser à faire un quiz la semaine prochaine)

- Pour la semaine prochaine, remplir ce qui est "TODO" dans card2.py
- Pour ceux qui trouvent ça trop facile, créez un card3.py qui utilise des atouts.

