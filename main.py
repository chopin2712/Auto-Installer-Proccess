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
        # os.system("sudo rm *.AppImage")
    elif fnmatch.fnmatch(file, '*.sh'):
        os.system("chmod +x *.sh")
        os.system("sudo sh *.sh")
        os.system("sudo rm *.sh")
    elif fnmatch.fnmatch(file, '*.jar'):
        os.system("sudo java -jar *.jar")
    elif fnmatch.fnmatch(file, '*.flatpakref0'): # DO NOT USE FLATPAK(added 0)
        os.system("flatpak update -v")
        os.system("sudo flatpak install *.flatpakref")
        os.system("sudo flatpak run *.flatpakref")
    elif fnmatch.fnmatch(file, '*.exe'): # Unstable
        os.system("chmod +x *.exe")
        os.system("sudo ./*.exe")
        os.system("./*.exe")
        os.system("wine *.exe")
os.system("sudo rm main.py")
