import os
import requests
from datetime import datetime

# List of subdomains to check
subdomains = [
    "http://blog.awesomeweb",
    "http://shop.awesomeweb",
    "http://main.awesomeweb"
]

# Log file path
log_file = "/var/www/awesomeweb/my_cron.log"

def check_subdomains():
    with open(log_file, "a") as log:
        for subdomain in subdomains:
            try:
                response = requests.get(subdomain)
                status = "UP" if response.status_code == 200 else f"DOWN (Status: {response.status_code})"
            except requests.ConnectionError:
                status = "DOWN (Connection Error)"
            
            log_entry = f"{datetime.now()} - {subdomain} is {status}\n"
            log.write(log_entry)
            print(log_entry)

if __name__ == "__main__":
    check_subdomains()

