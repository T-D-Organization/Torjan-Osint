
# Torjan-Osint Setup & Launcher
import os, sys, subprocess, json, time

try:
    import requests
except ImportError:
    subprocess.check_call([sys.executable,"-m","pip","install","requests"])
    import requests

__version__="0.1"
__github__="https://github.com/T-D-Organization/Torjan-Osint"

class Colors:
    RED='\033[91m';GREEN='\033[92m';YELLOW='\033[93m'
    BLUE='\033[94m';CYAN='\033[96m';END='\033[0m';BOLD='\033[1m'

def clear():
    os.system("cls" if os.name=="nt" else "clear")

def banner():
    clear() 

    print(f"""{Colors.RED}
============================================================
        Torjan-Osint Setup & Launcher v{__version__}
              Coded by @T-D-Organization
============================================================{Colors.END}""")

def check_version():
    try:
        r=requests.get("https://api.github.com/repos/T-D-Organization/Torjan-Osint/releases/latest",timeout=3)
        if r.status_code==200:
            latest=r.json().get("tag_name","").replace("v","")
            if latest:
                if tuple(map(int,latest.split(".")))>tuple(map(int,__version__.split("."))):
                    print(f"{Colors.YELLOW}Update available: v{latest}{Colors.END}")
    except:
        pass

def create_config():
    if not os.path.exists("config.json"):
        with open("config.json","w") as f:
            json.dump({"timeout":10,"theme":"dark","proxy":"","tor":False},f,indent=4)

def check_files():
    req=["Torjan-Osint.py","requirements.txt"]
    miss=[f for f in req if not os.path.isfile(f)]
    if miss:
        print("Missing:",", ".join(miss))
        return False
    print("All required files found.")
    return True

def install():
    subprocess.check_call([sys.executable,"-m","pip","install","--upgrade","pip"])
    subprocess.check_call([sys.executable,"-m","pip","install","-r","requirements.txt"])

def launch():
    subprocess.call([sys.executable,"Torjan-Osint.py"])

def main():
    create_config()
    while True:
        clear();check_version();banner()
        print("1.Install Requirements\n2.Launch\n3.Install & Launch\n4.Check Files\n5.Exit")
        c=input("> ").strip()
        if c=="1":
            if check_files(): install()
        elif c=="2":
            if check_files(): launch()
        elif c=="3":
            if check_files():
                install();launch()
        elif c=="4":
            check_files()
        elif c=="5":
            break
        input("Press Enter...")
if __name__=="__main__":
    main()
