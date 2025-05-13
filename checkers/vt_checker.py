import os
import requests
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("VIRUSTOTAL_API_KEY")

def check(ip):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {'x-apikey': API_KEY}
    try:
        response = requests.get(url, headers=headers)
        stats = response.json()["data"]["attributes"]["last_analysis_stats"]
        return f"Malicious: {stats['malicious']}, Suspicious: {stats['suspicious']}"
    except:
        return "Error"