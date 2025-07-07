from dotenv import load_dotenv
from checkers import abuseipdb, vt_checker, ipqualityscore
import os

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

# Format IPQualityScore results nicely
def format_ipqualityscore(result):
    lines = []
    keys = [
        "Fraud Score", "VPN", "Proxy", "Tor", "Bot", "Abuse",
        "ISP", "Org", "Loc", "Host", "ASN"
    ]
    for key in keys:
        if key in result:
            lines.append(f"{key}: {result[key]}")
    return "\n".join(lines)

def main():
    IP_LIST = load_ips()
    if not IP_LIST:
        print("No IPs found in ips.txt")
        return

    services = {
        "AbuseIPDB": abuseipdb.check,
        "VirusTotal": vt_checker.check,
        "IPQualityScore": ipqualityscore.check,
    }

    output_lines = []

    for ip in IP_LIST:
        output_lines.append("#" * 50)
        output_lines.append(f"IP {ip}")
        output_lines.append("-" * 50)

        for service_name, check_fn in services.items():
            result = check_fn(ip)

            if service_name == "IPQualityScore":
                # Assume result is a dict or string that can be parsed
                if isinstance(result, dict):
                    formatted = format_ipqualityscore(result)
                else:
                    formatted = result  # fallback
                output_lines.append(f"{service_name}:\n{formatted}")
            else:
                output_lines.append(f"{service_name}: {result}")

        output_lines.append("#" * 50 + "\n")

        # Print a short status to the terminal
        print(f"Status: Checked {ip} - See full report in output.txt")

    # Save results to output.txt
    with open("output.txt", "w") as f:
        f.write("\n".join(output_lines))

if __name__ == "__main__":
    main()

