# Dependencies
sudo apt install -y python3.7
sudo apt install -y wine
sudo apt install -y git
sudo apt install -y snap
sudo apt install -y java
sudo apt install -y openjdk-8-jre

sudo apt install -y flatpak
sudo apt install -y gnome-software-plugin-flatpak
sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

# Install
sudo mkdir /opt/aip
sudo cp * /opt/aip

# Commands
sudo cp /opt/aip/aip /usr/bin
sudo cp /opt/aip/aipn /usr/bin

# Get authorisations
sudo chmod 777 /usr/bin/aip
sudo chmod 777 /usr/bin/aipn

sudo chmod 777 -R /opt/aip
