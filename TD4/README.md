
# TD4 

- Prise en main de  [hanabi](https://github.com/JDGaraudEnsta/hanabi).
- Installation du module 
- Découverte du module (soit en lisant le répertoire `src`, soit en lisant la `doc` auto-générée).
- Poursuite du travail sur les tests unitaires (dans le cas hanabi cette fois-ci).



# Conclusion des TD3 et TD4

On a vu aujourd'hui : 

- pourquoi les tests (unitaires et du client final) sont utiles
- qu'on ~peut~ doit les écrire avant le code
- que `unittest` est un bon module pour automatiser tout ça

J'ai mentionné (probablement trop vite) la méthodo de développement :

    test -> doc -> rapid prototyping -> code

mais pas eu le temps de la mettre en pratique. C'est une très jolie façon de faire, on en rediscute évenutellement dans 15 jours.


Pour que vous ne perdiez du temps avec la compil de la doc (sphinx n'est pas toujours installé), je l'ai ajoutée dans `hanabi/doc/html-c7e855d/index.html`.


Pour dans quinze jours : 

- s'entrainer à utiliser `unittest`
  - en faisant l'exercice "roman numbers" de Dive Into Python
  - en complétant TD4/hanabi_unittest.py
    Pour ce TD4/hanabi_unittest.py, n'hésitez pas à proposer en continu vos contributions.
    Commencez par les faire dans votre branche `dev_<prenom>`, demandez à votre binome si ça lui semble bien, puis à moi.
    J'ai (en principe) protégé la branche master en écriture : il vous faudra ensuite faire un merge request vers `master` pour que tout le monde profite de votre nouveau test.
  - chaque étudiant doit obligatoirement avoir fait (au moins) une merge request d'ici la prochaine fois (et que celle-ci soit acceptée, donc ça veut dire ne pas le faire la veille du TD5 !)
    

- apprendre les règles du jeu hanabi (le mieux pour cela : quelques parties sur BGA)

- lire une (ou plus) des références biblio de https://github.com/JDGaraudEnsta/hanabi#bibliography
  Les articles ne sont pas évidents à comprendre, préparez des questions.

- prendre en main le module hanabi
  - en ajoutant des test unitaires (cf. ci-dessus)
  - en écrivant votre premier robot-qui-joue (inspirez-vous de `src/hanabi/ai.py`).
    J'ai essayé d'éclaircir la façon de s'en servir : `test/test_ai_cheater.py` fonctionne en l'état.
    Et `test/test_new_ai.py` vous montre comment utiliser votre propre ai (que vous auriez codée dans un fichier `my_new_smart_ai.py`).

- pendant cette prise en main, vous trouverez probablement que la doc n'est pas claire, que le code peut être amélioré, qu'une fonction mériterait un nom plus adapté, que la classe Game ne respecte pas les vraies règles du jeu (c'est un développement en cours dans la branche StrictRules).
  N'hésitez pas à interagir là-dessus : on peut s'autoriser à modifier `src` dans les 15 jours à venir, mais à partir de TD5 il sera figé pour qu'on parte tous sur des bases communes.

