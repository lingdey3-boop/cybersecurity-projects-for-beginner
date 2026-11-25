#created your own log file for log anlyger
import re
from collections import Counter
import requests
from urllib.parse import urlparse
import hashlib
def password_checker():
    i = input("ENTER YOUR PASSWORD: ")
    valid = True

    if len(i) <= 8:
        print("PASSWORD MUST BE MORE THAN 8 CHARACTERS LONG")
        valid = False

    if not re.search(r"[a-z]", i):
        print("PLEASE ENTER AT LEAST ONE LOWERCASE LETTER")
        valid = False

    if not re.search(r"[A-Z]", i):
        print("PLEASE ENTER AT LEAST ONE UPPERCASE LETTER")
        valid = False

    if not re.search(r"\d", i):
        print("ADD AT LEAST ONE NUMBER")
        valid = False

    if not re.search(r"[!@#$%&*]", i):
        print("ADD AT LEAST ONE SPECIAL CHARACTER")
        valid = False

    if valid:
        print("PASSWORD IS STRONG")
    else:
        print("PASSWORD IS WEAK")


def log_anylazer():
    failed_login = Counter()
    successful_login = Counter()
    ip_attempts = Counter()
    total_event = 0

    try:
        with open("ml", "r", encoding="utf-8") as file:
            for line in file:
                path = line.strip().split("|")
                if len(path) < 5:
                    continue

                total_event += 1

                status = path[3].strip()
                ip = path[2].strip().split("=", 1)[1]

                ip_attempts[ip] += 1

                if status == "STATUS=FAILED":
                    failed_login[ip] += 1
                elif status == "STATUS=SUCCESS":
                    successful_login[ip] += 1

    except FileNotFoundError:
        print("Log file 'mgt' not found.")
        return

    total_failed = sum(failed_login.values())
    total_successful = sum(successful_login.values())

    print("========== SECURITY LOG ANALYZER ==========")
    print(f"TOTAL EVENTS: {total_event}")
    print(f"TOTAL FAILED EVENTS: {total_failed}")
    print(f"TOTAL SUCCESSFUL EVENTS: {total_successful}")

    print("\n========== TOP 10 SUSPICIOUS IPs ==========")
    for ip, count in failed_login.most_common(10):
        print(f"{ip} -> {count} failed attempts")

    print("\n========== TOP 10 MOST ATTEMPTED IPs ==========")
    for ip, count in ip_attempts.most_common(10):
        print(f"{ip} -> {count} total attempts")


def https_security_header_checker():
    su = {
        "Strict-Transport-Security": "Helps enforce HTTPS",
        "Content-Security-Policy": "Controls which resources can load",
        "X-Content-Type-Options": "Helps prevent MIME-type sniffing",
        "X-Frame-Options": "Helps prevent websites from framing this page",
        "Referrer-Policy": "Controls referrer information",
        "Permissions-Policy": "Controls browser features"
    }

    url = input("ENTER YOUR URL: ").strip()
    if "://" not in url:
        url = "https://" + url

    pu = urlparse(url)
    if pu.scheme not in ("http", "https") or not pu.hostname:
        print("INVALID URL. ENTER A VALID HTTP OR HTTPS WEBSITE.")
        raise SystemExit

    try:
        response = requests.get(url, timeout=10, allow_redirects=True)
        headers = response.headers

        print("\n================ HTTPS SECURITY HEADER CHECKER ================")
        print("WEBSITE:", response.url)
        print("HTTPS STATUS CODE:", response.status_code)
        print(headers)

        present = 0
        missing = 0

        print("\n============== SECURITY HEADER REPORT ===============")
        for header, purpose in su.items():
            if header in headers:
                print(f"[PRESENT] {header}")
                present += 1
            else:
                print(f"[MISSING] {header}")
                missing += 1

        print("============ SUMMARY ============")
        print("HEADERS CHECKED:", len(su))
        print("HEADERS PRESENT:", present)
        print("HEADERS MISSING:", missing)

    except requests.exceptions.RequestException:
        print("COULD NOT CONNECT TO THE WEBSITE")

def file_hasher():
    file_path = input("Enter the file path: ").strip()
    hasher = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            while True:
                data = file.read(4096)
                if not data:
                    break
                hasher.update(data)

        digest = hasher.hexdigest()
        st=digest[:6]
        print("SHA-256:", st)
        return st

    except OSError as error:
        print("Error reading file:", error)
        return None
def Exit():
    print("GOODBEY")
    break
if __name__ == "__main__":
    while True:
        print("\n========== WELCOME TO THE SECURITY TOOLKIT ==========")
        print("1. PASSWORD STRENGTH CHECKER")
        print("2. LOG ANALYZER")
        print("3. HTTPS SECURITY HEADER CHECKER")
        print("4. FILE HASHER")
        print("5. EXIT")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            password_checker()
        elif choice == "2":
            log_analyzer()
        elif choice == "3":
            https_security_header_checker()
        elif choice == "4":
            file_hasher()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 5.")

# you can add more functionality or options here if you want changes are allowed
#MD
    
