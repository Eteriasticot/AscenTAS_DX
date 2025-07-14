Premièrement, vous devez installer python et les librairies nécessaires.

1. Installer python
Vous pouvez juste aller sur https://www.python.org et installer la dernière version.

2. Installer les librairies
Il suffit d'ouvrir un terminal de commande et taper les commandes 'pip install pywin32', 'pip install pygetwindow', 'pip install pyautogui' et 'pip install pydirectinput'.

3. Faire votre TAS
Vous pouvez maintenant écrire dans le fichier inputs.txt. 'u' correspond à 'flèche haut', 'd' à 'flèche bas', 'l' à 'flèche gauche', 'r' à 'flèche droite', 'j' au saut ou dive, 'f' au dash et 'e' à 'entrée'.
Gardez un seul input par ligne en utilisant ce format : 'r 00:12.345'. Le programme devrait fonctionner en n'écrivant pas les minutes tant qu'elles sont à 0 mais le rendu final du fichier txt serait laid. Si votre run dépasse une heure, continuez d'itérer les minutes pour rester dans le format 'xx:xx.xxx', les décimales sont parfaitement optionelles.
Pour tous les inputs à part sauter, dash et entrée, chaque appel à cet input va inverser son état, donc si on n'a aucun input activé et qu'on écrit 'r xx:xx.xxx', l'input droit restera actif jusqu'au prochain appel de cet input.

4. Jouer votre TAS
Une fois que vous avez fini votre fichier .txt, enregistrez le, démarrez votre jeu et restez dans le menu principal, sur le bouton start ou continue et lancez le fichier python. Le jeu se remettra au premier plan et supprimera votre save avant de jouer les inputs indiqués dans le fichier .txt.

Amusez vous à faire votre TAS