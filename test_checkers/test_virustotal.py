import os
from dotenv import load_dotenv
load_dotenv()

from checkers import vt_check as virustotal

if __name__ == "__main__":
    ip = "82.25.110.208"
    result = virustotal.check(ip)
    print("VirusTotal result:", result)
