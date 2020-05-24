# Insta Web Scrapper
Welcome to the EmailInstaCheck project.

If you like my work and want to support it the best way is by adding a star to this project (top of the page) :)

## Docker installation
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
- Download this project with de Clone or Download button on the right top.

- Unzip the folder, start a terminal window from this folder and build the Docker image by entering the following command: 
```bash
docker build -t mail_scrapper .
```
- Once the build is finished, run it with this command:
```bash
docker run -it -w /usr/workspace -v $(pwd):/usr/workspace mail_scrapper
```

## Contributing
Any bugs you find please consider sending them.

## Used libraries
- [Selenium](https://pypi.org/project/selenium/)
- [Pandas](https://pypi.org/project/pandas/)
