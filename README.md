# Insta Web Scrapper
Welcome to the EmailInstaCheck project.

If you like my work and want to support it the best way is by adding a star to this project (top of the page) :)

## Installation
- If you haven’t already downloaded the installer (Docker Desktop Installer.exe), you can get it from [Docker Hub](https://hub.docker.com/editions/community/docker-ce-desktop-windows/).. It typically downloads to your Downloads folder, or you can run it from the recent downloads bar at the bottom of your web browser.

- When prompted, ensure the Enable Hyper-V Windows Features option is selected on the Configuration page.

- Follow the instructions on the installation wizard to authorize the installer and proceed with the install.

- When the installation is successful, click Close to complete the installation process.

- Start Docker by cliking on the icon. When the whale icon in the status bar stays steady, Docker Desktop is up-and-running, and is accessible from any terminal window.

- To check that the install has been made correctly, open the terminal by using <kbd>⌘R</kbd> and enter:
```bash
docker --version
```

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

## Used libraries
- [Selenium](https://pypi.org/project/selenium/)
- [Pandas](https://pypi.org/project/pandas/)
