import os
from dotenv import load_dotenv
load_dotenv()

from checkers import ipqualityscore

if __name__ == "__main__":
    ip = "82.25.110.208"
    result = ipqualityscore.check(ip)
    print("IPQualityScore result:", result)

