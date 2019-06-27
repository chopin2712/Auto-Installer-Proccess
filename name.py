import os

# Priority

# Package Name
name = input("PACKAGE NAME: ")

# APTITUDE
file = open("package.txt", "a")
file.write("sudo apt -y install ")
file.write(name)
file.close()
file = open("package.txt", "r")
os.system(file.read())
file.close()
os.system("sudo rm package.txt")

# Tag finder
tag = input("Would you like a special tag? for snap [Y, ] ")
if tag == "Y" or tag == "y":
    tag = input("What tag would you like (starting by --) > ")

# SNAP
file = open("package.txt", "a")
file.write("sudo snap install ")
file.write(name)
file.write(" ")
file.write(tag)
file.close()
file = open("package.txt", "r")
os.system(file.read())
file.close()
os.system("sudo rm package.txt")

# Anti-flatpak
exit
# FLATPAK (DO NOT USE)
file = open("package.txt", "a")
file.write("sudo flatpak search ")
file.write(name)
file.close()
file = open("package.txt", "r")
os.system(file.read())
file.close()
os.system("sudo rm package.txt")

file = open("package.txt", "a")
file.write("sudo flatpak install ")
file.write(name)
file.close()
file = open("package.txt", "r")
os.system(file.read())
file.close()
os.system("sudo rm package.txt")

file = open("package.txt", "a")
file.write("sudo flatpak run ")
file.write(name)
file.close()
file = open("package.txt", "r")
os.system(file.read())
file.close()
os.system("sudo rm package.txt")
