import time
import argparse

from colorama import Fore, Style

from modules.subfinder import check_subfinder, run_subfinder
from modules.assetfinder import check_assetfinder, run_assetfinder
from modules.merge_subs import merge_subdomains
from modules.http_probe import probe_subdomains

def read_subdomains_from_file(file_path):
    with open(file_path, "r") as file:
        subdomains = file.readlines()
    return [subdomain.strip() for subdomain in subdomains]

def main():
    banner = """

      _____       _    ______ _                          
     /  ___|     | |   |  _  (_)                         
     \ `--. _   _| |__ | | | |___   _____ _ __ __ _  ___ 
    `--. \ | | | '_ \| | | | \ \ / / _ \ '__/ _` |/ _  |
    /\__/ / |_| | |_) \| |/ /| |\ V /  __/ | | (_||  __/
    \____/ \__,_|_.__/|___/ |_| \_/ \___|_|  \__, |\___|
                                            __/ |     
                                            |___/      


    """
    print(Fore.CYAN + banner + Style.RESET_ALL)
    print(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Author: G0urmetD (403 - Forbidden)")
    print(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Version: 3.1")

    # script arguments/parameters
    parser = argparse.ArgumentParser(description='Scan for subdomains and probe HTTP status codes.')
    parser.add_argument('-d', '--domain', dest='domain', required=True, help='Domain to scan')
    args = parser.parse_args()
    domain = args.domain

    # start tool timer
    start_time = time.time()
    
    # call subfinder install check function
    print(f"=============================== {Fore.CYAN}[CHECK]{Style.RESET_ALL} ===============================")
    # Check and install Subfinder
    print(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Checking subfinder on the system")
    check_subfinder()

    # Check and install Assetfinder
    print(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Checking assetfinder on the system")
    check_assetfinder()

    print(f"=============================== {Fore.CYAN}[END]{Style.RESET_ALL} ===============================")

    # starting subdomain enumeration
    print(f"=============================== {Fore.CYAN}[SUBDOMAINS]{Style.RESET_ALL} ===============================")
    print("\n")
    print(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Scanning for subdomains...")
    time.sleep(2)

    # call subfinder logic module
    run_subfinder(domain)

    # call assetfinder function
    run_assetfinder(domain)

    # compare subdomain findings
    # save compared subdomains in final .txt file
    merge_subdomains("subs-subfinder.txt", "subs-assetfinder.txt", "subs-final.txt")

    print(f"=============================== {Fore.CYAN}[END]{Style.RESET_ALL} ===============================")
    print(f"=============================== {Fore.CYAN}[HTTP/HTTPS PROBE]{Style.RESET_ALL} ===============================")
    # loop through compared subdomain findings and run http/https probe & print out
    # save accessible subdomains in .txt file
    all_subdomains = read_subdomains_from_file("subs-final.txt")
    print(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} I'm working on it, grab a coffee ...")
    table_http, table_https = probe_subdomains(all_subdomains)
    print(f"{Fore.MAGENTA}HTTP Probe:{Style.RESET_ALL}")
    print(table_http)
    print(f"\n{Fore.MAGENTA}HTTPS Probe:{Style.RESET_ALL}")
    print(table_https)

    # end tool timer & print out
    end_time = time.time()
    scan_time = end_time - start_time
    print("")
    print(f'{Fore.YELLOW}Scan completed in {scan_time:.2f} seconds.{Style.RESET_ALL}')

if __name__ == "__main__":
    main()
