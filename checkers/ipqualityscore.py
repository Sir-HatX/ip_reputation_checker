import os
import requests
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("IPQUALITYSCORE_API_KEY")

def check(ip):
    url = f"https://ipqualityscore.com/api/json/ip/{API_KEY}/{ip}?fast=true"
    try:
        response = requests.get(url)
        data = response.json()

        fraud_score = data.get("fraud_score", "N/A")
        is_vpn = data.get("vpn", False)
        is_tor = data.get("tor", False)
        is_proxy = data.get("proxy", False)
        is_abuser = data.get("recent_abuse", False)
        is_bot = data.get("bot_status", False)
        hostname = data.get("host", "N/A")
        isp = data.get("ISP", "N/A")
        org = data.get("organization", "N/A")
        city = data.get("city", "N/A")
        region = data.get("region", "N/A")
        country = data.get("country_code", "N/A")
        ASN = data.get("ASN", "N/A")

        return (
            f"Fraud Score: {fraud_score}\n"
            f"VPN: {is_vpn}, Proxy: {is_proxy}, Tor: {is_tor}\n"
            f"Bot: {is_bot}, Abuse: {is_abuser}\n"
            f"ISP: {isp}, Org: {org}\n"
            f"Loc: {city}, {region}, {country}\n"
            f"Host: {hostname}, ASN: {ASN}"
        )
    except Exception as e:
        return f"Error: {e}"

