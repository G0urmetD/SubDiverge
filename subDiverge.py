import subprocess
import requests
import time
import socket
import argparse

from fake_useragent import UserAgent
from colorama import Fore, Style

banner = """

 _____       _    ______ _                          
/  ___|     | |   |  _  (_)                         
\ `--. _   _| |__ | | | |___   _____ _ __ __ _  ___ 
 `--. \ | | | '_ \| | | | \ \ / / _ \ '__/ _` |/ _  |
/\__/ / |_| | |_) \| |/ /| |\ V /  __/ | | (_| |  __/
\____/ \__,_|_.__/|___/ |_| \_/ \___|_|  \__, |\___|
                                          __/ |     
                                         |___/      


"""

print(Fore.CYAN + banner + Style.RESET_ALL)
print(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Author: G0urmetD (403 - Forbidden)")
print(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Version: 2.3.3")

# Function to install Subfinder if not already installed
def install_subfinder():
    try:
        subprocess.run(["subfinder", "--version"], check=True)
        print(f"{Fore.GREEN}[DONE]{Style.RESET_ALL} Subfinder already installed.")
    except subprocess.CalledProcessError:
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Subfinder not found.")
        print(f"{Fore.MAGENTA}[Install]{Style.RESET_ALL} Installing subfinder for you...")
        subprocess.run(["GO111MODULE=on go get -u github.com/projectdiscovery/subfinder/v2/cmd/subfinder"], shell=True)
        print(f"{Fore.GREEN}[DONE]{Style.RESET_ALL} Subfinder installed successfully.")

# Check and install Subfinder
print(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Checking subfinder on the system")
install_subfinder()

parser = argparse.ArgumentParser(description='Scan for subdomains and probe HTTP status codes.')
parser.add_argument('-d', '--domain', dest='domain', required=True, help='Domain to scan')
args = parser.parse_args()

domain = args.domain

def commands(cmd):
    try:
        subprocess.check_call(cmd, shell=True)
    except:
        pass
    
start_time = time.time()
print("\n")
print(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Scanning for subdomains...")
time.sleep(2)

print(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Searching Subdomains with subfinder")
cmd = "subfinder -d {} > subdomains.txt".format(domain)
commands(cmd)

print(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Probing Subdomains")

with open('subdomains.txt', 'r') as f:
    subdomains = f.readlines()

gooddomains_http = []
gooddomains_https = []

def ipadd(subdomain):
    if "http" in subdomain:
        subdomain = subdomain.replace("http://", "")
    if "https" in subdomain:
        subdomain = subdomain.replace("https://", "")
    return socket.gethostbyname(subdomain)

# probing subdomains with HTTP
print(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Probing Subdomains with HTTP")
for domain in subdomains:
    try:
        domain = domain.strip()
        http = "http://" + domain
        ua = UserAgent()
        header = {'User-Agent':str(ua.chrome)}     
        # Test HTTP for each subdomain
        resphttp = requests.get(http, headers=header, timeout=5)
        
        if resphttp.status_code == 200:
            print (Fore.GREEN + "[200] " + "{}: {}".format(http, ipadd(http)))
            gooddomains_http.append("[200] " + http + "\n")
        elif resphttp.status_code in [403, 404]:
            print (Fore.RED + "[403,404] " + "{}: {}".format(http, ipadd(http)))
            gooddomains_http.append("[403,404] " + http + "\n")
        else:
            print (Fore.YELLOW + "[{}] ".format(resphttp.status_code) + "{}: {}".format(http, ipadd(http)))
            gooddomains_http.append("[{}] ".format(resphttp.status_code) + http + "\n")
            
    except Exception as e:
        print(Fore.RED + "[Error] " + "{}".format(http))

# probing subdomains with HTTPS
print(f"\n{Fore.CYAN}[INFO]{Style.RESET_ALL} Probing Subdomains with HTTPS")
for domain in subdomains:
    try:
        domain = domain.strip()
        https = "https://" + domain
        ua = UserAgent()
        header = {'User-Agent':str(ua.chrome)}     
        # Test HTTPS for each subdomain
        resphttps = requests.get(https, headers=header, timeout=5)
        
        if resphttps.status_code == 200:
            print (Fore.GREEN + "[200] " + "{}: {}".format(https, ipadd(https)))
            gooddomains_https.append("[200] " + https + "\n")
        elif resphttps.status_code in [403, 404]:
            print (Fore.RED + "[403,404] " + "{}: {}".format(https, ipadd(https)))
            gooddomains_https.append("[403,404] " + https + "\n")
        else:
            print (Fore.YELLOW + "[{}] ".format(resphttps.status_code) + "{}: {}".format(https, ipadd(https)))
            gooddomains_https.append("[{}] ".format(resphttps.status_code) + https + "\n")
                
    except Exception as e:
        print(Fore.RED + "[Error] " + "{}".format(https))

with open("goodsubs_http.txt", "w") as g:
    g.writelines(gooddomains_http)

with open("goodsubs_https.txt", "w") as g:
    g.writelines(gooddomains_https)

end_time = time.time()
scan_time = end_time - start_time
print("")
print(f'{Fore.YELLOW}Scan completed in {scan_time:.2f} seconds.{Style.RESET_ALL}')
