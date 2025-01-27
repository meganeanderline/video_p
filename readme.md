DOCUMENTATION DU PROJET


ci joint le lien de visualisation de la demo relative au projet https://drive.google.com/file/d/1s9hjICdMlmxRELVBurA8QZfyWxlKi62o/view?usp=sharing

Ont pris part à ce projet les étudiants :
  
  . Nguefo Momo
  . Chuente Olivier
  . Ekoto Akono
  . Bile Owona
  . Djomgoue Brandon

1.	Introduction / Résumé



	Présentation du projet
                   
      Ce projet s'inscrit dans le cadre du cours de Cloud Computing et l’objectif attendu est la réalisation d'un pipeline hybride de traitement vidéo. Celui-ci est constitué de plusieurs phases intégré dans deux modules principaux.
      
•	Le premier module implémenté en locale comprend les étapes suivantes :
            -  Downscale : il s'agit ici de compresser la vidéo originale en des formats plus léger (240p et 360p)
            - Langldent : dédié à la détection de la langue utilisé dans la vidéo
            - Subtile : utilisé pour l'extraction des paroles de la vidéo et leur transformation en métadonnées
        -Animal Detect : utilisé pour détecter la nature des animaux présents dans la vidéo.

•	Le deuxième module est à implémenter sur un serveur AWS :
            - Load Balancer pour équilibrer les charges
            - Amazon EC2 : constitué des machines virtuelles qui reçoivent les vidéos et les métadonnées enregistrées dans une base de données. Ensuite d'implémenter une interface qui permettra de visualiser ces vidéos dans leurs différents formats ainsi que les métadonnées y afférentes.
2.	Prérequis


•	Liste des outils ou dépendances nécessaires pour exécuter le code.

 -  installer docker compose et docker
 -  Python 3.9
 - Bibliothèques Python :
	moviepy
	speech_recognition
	langdetect

Tous définis dans le docker files.

•	Dépendance

-	ffmpeg

3. Installation et exécution

a.	Clonez le dépôt
 
Ouvrir un dossier dans lequel l’on veut cloner le projet, ouvrir le terminal et exécuter la commande suivante : git clone https://github.com/meganeanderline/video_p. Un fois le projet cloné

b.	Exécuter

Se positionner dans le fichier vidéo_p et taper la commande ‘docker compose up’ dans le terminal. Cette commande exécute deux instructions : docker build et docker run.
•	docker build qui recherche si l’image n’est pas installé en locale si non elle la crée à partir du docker hub avec toutes ses dépendances d’après les spécificités contenues dans le docker file.
•	Docker run qui est chargé de l’exécution.

4. Structure des fichiers/dossiers

Création du répertoire data contenant :
- Un répertoire pour la sauvegarde de la langue détecté dans la vidéo.
-  Un répertoire pour la sauvegarde du sous titrage sur 30 secondes de ce qui est dit dans la vidéo.
- la vidéo compressée sur ces deux formats.


           LIMITES

Notre solution a plusieurs limites par rapport aux exigences initiales, notamment :

	absence du module Animal detect.
	impossibilité du transfert de la vidéo et tes métadonnées sur le serveur AWS ainsi que la mise à disposition pour d’éventuelles consultations par un internaute.

         DIFFICULTÉS

Nous avons rencontré plusieurs difficultés parmi lesquels :
	la mise en œuvre du module animal detect, car la bibliothèque Torch qui permet d’utiliser les modèles assez lourds comme ssd300_vgg16  ne détectait pas avec précision les animaux présents sur la vidéo.
	l’utilisation du cloud AWS, la configuration des services EC2 et le service de la base de données.

