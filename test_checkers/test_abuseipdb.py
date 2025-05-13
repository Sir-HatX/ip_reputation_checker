import os
from dotenv import load_dotenv
load_dotenv()

from checkers import abuseipdb

if __name__ == "__main__":
    ip = "82.25.110.208"
    result = abuseipdb.check(ip)
    print("AbuseIPDB result:", result)

