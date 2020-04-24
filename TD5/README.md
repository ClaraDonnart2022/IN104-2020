# TD 5 - bilan

On n'a *pas* discuté de (y penser pour le TD6) :
- rapid prototyping
- invariants d'un objet pour les tests unitaires.


On a discuté aujourd'hui des points suivants : 

## class Card Deck Hand Game 

Pas de grosses difficultés de ce côté. Doc trop succincte ou manquant d'exemples par endroits.


## Fichier ai.py et classe AI 

À ce propos, vous avez tous noté que la fonction `Cheater.play` n'est pas un modèle à suivre : 
elle fonctionne mais fait ~100 lignes dont certaines sont indigestes ; 
dans un bon code, elle aurait été relue, refactorisée, splittée en 4-5 sous-fonctions élémentaires 
pour que le tout soit lisible, maintenable et améliorable.

Readability counts.



## Piège à éviter pour votre AI

Camille est tombée sur un os :
https://github.com/JDGaraudEnsta/hanabi/issues/11
Le symptome : le jeu plante avec une erreur `AttributeError: 'RandomAI' object has no attribute 'pop'`.

C'est effectivement un "piège" (pour les curieux, le code de `Game.turn` est écrit LBYL au lieu de "EAFP et duck-typing". cf https://docs.python.org/3/glossary.html).

La bonne solution, ce serait donc de corriger le bout de code de `Game.turn` pour que tout objet qui a une fonction `play` soit correctement reconnu (une fois fait, je fermerai l'issue #11).
Pour le moment, vous êtes forcés de dériver de `ai.AI`. Donc votre code de my_new_ai.py doit ressembler à :

```
import hanabi
class RandomAI(hanabi.ai.AI):
    def play(self):
        ...
```


## Listes par compréhension

Par exemple :

      precious = [ card for card in
                   self.other_players_cards
                   if (1+game.discard_pile.cards.count(card))
                       == game.deck.card_count[card.number] ]
                       
Il faut savoir que ça existe, c'est bien d'apprendre à s'en servir (peut-être sur des cas plus simples pour commencer).
Avec un peu d'habitude c'est plus lisible (et plus rapide) qu'une liste qu'on remplit au fur et à mesure par une boucle for.



## Python est interprété

Il est possible d'ajouter à la volée un nouvel attribut à une carte, par exemple :

    card = game.hands[1].cards[2]
    card.public_possibility_table = np.ones((5,5), dtype=np.bool)

puis de vous en servir pour suivre l'évolution des indices reçus sur cette carte (au sens de la méthode "Recommendation strategy").
(en langage compilé vous auriez été obligés de modifier ou dériver la classe Card pour lui ajouter un attribut ; où gérer la table à part).


Attention, c'est à double tranchant, si vous écrivez :

    card.color_hint = Color.Blue
    
mais que tout le reste du code utilise `color_clue` (au lieu de hint), vous aurez des mauvaises surprises (un langage compilé vous détecterait dès la compilation).
                   

## merge StrictRules vers master

Pour ceux qui voulaient voir un merge jusqu'au bout, j'ai noté les étapes du merge StrictRules -> master. 

C'est un peu long à écrire, mais les étapes "git" sont faciles. Le plus dur c'est la chasse aux bugs.


    git stat   # pour s'assurer qu'il n'y a pas de modifs non commitées sur master

    git tag -a LooseRules ed4311c -m 'Add a tag just before merging StrictRules (just in case)'

Alternativement, on pourrait aussi créer une branche avec `git checkout -b LooseRules`.
Comme on n'a pas prevu d'en continuer le développement, ce n'est pas indispensable.

Je switch sur la branch StrictRules

    git checkout StrictRules

et je la mets à jour des modifs de master

    git merge master


Il me dit qu'il n'a pas réussi à tout merge automatiquement.
On regarde où ça en est :

```
git stat

On branch StrictRules
Your branch is up to date with 'origin/StrictRules'.

You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Changes to be committed:
	new file:   FAQ.md
	renamed:    Week1.md -> Old/Week1.md
	renamed:    Week2.md -> Old/Week2.md
	renamed:    Week3.md -> Old/Week3.md
	renamed:    Week4.md -> Old/Week4.md
	modified:   README.md
    ...

Unmerged paths:
  (use "git add <file>..." to mark resolution)

	both modified:   src/hanabi/ai.py
	both modified:   src/hanabi/deck.py
```

Le premier paquet de fichiers, c'est tout ce qui s'est bien passé (on vérifie quand même que tout a l'air honnête).
Les 2 derniers fichiers (Unmerged paths), c'est ceux où il faudra une intervention humaine. 

Il y a plein de façons de résoudre ; à titre perso, j'ai l'habitude d'ouvrir les fichiers dans un éditeur de texte, et chercher les blocs du style (ici dans ai.py) :

    <<<<<<< HEAD
        if game.blue_coins >0:
            print ('Cheater would clue randomly:')
            return 'c'+random.choice('12345RGBWY')
    =======
        if game.blue_coins > 0:
            print('Cheater would clue randomly: cW')
            return 'cw'
    >>>>>>> master

puis de garder le meilleur des deux blocs (ici, celui du haut est plus malin).
Les logiciels comme kdiff, meld, les interfaces graphiques à git, vous mettent une couche conviviale sur cette opération.

À ceux qui m'ont demandé "comment je donne un indice à un joueur autre que le suivant", vous verrez que la branche StrictRules avait un bout d'exemple (dans la doc de Game.clue) :

        Example:
           hanabi> cWB    # is a white clue to Benji
           hanabi> c1     # is a 1 clue to next player
           hanabi> cRed   # is interpreted as a red clue to Elric, probably not what you expected!

@ Guillaume ou Florian (j'ai oublié lequel de vous deux j'avais chargé d'ajouter cet exemple) : il est maintenant plus facile d'ajouter au Cheater qu'il choisisse un joueur cible au hasard.


Revenons au merge ; le code est maintenant syntaxiquement correct, j'en fais un commit :

    git stat  # pour vérifier qu'il n'y a plus de "Unmerged paths"
    git commit -m "Merge (update) branch StrictRules wrt. master"

On réinstalle la nouvelle version (par prudence, on nettoye bien avant) : 

    # sous linux
    make distclean
    make module

    # sous windows
    pip3 uninstall hanabi
    supprimer les répertoires build, dist, egg-info
    python3 setup.py install --user



Et maintenant avant de push, il reste à vérifier que tous les tests sont ok : 

    cd test
    ./run_tests.sh
    
    ========= Summary ===========
    test       score ref  status
    game1.py       4   4    Ok    
    game2.py      20  20    Ok    
    game3.py      24  24    Ok    
    game4.py       0  25  Failed  
    game5.py       0  21  Failed  
    game6.py       0  21  Failed  
    game7.py      23   0  No ref  
    game8.py       0   0  No ref  

vous voyez que la modif StrictRules a cassé les test 4-5-6 (et peut-être aussi 7 et 8, mais ils n'avaient pas de ref, donc on ne sait pas si c'est grave:-/). 

Il ne reste plus qu'à les regarder (ça peut être long) :
- game4 : facile, il y est écrit "A perfect game by 2 Cheaters" ; donc on les refait jouer et on enregistre la nouvelle séquence de moves

- game5 : c'est plus compliqué : il contient des annonces interdites par StrictRules (par ex le tout premier indice d'Alice), donc le jeu se semble décalé ... mais en fait, le vrai souci c'est qu'il traine un bug dans la branch StrictRules : un jeton est consommé même quand le "clue" est refusé ; après correction le test5 marche aussi bien qu'avant.

- game6 : idem, souci de décalage, sur une ou deux annonces corrigées à la main.

- game 7 et 8, j'en ai profité pour ajouter les scores de références

- game 9 : ajouté pour s'assurer que 3 kaboum font un score de zero


Maintenant 100% des tests sont ok, et unittest_hanabi fonctionne toujours. Donc on peut commit et push :

    git stat ; git tkdiff   # toujours verifier avant un commit

    git add src/hanabi/deck.py src/hanabi/ai.py
    git commit -m 'Fix bug: a blue coin was used even if the the Clue was invalid'

    git add test/game9.py
    git commit -a -m "Fix all tests when using StrictRules"
    
    git push   # il va juste push la branch


Il ne reste plus qu'à faire un merge de la branche vers master.
En ligne de commande ce serait dans le genre de :

    git checkout master
    git merge StrictRules
    # en principe install et tests
    git commit -a -m "Merge back StrictRules into master"
    git push

Mais pour cette fois, je suis passé par github, qui, parce qu'il a vu que j'ai commité dans une branche, a tout de suite proposé de faire un pull-request, et c'était réglé en 3 clics (parce que pas de conflits).



## Mettre vos versions de hanabi à jour

Maintenant pour utiliser le bon décompte de points final, vous devez mettre à jour. 

Ceux qui ont juste cloné le dépôt hanabi, vous faites un `git pull`.

Ceux qui ont fait un fork, pour récupérer cette modif, je vous renvoie vers le blabla de l'an dernier :
https://github.com/JDGaraudEnsta/hanabi/blob/master/Old/Week2.md#git-workflow
il y a la version ligne de commande et la version via github.
