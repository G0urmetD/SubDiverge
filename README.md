# SubDiverge

## Description
Another subdomain tool with HTTP/HTTPS probe. The Tool is designed to find subdomains with subfinder (fast), assetfinder and probe the subdomains with HTTP and HTTPS. Everything will printed out nicely formatted and colorized.

## Help
```bash
                                                                                                                      
      _____       _    ______ _                                                                                       
     /  ___|     | |   |  _  (_)                                                                                      
     \ `--. _   _| |__ | | | |___   _____ _ __ __ _  ___                                                              
      `--. \ | | | '_ \| | | | \ \ / / _ \ '__/ _` |/ _  |                                                            
    /\__/ / |_| | |_) \| |/ /| |\ V /  __/ | | (_||  __/                                                              
    \____/ \__,_|_.__/|___/ |_| \_/ \___|_|  \__, |\___|                                                              
                                            __/ |                                                                     
                                            |___/                                                                     
                                                                                                                                                                                                                        
[INFO] Author: G0urmetD (G0urmet)
[INFO] Version: 3.7.1
usage: subDiverge.py [-h] -d DOMAIN [-s] [-p] [-t TIMEOUT]

Scan for subdomains and probe HTTP status codes.

options:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        Domain to scan
  -s, --subs            Run Subdomain enumeration.
  -p, --probe           Enable HTTP probe
  -t TIMEOUT, --timeout TIMEOUT
                        Timeout for HTTP probe
```

## Known Issues
- Missing subfinder
```bash
sudo apt install subfinder -y
```
