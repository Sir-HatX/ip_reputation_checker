from dotenv import load_dotenv
from tabulate import tabulate
from checkers import abuseipdb, vt_check, ipqualityscore, greynoise, alienvault

# Load .env variables
load_dotenv()

# Load IPs from file
def load_ips(file_path="ips.txt"):
    try:
        with open(file_path, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: '{file_path}' not found.")
        return []

def main():
    IP_LIST = load_ips()
    if not IP_LIST:
        print("No IPs found in ips.txt")
        return

    services = {
        "AbuseIPDB": abuseipdb.check,
        "VirusTotal": vt_check.check,
        "IPQualityScore": ipqualityscore.check,
    #    "GreyNoise": greynoise.check,
    #    "AlienVault": alienvault.check
    }

    # Build table data with services as rows
    table = []
    for service_name, check_fn in services.items():
        row = [service_name]
        for ip in IP_LIST:
            row.append(check_fn(ip))
        table.append(row)

    # Build headers with IPs
    headers = ["Service"] + IP_LIST
    print(tabulate(table, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    main()
