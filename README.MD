# DeportedCommentary
Est un programme de commentaire centralisé décentralisé :3

En gros c'est un programme un peu dans l'idée de Isso (python), hashover (PHP), Juvia (Ruby?) et probablement d'autres.
Discourse et Vanilla Forum permettent d'être utilisé comme système de commentaire par exemple.

Ces programmes existent pour faire concurrence à Disqus
afin de pouvoir avoir un système de commentaire "simple" en rassemblant la gestions de ses commentaires venant de plusieurs sites sur un seul. ça permet d'avoir la main sur son propre service plutôt que de devoir faire une confiance aveugle en une entreprise qui est la pour ce faire des sous, et pour ça elle vends votre vie privé.

Ce genre de système permet par exemple d'avoir des commentaires sur des sites statique, ou sur des sites ou un système de commentaire n'est pas présent ou ne vous convenant pas.

# Pourquoi avoir fait ma propre alternative en Python sachant que Isso existe déjà ?
J'aime coder, j'ai commencé à apprendre le python assez récemment, et je rien n'est plus formateur pour apprendre un nouveau langage de ce lancer dans des choses un peu complexe des le début pour apprendre sur le tas.

De plus créer mon propre programme me permet d'en faire ce que je veux, et le rendre modulable plus facilement pour mes besoins (il est bien plus simple de comprendre un programme qu'on a fait sois même.

# Prérequis
 - Python 3.5 >=
 - pip
 - virtualenv (pip install virtualenv)
 - avoir un site sur lequel intégrer le programme :3
 - le reste pip s'en occupera

# Installation
```
git clone 'https://github.com/purexo/DeportedCommentary.git'
cd DeportedCommentary
virtualenv ENV
source ENV/bin/activate
pip install -r requirements.txt
cp config.example.json config.json
```

# Configuration
 - éditez le fichier config.json

## Explication du fichier de config
 - host : choisissez l'adresse ip ou DNS sur lequel est lancé votre programme (default = "localhost")
 - port : le port sur lequel ce lance votre programme (default = 8080)
 - sitename : nom de votre site (utilisé pour la page d’accueil) assez optionnel
 - pageadmin : chemin d'acces à l'interface d'administration / elle n'est pas encore mise en place.
 - theme : nom de votre thème (dans le dossier view) (default=default ; c'est un thème material design, assez sobre)
 - Allow-Origin : tableau de valeur. s'ajoutera aux headers de vos pages
   - Access-Control-Allow-Origin: valeur une
   - Access-Control-Allow-Origin: valeur 2
   - ça permet d'autoriser les requêtes ajax venant de toutes(*) adresses extérieurs, ou seulement quelques unes, vous pouvez vouloir que votre site ne soit accessible que de vos adresses et pas par tout le monde, c'est votre choix.
 - akismet-key : votre clé akismet, sinon l'antispam ne fonctionnera pas
 
## Explication du theme
  - Copiez collez les dossier (theme) default des dossiers view et static
  - Choisissez un nom pour la copie, les noms doivent correspondre
  - /!\ le path dans l'url ferra correspondre '/static/votrefichier' au chemin 'static/votretheme/votrefichier'
  - personnalisez le
  - éditez le fichier de config pour le faire correspondre à votre theme (juste le nom du dossier, pas de chemin.)
  
[More details here](Documentation/Theming/README.MD).
 
# Lancement (test only)
```python(3?) main.py```

# Deployement
 - in [Apache](Documentation/Deployement/Apache/README.MD)
 - in [Nginx](Documentation/Deployement/Nginx/README.MD)

## Intégration
vous récupererez le code en vous connectant à la page d'acceuil de votre programme python via l'exterieur.

exemple : http(s)://votre.domaine:votreport/ cela ressemblera à    

	<div id="DPCommentary"></div>
	<script type="text/javascript" src="http://localhost:8080/integrate"></script>
	
Mais il ne faut pas que ce soit en localhost

# NotaBene
Une limitation du protocole XmlHttpRequest fait qu'il est impossible de récupérer le contenue d'une adresse avec un protocole différent

Si vous remarquez que le theme par défaut fait des requetes vers l'exterieur de votre programme c'est que j'ai oublié d'importer localement les assets, merci de me le signaler. après si vous voulez utiliser votre propre thème avec CDN c'est votre choix :3

# Librairie et ressources utilisé
 - [bottle](http://bottlepy.org/docs/dev/index.html) (c'est le serveur web)
 - [peewee](http://docs.peewee-orm.com/en/latest/index.html) ORM pour SQL
 - [SQLite](https://www.sqlite.org/) ça me semble suffisant pour gerer une base de commentaires
 - [validate_email](https://pypi.python.org/pypi/validate_email) pour valider les email fournie. Le champ est optionel donc pas de raison de mal le remplir
 - lib python standard (nottament urllib.parse et json)
 - [akismet python](https://pypi.python.org/pypi/akismet/0.2.0) passé à la moulitte de 2to3 et quelques modification d'encodage, va faloir que je lui propose au mec qui a fait la lib
 - [Awesome Font](https://fortawesome.github.io/Font-Awesome/) pour mon thème material, j'ai un peu honte, toute une police pour faire juste l'icone d'envois de commentaire :3
 - [Roboto Font](https://www.google.com/fonts/specimen/Roboto)
 - [Material Design](https://www.google.com/design/spec/material-design/introduction.html) de moi, librement inspiré des specifications de google

# Remerciements
 - [Geluchat](https://www.dailysecurity.fr/) pour m'avoir motiver à me lancer dans le python
 - [Sam et max](http://sametmax.com/) le 3/4 de ce que je connais en python c'est grâce à leur site, et j'ai choisi mes libs avec [cet article](http://sametmax.com/sept-petites-libs-qui-changent-la-vie-dun-dev-python/)
 
# Feature future
 - [ ] captcha (optionel)
 - [ ] panel admin (mdp hashé dans le fichier de config)
 - [ ] choix entre ReStructuredText et Markdown, par commentaire (BDD broken)
 - [ ] fil RSS
 - [ ] Authentification user optionelle (BDD broken)
 - [ ] Mail -> Admin (new commentaire), Mail -> user (dans son fil)
