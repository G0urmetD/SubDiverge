import socket
import requests
import random
import datetime

from tabulate import tabulate
from colorama import Fore, Style

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/88.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/87.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.37 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/90.0.818.62 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/88.0.705.81 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/87.0.664.75 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
]

def get_formatted_datetime():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S %m/%y")

def format_status(status_code):
    if status_code == 200:
        return f"{Fore.GREEN}{status_code}{Style.RESET_ALL}"
    elif status_code in [403, 404]:
        return f"{Fore.RED}{status_code}{Style.RESET_ALL}"
    else:
        return f"{Fore.YELLOW}Unknown{Style.RESET_ALL}"

def probe_subdomains(subdomains, timeout):
    table_data_http = []
    table_data_https = []

    for domain in subdomains:
        try:
            domain = domain.strip()
            http_url = "http://" + domain
            https_url = "https://" + domain

            # HTTP Probe
            resp_http = requests.get(http_url, headers={'User-Agent': random.choice(USER_AGENTS)}, timeout=timeout)
            http_status_code = resp_http.status_code
            http_ip = socket.gethostbyname(domain)

            formatted_http_status = format_status(http_status_code)
            http_row = [get_formatted_datetime(), formatted_http_status, f"{Fore.YELLOW}{http_url}{Style.RESET_ALL}", http_ip]
            table_data_http.append(http_row)

            # HTTPS Probe
            resp_https = requests.get(https_url, headers={'User-Agent': random.choice(USER_AGENTS)}, timeout=timeout)
            https_status_code = resp_https.status_code
            https_ip = socket.gethostbyname(domain)

            formatted_https_status = format_status(https_status_code)
            https_row = [get_formatted_datetime(), formatted_https_status, f"{Fore.YELLOW}{https_url}{Style.RESET_ALL}", https_ip]
            table_data_https.append(https_row)

        except Exception as e:
            http_row = [get_formatted_datetime(), f"{Fore.RED}Unkown{Style.RESET_ALL}", f"{Fore.RED}{http_url}{Style.RESET_ALL}", ""]
            table_data_http.append(http_row)
            https_row = [get_formatted_datetime(), f"{Fore.RED}Unkown{Style.RESET_ALL}", f"{Fore.RED}{https_url}{Style.RESET_ALL}", ""]
            table_data_https.append(https_row)

    headers = [f"{Fore.MAGENTA}Time{Style.RESET_ALL}", f"{Fore.MAGENTA}Status{Style.RESET_ALL}", f"{Fore.MAGENTA}URL{Style.RESET_ALL}", f"{Fore.MAGENTA}IP Address{Style.RESET_ALL}"]
    table_http = tabulate(table_data_http, headers=headers, tablefmt="rounded_outline")
    table_https = tabulate(table_data_https, headers=headers, tablefmt="rounded_outline")

    return table_http, table_https
