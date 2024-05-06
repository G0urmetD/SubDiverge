import subprocess
from colorama import Fore, Style

# checks if subfinder is installed
def check_subfinder():
    try:
        # checks subfinder version
        print(f"{Fore.GREEN}[DONE]{Style.RESET_ALL} Subfinder already installed.")
        subprocess.run(["subfinder", "--version"], check=True)
        
        # updating subfinder
        print(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Updating subfinder.")
        subprocess.run(["subfinder", "--update"], check=True)
    except subprocess.CalledProcessError:
        print(f"{Fore.YELLOW}[WARN]{Style.RESET_ALL} Subfinder not found.")
        
        # installing subfinder
        print(f"{Fore.CYAN}[Install]{Style.RESET_ALL} Installing subfinder for you...")
        subprocess.run(["GO111MODULE=on go get -u github.com/projectdiscovery/subfinder/v2/cmd/subfinder"], shell=True)
        print(f"{Fore.GREEN}[DONE]{Style.RESET_ALL} Subfinder installed successfully.")
        
        # updating subfinder
        print(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Updating subfinder.")
        subprocess.run(["subfinder", "--update"], check=True)

def run_subfinder(domain):
    print(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Searching Subdomains with subfinder ...")
    cmd = "subfinder -d {} | sort -u".format(domain)
    try:
        # Capture the output of subfinder
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        # Write the output to a text file
        with open("subs-subfinder.txt", "w") as file:
            file.write(result.stdout)
        # Print the output to the console
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} An error occurred: {e}")