green="\033[0;32m"        # Green
yellow="\033[0;33m"       # Yellow
on_ipurple="\033[10;95m"  # Purple
on_icyan="\033[0;106m"    # Cyan
on_iwhite="\033[0;107m"   # White
blue="\033[0;34m"         # Blue
red="\033[0;31m"          # Red
purple="\033[0;35m"       # Purple
cyan="\033[0;36m"         # Cyan
white="\033[0;37m"        # White
icyan="\033[0;96m"        # Cyan
on_icyan="\033[0;106m"    # Cyan

import os
import sys
import time

os.system("clear")

print(green+"""
Welcome to 
 ____  _   _ ____  _____ ____
/ ___|| | | |  _ \| ____|  _ \                    \___ \| | | | |_) |  _| | |_) |                    ___) | |_| |  __/| |___|  _ <
|____/ \___/|_|   |_____|_| \_\

 ____            _                                | __ )  __ _ ___(_) ___
|  _ \ / _` / __| |/ __|
| |_) | (_| \__ \ | (__
|____/ \__,_|___/_|\___|"""+blue+"""  v1.0"""+yellow+"""
 
Developer	: SUPER BIPAP Team
Github		: https://github.com/superbipap/
Facebook	: fb.com/superbipap
		  fb.com/groups/superbipap
Telegram	: t.me/superbipap
		  t.me/super_bipap
Website	  	: https://www.superbipap.com
""")

print(red+"""For Username and Password Contact on FB or TG
"""+purple+"""Enter Correct Username and Password""")

n=5
while n<10:
	username="SUPER"
	password="Basic"
	
	
	intusername=str(input('\n'+'\033[1;33m'+'Enter The Username: '+'\033[0m'))
	intpassword=str(input('\033[1;33m'+'Enter The Password: '+'\033[0m'))
	
	if username==intusername and password==intpassword:
		print('\033[1;32m','\nLogin sussecful [You Are Visit SUPER SMS Bomber ','\033[0m'+'(✔)')
		print('\n')
		os.system("clear")
		break
		
	else:
		print('\033[1;31m','\nYou Are Worng UserName OR Wrong Password ✘','\033[0m'+'')
		print('\n')
		os.system("python basic.py")

os.system("clear")

print(green+"Updating Package"+white)
time.sleep(2)
os.system("pkg update -y")
os.system("clear")

print(green+"Upgrading Package"+white)
time.sleep(2)
os.system("pkg upgrade -y -y -y")
os.system("clear")

print(green+"Installing git"+white)
time.sleep(2)
os.system("pkg install git -y")
os.system("clear")

print(green+"Installing python"+white)
time.sleep(2)
os.system("pkg install python -y")
os.system("clear")

print(green+"Installing python2"+white)
time.sleep(2)
os.system("pkg install python2 -y")
os.system("clear")

print(green+"Installing php"+white)
time.sleep(2)
os.system("pkg install php -y")
os.system("clear")

print(green+"Installing ruby"+white)
time.sleep(2)
os.system("pkg install ruby -y")
os.system("clear")

print(green+"Installing openssh"+white)
time.sleep(2)
os.system("pkg install openssh -y")
os.system("clear")

print(green+"Installing tree"+white)
time.sleep(2)
os.system("pkg install tree -y")
os.system("clear")

print(green+"Installing wget"+white)
time.sleep(2)
os.system("pkg install wget -y")
os.system("clear")

print(green+"Installing figlet"+white)
time.sleep(2)
os.system("pkg install figlet -y")
os.system("clear")

print(green+"Installing pip requests"+white)
time.sleep(2)
os.system("pip install requests -y")
os.system("clear")

print(green+"Installing pip2 requests"+white)
time.sleep(2)
os.system("pip2 install requests -y")
os.system("clear")

print(green+"Installing pip mechanize"+white)
time.sleep(2)
os.system("pip install mechanize -y")
os.system("clear")

print(green+"Installing pip2 mechanize"+white)
time.sleep(2)
os.system("pip2 install mechanize -y")
os.system("clear")

print(green+"Upgrading pip"+white)
time.sleep(2)
os.system("pip install --upgrade pip")
os.system("clear")

print(green+"Installing root-repo"+white)
time.sleep(2)
os.system("pkg install root-repo -y")
os.system("clear")

print(green+"Installing unstable-repo"+white)
time.sleep(2)
os.system("pkg install unstable-repo -y")
os.system("clear")

print(green+"Installing x11-repo"+white)
time.sleep(2)
os.system("pkg install x11-repo -y")
os.system("clear")

print(green+"Installing cmatrix"+white)
time.sleep(2)
os.system("pkg install cmatrix -y")
os.system("clear")

print(green+"       All package installed successfully")
print("")
print(blue+"Thanks for using our tools.")
print(purple+"We update regularly this tools. More package will be added soon.")
print(green+"Stay with #super_bipap_team")
print(green+"We work for Islam and Mankind"+white)
time.sleep(12)

os.system("python main.py")
