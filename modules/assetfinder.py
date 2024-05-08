import subprocess
from colorama import Fore, Style

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
