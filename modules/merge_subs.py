from colorama import Fore, Style

def merge_subdomains(file1, file2, final_file):
    print(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Merging subdomain files and create a final subs-final.txt file.")
    
    # open the files and read the content
    with open(file1, "r") as f1, open(file2, "r") as f2:
        subdomains1 = set(f1.read().splitlines())
        subdomains2 = set(f2.read().splitlines())

    # merge both sets and remove doubles
    merged_subdomains = subdomains1.union(subdomains2)

    # write merged subdomains into final file
    with open(final_file, "w") as final:
        for subdomain in merged_subdomains:
            final.write(subdomain + "\n")