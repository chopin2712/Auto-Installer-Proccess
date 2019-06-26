# Install deb files
sudo apt upgrade
sudo apt update

sudo dpkg -i *.deb
sudo apt -f -y install
sudo rm *.deb

# Install AppImages as root
sudo chmod +x *.AppImage
sudo ./*.AppImage

# Install AppImages as user
chmod +x *.AppImage
./*.AppImage
sudo rm *.AppImage

# Install sh files LAST
chmod +x *.sh
sudo sh *.sh
sudo rm *.sh
