import fnmatch
import os

m = os.system("ls")

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.deb'):
        os.system("sudo dpkg -i *.deb")
        os.system("sudo apt -f -y install")
        os.system("sudo rm *.deb")
    elif fnmatch.fnmatch(file, '*.AppImage'):
        os.system("sudo chmod +x *.AppImage")
        os.system("sudo ./*.AppImage")
        os.system("./*.AppImage")
        os.system("sudo rm *.AppImage")
    elif fnmatch.fnmatch(file, '*.sh'):
        os.system("chmod +x *.sh")
        os.system("sudo sh *.sh")
        os.system("sudo rm *.sh")
    elif fnmatch.fnmatch(file, '*.flatpakref'):
        os.system("flatpak update -v")
        os.system("sudo flatpak install *.flatpakref")
        os.system("sudo flatpak run *.flatpakref")
    # wine
os.system("sudo rm main.py")
