# Insta Web Scrapper
Welcome to the EmailInstaCheck project.

If you like my work and want to support it the best way is by adding a star to this project (top of the page) or you can donate here :)
[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://paypal.me/basiler75)

docker build -t webscrapper_data .
basileroth$ docker run -it -p 8888:8888 webscrapper


## Installation
Téléchargez la dernière version de python [à partir d'ici](https://www.python.org/downloads/).

Téléchargez l'image virtuelle de Chrome que on va utiliser [à partir de ce lien](http://chromedriver.storage.googleapis.com/index.html?path=81.0.4044.69/). Attention : il faut que la version téléchargée soit la même que ta version actuelle de Google Chrome, à trouver dans les paramètres de Chrome.
Dézipper le fichier et le déposer dans le dossier du projet.

## Windows
Ouvrez le terminal en utilisant <kbd>⌘R</kbd> et rentrez:
```bash
cmd
```
Après que la console se soit ouverte, tapez 
```bash
pip3 install openpyxl pandas xlrd selenium
```
ou 
```bash
pip install openpyxl pandas xlrd selenium
```
pour installer les librairies nécessaires.

## Usage
Le fichier main.py, accessible dans le dossier /src contient les variables d'environement à modifier.
```python
file_path = nom du fichier à traiter
chromedriver_path = où est enregistré chromdriver.exe
name_column_mail = nom de la colonne des mails
name_column_status = nom de la colonne du statut
```
Lancer main.py et le résultat sera sauvegardé dans le fichier liste_mail_output.xlsx dans le dossier /output.

## Contributing
Any bugs you find please consider sending them.

## Required libraries
- [Selenium](https://pypi.org/project/selenium/)
- [Pandas](https://pypi.org/project/pandas/)
