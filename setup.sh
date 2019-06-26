# Dependencies
sudo apt install python3.7
sudo apt install wine
sudo apt install git
sudo apt install snap

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
