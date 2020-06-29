import os
import sys
import platform
import shutil

if not platform.system() == "Linux":
    sys.exit("Just GNU/Linux .")

try:
    os.system("chmod +x betikfetch.py")
    shutil.copy("betikfetch.py","/usr/bin/betikfetch")
except PermissionError:
    sys.exit("PermissionError ! Please try with 'sudo' ...")

if os.path.exists("/usr/bin/betikfetch"):
    print("Success ! Tryingin add ..rc")

shell = os.environ["SHELL"]
if shell == "/bin/bash":
    with open("/home/{}/.bashrc".format(os.getlogin()),"a") as yaz:
        yaz.write("\nbetikfetch\n")
elif shell == "/usr/bin/fish":
    with open("/home/{}/.config/omf/init.config".format(os.getlogin()),"a") as yaz:
        yaz.write("\nbetikfetch\n")
elif shell == "/usr/bin/zsh":
    with open("/home/{}/.zshrc".format(os.getlogin()),"a") as yaz:
        yaz.write("\nbetikfetch\n")
else:
    sys.exit("What is your shell ?")

print("Success . ReOpen your shell .")