import subprocess
from colorama import Fore, Style

# checks if assetfinder is installed
def check_assetfinder():
    try:
        # installing assetfinder
        print(f"{Fore.CYAN}[Install]{Style.RESET_ALL} Installing assetfinder for you...")
        subprocess.run(["sudo apt install -qq assetfinder -y > /dev/null"], shell=True)
        print(f"{Fore.GREEN}[DONE]{Style.RESET_ALL} assetfinder installed successfully.")
    except:
        print(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Assetfinder may already installed or something went wrong.")

def run_assetfinder(domain):
    print(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Searching Subdomains with assetfinder ...")
    cmd = "assetfinder {} | sort -u".format(domain)
    try:
        # Capture the output of assetfinder
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        # Write the output to a text file
        with open("subs-assetfinder.txt", "w") as file:
            file.write(result.stdout)
        # Print the output to the console
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} An error occurred: {e}")