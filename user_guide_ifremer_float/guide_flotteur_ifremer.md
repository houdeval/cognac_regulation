# Guide d'utilisation du prototype l'Ifremer



# Mise en route du flotteur

## Avec controle total sur le flotteur

Brancher un clavier, une souris et un écran à la carte Raspberry. Utiliser une alimentation stabilisée pour éviter de consommer les piles (régler 10.8V, 4A à vide). Le mot de passe par défaut pour la Rasberry est *toor*

## A distance en se connectant au drone

Enlever l'aimant pour alimenter le flotteur avec les piles et attendre un peu pour que la Raspberry ait le temps de s'allumer.

Configuration de la Raspberry en mode AD-HOC en éditant le ficher */etc/network/interfaces* (à faire avant, lors du controle du flotteur avec un écran, une souris et un clavier):

```
auto wlan0
iface wlan0 inet static
address 192.168.0.13
netmask 255.255.255.0
wireless-channel 1
wireless-essid ifremer_float
wireless-mode ad-hoc
```

*ifremer_float* sera le nom du réseau visible à distance (peut être modifié).

L'adresse *192.168.0.13* sera celle de la Raspberry sur le réseau généré en mode Ad-Hoc. (peut être modifié).

Configuration de l'ordinateur pour accéder à la Raspberry :

Activer la fonction WIFI de l'ordinateur puis se connecter au SSID du réseau de la Raspberry (par défaut *ifremer_float*) et régler la connexion de sorte à ce que l'ordinateur soit sur le même sous-réseau que la Raspberry, par exemple.

```
IPv4: Manual
Adresse IP: 192.168.0.42
Sous-réseau: 255.255.255.0
```

(L'adresse IP peut-être changé du moment qu'elle est de la forme 192.168.0.X avec X différent de 0, 13 ou 255).

Ensuite, tester la connexion avec :

```
ping 192.168.0.13
```

On peut aussi directement se connecter en ssh avec le mot de passe *toor* :

```
ssh pi@192.168.0.13
[toor]
```

Si cette étape ne fonctionne pas, vérifier que le ssh est bien activé sur la carte grâce à l'interface générée par la commande :

```
sudo raspi-config 
```

# Mise hors tension du flotteur

Fermer tous les processus ROS sur la Raspberry pour éviter de causer des problèmes (fermer les terminaux en cours et vérifier s'il n'en reste pas par l'outil screen). Couper la Rasberry proprement avec par exemple la commande :

```
sudo shutdown now
```

Attendre un peu puis remettre l'aimant à l'aide des marques pour éteindre le flotteur complétement.


# Pré-deploiement du flotteur

- Vérifier que la connexion à distance est établie.

- Vérifier s'il faut changer les piles, tension de fonctionnement correcte pour 8 piles : entre 10 V et 12 V lorsque le vérin n'est pas en marche :
```
./get_batteries.zsh
```

- Vérifier les joints d'étanchéité (attention aux cheveux coincés dans les joints) et les branchements.

- Graisser les parois du piston et les joints si nécessaire.

- Faire le vide (voir procédure avec Olivier PEDEN) : utiliser capteur de pression interne (voir après) et être entre 600 mbar et 650 mbar. Noter la valeur de pression interne et attendre au moins trois heures avant de valider la tenue du vide en revérifiant la valeur. Si la valeur est légèrement différente de la valeur initiale à 20 mbar près, c'est normal, la pression varie aussi à cause de la température extérieur et de l'échauffement des composants électroniques dans le flotteur.

- Vérifier et éventuellement ajuster date: `sudo date 0906142918`


# Procédure de ballastage

- Choisir une position d'équilibre arbitraire en réglant la position du piston (de 0 [complètement sorti] à 5700 [complètement rentré], les commandes sont expliquées après). Cette position correspond au critère suivant : lors qu'on rentre un peu plus le piston par rapport à cette position, le flotteur doit commencer à couler. Le choix de cette position résulte d'un compromis entre le fait d'avoir les antennes bien sorties en surface ou le fait d'avoir beaucoup de réserve de flottabilité lors de la régulation en profondeur.

- Se placer à cette position puis ajouter du leste (feuilles de plomb avec scotch robuste, le scotch a également une masse à prendre en compte lors du ballastage) jusqu'à ce que le flotteur soit sur le point de couler.


# Utilisation principale du flotteur avec le middleware ROS

## Les points à connaître
Les différentes fonctions du flotteur sont exécutées grâce à l'outil ROS. Quelques points à savoir :

- Lorsque ROS est actif, toutes les commandes ROS peuvent être lancées depuis n'importe quel endroit dans un shell, excepté les commandes de lancement des nodes comme *roslaunch*.

- Les différentes fonctions sont exécutés corresondent à des topics émits par l'intermédiaire de nodes lancés dans des fichiers avec l'extension *.launch*. Pour lancer un tel fichier, il faut se placer dans l'espace de travail */pi/home/workspaceFlotteur* et lancer : 

```
roslaunch package_name ficher.launch
```
où *package_name* est le nom du package contenant le fichier *fichier.launch*.

Par exemple pour accéder aux capteurs, il faut lancer *driver.launch* dans le package *seabot* :

```
roslaunch seabot driver.launch
```



Il est également possible de lancer un fichier *.launch* en se plaçant directement à l'endroit où il se trouve et en exécutant : 
```
roslaunch ficher.launch
```

- Pour connaître le nom des topics en cours de fonctionnement, on peut exécuter depuis n'importe où la commande :

```
rostopic list
```

- Pour écouter les topics, la commande est :

```
rostopic echo nom_topic
```
où nom_topic est le nom complet du topic à écouter.

Par exemple, l'éxécution de *driver.launch* va générer le topic */driver/sensor_internal* correspondant au capteur de pression interne affiché par *rostopic list*.

Pour l'écouter, il suffit d'éxécuter la commande : 
```
rostopic echo /driver/sensor_internal
```

Similairement, la liste des nodes en cours est donnée par la commande :
```
rosnode list
```

Plus de détails sur les commandes les plus utiles sont fournis dans ce formulaire :

![Formulaire ROS page 1](https://github.com/houdeval/cognac_regulation/blob/master/user_guide_ifremer_float/ROScheatsheet_catkin-page-001.jpg)

![Formulaire ROS page 2](https://github.com/houdeval/cognac_regulation/blob/master/user_guide_ifremer_float/ROScheatsheet_catkin-page-002.jpg)

![Formulaire ROS page 3](https://github.com/houdeval/cognac_regulation/blob/master/user_guide_ifremer_float/ROScheatsheet_catkin-page-003.jpg)

- L'environment ROS permet l'utilisation de l'autocompletion tab

- Le shell permet de retrouver rapidement des commandes récentes en appuyant sur la flèche du haut :
Par exemple, si on a commencé à taper "piston" et que l'on fait la flèche du haut, le shell va proposer la dernière commande exécutée avec le mot "piston", en refaisant la flèche du haut, l'avant-dernière commande, etc...

- Les commandes ROS telles que *roslaunch ...* ou *rostopic echo ...* sollicitent le terminal comme des processus en exécutés en continue. Pour les arrêter, il faut faire `[ctrl-C]` dans le shell correspondant.

- TRES IMPORTANT : lorsque le flotteur va descendre sous l'eau, la connexion ssh avec l'ordinateur va être interrompue et la totalité des processus de la fenêtre en ssh vont s'arrêter donc le flotteur ne pourra plus continuer ses mission, pour cela il faut utiliser l'outil *screen*. Il permet également d'avoir plusieurs terminaux en cours avec une seule session ssh. Pour lancer un terminal qui ne sera pas interrompu lors de la déconnexion :

```
screen -a
```

(Pour savoir si on est dans un terminal "screen", il suffit de regarder le nom de la fenêtre). Dans ce type de terminal, il n'est pas possible de remonter avec la molette pour voir les données affichées plus haut dans la fenêtre.

`[ctrl-A] [ctrl-D]` détache le terminal sans le tuer en revenant à la session ssh d'origine et permet donc de garder en fonctionnement les tâches en cours malgré la déconnexion.

`[ctrl-D]` tue le terminal "screen" et revient à la session ssh d'origine.

Pour se rattacher à un terminal "screen":  `screen -r (tab pour autocomplétion)` Les différents terminaux "screen" sont identifiables par des nombres.

## Liste des commandes importantes

(les commandes *roslaunch ...* sont à rentrer à la racine de */workspaceFlotteur*).


- Lancement du fonctionnement des capteurs (attendre 30 secondes après la commande si on veut accéder au piston):
```
roslaunch seabot driver.launch
```

- Lancement du fonctionnement des capteurs avec génération de fichier *.bag* pour obtenir des graphs des résultats des missions (attendre 30 secondes après la commande si on veut accéder au piston), lancer ce node indépendemment permet par exemple de générer des logs sans lancer de mission de régulation, juste en étudiant le comportement du piston par exemple:
```
roslaunch seabot base.launch
```
- Lancement d'une mission de régulation:
```
roslaunch seabot mission.launch
```

- Afficher dans le shell les données du capteur de pression, température et humidité interne (après lancement de *driver.launch* ou *base.launch* ou *mission.launch*):
```
rostopic echo /driver/sensor_internal
```

- Afficher dans le shell les données du capteur de pression externe, la température affichée n'est pas précise, il s'agit de celle utilisée pour ajuster la valeur de la pression. La valeur de la pression n'est pas absolue mais est corrigée lors des missions (après lancement de *driver.launch* ou *base.launch* ou *mission.launch*):
```
rostopic echo /driver/sensor_external
```

- Afficher dans le shell les données du capteur de température externe (après lancement de *driver.launch* ou *base.launch* ou *mission.launch*):
```
rostopic echo /driver/sensor_temperature
```

- Afficher dans le shell les données du piston (30 secondes après lancement de *driver.launch* ou *base.launch* ou *mission.launch* à cause du reset fait par le PIC au démarrage du driver gérant le piston):
```
rostopic echo /driver/piston/state
```

- Afficher dans le shell les données de mission en temps réel (*mission.launch*):
```
rostopic echo /mission/set_point
```

# Planification des missions et mise à jour du code

## Planification d'une mission de régulation

Pour planifier une mission, il faut aller dans */workspaceFlotteur/src/seabot/mission*, ensuite créer ou éditer un fichier *.xml* comme les autres modèles.

Le bloc de code associé à la balise <offset> doit être commenté (<!-- -->) si la Raspberry n'est pas l'heure sinon une erreur sera générée. 

Dans la balise *loop*, *number* correspond au nombre de cycles à effectuer.

Dans la balise *waypoint* :

- *duration* correspond à la durée attribuée au flotteur pour appliquer sa consigne et la suivre, c'est à dire que si on veut que le flotteur se régule à 20 m en partant de la surface pendant 5 min, il faudra prendre en compte que le temps de descente jusqu'à 20 m est inclu dans les 5 min.

- *depth* correspond à la profondeur de consigne, pour faciliter l'initialisation de certaines variables, il est conseillé de faire un premier palier à 1 m de profondeur avant de descendre plus profond.

- *limit_velocity* correspond à la vitesse maximale en mètres par seconde que le flotteur est autorisé à atteindre lorsqu'il est loin de sa consigne (proportionnel au paramètre de vitesse nu de la régulation state feedback).

- *approach_velocity* correspond à la distance en metres à partir de laquelle que le flotteur est supposé adapter sa vitesse pour atteindre sa consigne avec précision (paramètre de distance delta de la régulation state feedback).


Ensuite une fois le fichier de mission éditer, il faut rentrer son nom en paramètre dans le fichier */workspaceFlotteur/src/seabot/launch/mission.launch* (*mission_depth_only.xml* par défaut): 

```
<param name="mission_file_name" value="nom_fichier.xml"/>
```

Ensuite pour lancer la mission, il suffit de lancer la commande :
```
roslaunch seabot mission.launch
```


## Planification d'une mission avec simple contrôle du piston

Pour utiliser le piston il va falloir le rendre accessible soit simplement par :
```
roslaunch seabot driver.launch
```
Soit si on veut générer des fichiers *.bag* (pour avoir les graphes) par :
```
roslaunch seabot base.launch
```
Ne pas oublier d'attendre 30 secondes pour le reset du PIC.
Ensuite le piston est directement controlable en éxécutant les fichiers suivant : 

- */workspaceFlotteur/src/seabot_driver/seabot_piston_driver/script/test_piston.py* envoie par défaut une seul commande de position au piston à la ligne *piston_position.publish(0)*. Cette commande doit être comprise entre 0 et 5700, la position de sortie du gros piston se situe à environ 1440.

- */workspaceFlotteur/src/seabot_driver/seabot_piston_driver/script/test_piston_dive_and_surface.py* permet d'automatiser le déplacement du gros piston en choissant sa position par *piston_position.publish(0)* et le temps d'attente entre chaque ordre avec *rospy.sleep(300)* où le temps est ici 300 secondes. Le nombre de cycles à effectuer est géré par la boucle for.

## Récapitulatif de la structure du code

L'architecture logicielle du code décompose *workspaceFlotteur* en plusieurs blocs. Si le code est amené à être exporté de la carte, il suffit de récupérer le dossier */workspaceFlotteur* sans les dossiers *build* ni *devel* qui sont des fichers de compilation. Dans le dossier *src* sont présents les différents packages :

- seabot : package principal qui contient les fichiers de missions et les principaux fichiers *.launch*

- seabot_depth_regulation : tout ce qui concerne l'élaboration de la commande lors de la régulation en profondeur

- seabot_driver : tout ce qui concerne les drivers des capteurs et du piston au niveau le plus bas dans ROS

- seabot_fusion : tout ce qui concerne l'analyse direct des données capteurs et le filtre de Kalman

- seabot_iridium : tout ce qui concerne la communication iridium

- seabot_mission : tout ce qui concerne la couche plus bas niveau du lancement des missions

- seabot_safety : tout ce qui concerne la mise en sécurité du flotteur

- seabot_simulator : outil de simulation intégré au flotteur

- seabot_waypoint_regulation : pour faire de la régulation horizontale mais inutile sur le flotteur de l'Ifremer

Par ailleurs, chaque package se compose au moins d'un fichier de compilation, très souvent d'un dossier *src* qui contient les codes bas niveau en *.cpp* et d'un dossier *launch* qui contient les fichiers *.launch* associés au package.

![Software architecture](https://github.com/houdeval/cognac_regulation/blob/master/user_guide_ifremer_float/ifremer_float_software_architecture.png)

## Modification de paramètres des fichiers *.launch*

Les différents paramètres situés dans les fichiers *.launch* peuvent être modifiés directement sans recompilation. La syntaxe utilisé est celle du langage XML, les commandes entre les balises <!--  --> correspondent donc à des commentaires.

## Modification du code en profondeur (fichiers .cpp et nom des fichiers)

Lorsque des fichiers *.cpp* ou des noms de fichiers ont été modifiés ou ajoutés, il faut recompiler le code pour que ces modifications soit prises en compte lors de l'éxécution.

Pour cela, il faut se placer à la racine de */workspaceFlotteur* et éxécuter la commande :

```
catkin_make -j2
```
La compilation est intelligence : seuls les fichiers modifiés devraient être recompilés. Parfois, il arrive que la compilation échoue sans message d'erreur, c'est à dire qu'elle est arrivée à terme mais les modifications n'ont tout de même pas été prises en compte (s'il n'y a pas eu de message de compilation en vert, cela signifie que le compilateur n'a détecté aucune modification). Pour remédier à ce problème, il faut effacer le dossier */workspaceFlotteur/build* et recompiler.

Si le problème persiste ou que des problèmes de chemins ou de noms de fichiers se présentent lors de la compilation, sans cause déterminée a priori, effacer le dossier */workspaceFlotteur/devel* et recompiler pourrait résoudre le problème.



# Test équilibrage

- avoir allumé le drone
- le mettre à l'eau
- faire un `screen -a`
- `roslaunch seabot calibration_equilibrium.launch`
- piston rentre jusqu'à ce que la profondeur dépasse 20cm et s'arrête
- un paramètre à régler: le paramètre de départ du piston (`start_piston_position` dans `seabot/script/calibration_equilibrium.py`), 1400 par exemple.
Avec houle il va falloir peut-être diminuer la valeur
Dans l'idéal il faut faire ça au port avant (i.e. sans houle).

Valeur obtenue à l'issue du test: `Piston Position`.

Cette valeur est à noter et reporter dans `seabot/launch/regulation.launch`, variable `offset_piston`. Mettre un peu moins pour qu'il soit flottant (50)



# Post-déploiement

## Récupération du flotteur

Vérifier humidité sur les parois du drone et sur les joints, fermer les terminaux "screen" et *sudo shutdown now* pour éteindre la raspberry manuellement. Attendre une minute et remettre l'aimant. Penser à bien nettoyer le flotteur à l'eau douce et essuyer avec de l'air comprimé et un chiffon, surtout au niveau de la vis du vide avant d'ouvrir le flotteur.

## logs

Les logs se trouvent dans le dossier caché dans */pi/home*: `.ros/`.

Ceux sont les fichiers .bag (pour générer les graphs) classés par date et les log des consoles (.ros/log/latest/).

Pour récupérer ces données avec le protocole scp, depuis l'ordinateur à distance et le dossier où on veut stocker les log, faire : 

```
scp pi@192.168.0.13:.ros/nom_ficher.bag .
```

Pour afficher les données des log sous forme de graph, il faut utiliser les outils situés dans */workspaceFlotteur/tools*.
Une manière de faire est de récupérer tout le dossier *tools* sur l'ordinateur à distance et d'éxécuter la commande suivant au même endroit où se trouve le dossier *tools* sur l'ordinateur :

```
python tools/rosbag/log.py /chemin_absolue/fichier.bag
```

Par exemple :
```
python tools/rosbag/log.py /export/home/ahoudevi/log_float_ifremer/2019-04-24-03-55-03_0.bag
```

# Diagnostiques de problèmes courants

- Une bonne partie des problèmes peut être diagnostiquée grâce à l'affichage de nombreuses données dans le terminal d'éxécution de la commande *roslaunch seabot mission.launch*. Pour faciliter la lecture de ces données, on peut les envoyer dans un fichier lors de l'éxécution de la commande pour pouvoir les interpréter plus tard, par exemple dans un fichier *fichier.log* : 
```
roslaunch seabot mission.launch > fichier.log
```

- Problèmes de régulation : se référer aux graphs provenant des logs et au tableau des erreurs liées aux packages safety ci-dessous :

![Safety errors](https://github.com/houdeval/cognac_regulation/blob/master/user_guide_ifremer_float/recap_chart_safety_mode.png)

- Problèmes de capteurs, éxécuter `i2cdetect -y 1` pour vérifier que les canaux sont bien présents, 76 (pression, température et humidité interne), 77 (température externe), 38 (piston), 40 (pression externe). On doit en avoir 4.

- Test piston sinus (si moteur fonction bien): `roslaunch seabot test_sinus.launch`

- vérifier état batterie:
`./get_batteries.zsh`

- Le flotteur semble stopper sa mission après l'avoir commencée (bien vérifier si le terminal utilisé était en "screen").



# Subtilités

- Le capteur de pression ne fonction que si la ligne *sudo sh -c 'echo "Y" >/sys/module/i2c_bcm2708/parameters/combined'* est activée.

Pour que la commande soit prise en compte à chaque démarrage, écrire simplement la commande à un endroit dans le fichier */etc/rc.local* :
```
echo "Y" >/sys/module/i2c_bcm2708/parameters/combined
```
- Les butées de fin de course du piston été simulées (variables *switch_in* et *switch_out*).

- La butée de mi-course du flotteur n'est pas utilisée mais la variable est lisible (*switch_halfway*).

- Le code de Thomas se trouver sur *https://github.com/ThomasLeMezo/seabot* : attention le code du flotteur de l'Ifremer a été beaucoup modifié par rapport à la version de Thomas sur plusieurs point : adresse des batteries, adresse du capteur de température externe, gestion des switch, driver du capteur de pression externe, paramètres propres au caractéristiques physiques du flotteur différents, pas de facteur 4 pour la gestion de la position du piston, deux variables pour gérer la vitesse du piston au lieu d'une seule, variable get_version différente, nodes des capteurs non-utilisés commentés dans les *.launch* (centrale inertielle, propulseurs).


