import os
import requests
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("ABUSEIPDB_API_KEY")

def check(ip):
    try:
        url = "https://api.abuseipdb.com/api/v2/check"
        headers = {
            "Key": API_KEY,
            "Accept": "application/json"
        }
        params = {
            "ipAddress": ip,
            "maxAgeInDays": "90"
        }
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()["data"]

        score = data.get("abuseConfidenceScore", "N/A")
        is_tor = data.get("isTor", "N/A")
        total_reports = data.get("totalReports", "N/A")

        return f"Score: {score}, Tor: {is_tor}, Reports: {total_reports}"
    except Exception as e:
        return f"Error: {str(e)}"