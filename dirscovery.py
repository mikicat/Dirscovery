from termcolor import colored
import requests
import sys

def help():
    print("python3 dirscovery.py [url] [wordlist] [extensions type: .php,.html,.txt]")

try:
    url = sys.argv[1]
    path = sys.argv[2]
except:
    help()
    exit()
try:
    extensions = sys.argv[3]
    extensions = extensions.split(',')
except:
    extensions = "/"

print()
print(colored("  ____  _  ____  ____  ____  ____  _  _  _____ ____ ___  _", "red"))
print(colored(" /  _ \/ \/  __\/ ___\/   _\/  _ \/ \ |\/  __//  __\\\  \//", "red"))
print(colored(" | | \|| ||  \/||    \|  /  | / \|| | //|  \  |  \/| \  / ", "red"))
print(colored(" | |_/|| ||    /\___ ||  \__| \_/|| \// |  /_ |    / / /  ", "red"))
print(colored(" \____/\_/\_/\_\\\____/\____/\____/\__/  \____\\\_/\_\/_/   ", "red"))
print()
print(colored("[--]", "yellow"), colored("         \'A Simple Directory Discoverer\'         ", "blue"), colored("[--]", "yellow"))
print(colored("[--]", "yellow") + colored("             Created by:", "blue") + colored(" Mike & Marti         ", "green") + colored("   ", "blue") + colored("  [--]", "yellow"))
print(colored("                       Version ", "blue") + colored(" 0.2", "green"))
print()

print("Host:", url)
print("Wordlist:", path)

if extensions != '':
    print("Extensions:", extensions)

print("\nStarting...\n")

try:
    with open(path, "r") as f:
        matches = 0
        lines = f.readlines()
        r = requests.get(url)
        if (r.status_code) != 200:
            print("\nCannot connect to webpage.")
            print("Quitting...")
        else:
            for line in lines:
                line = line.lstrip().rstrip()
                full_url = [url, line]
                if url.endswith('/') or line.startswith('/'):
                    full_url = ''.join(full_url)
                else:
                    full_url = '/'.join(full_url)
                without_ext = full_url

                for i in range(0, len(extensions)):
                    full_url = without_ext
                    full_url = full_url + extensions[i]

                    req = requests.get(full_url)
                    if (req.status_code) == 200:
                        matches = matches + 1
                        print("Match Found: " + full_url)
                    else:
                        pass
    print("Total matches:", matches)
except KeyboardInterrupt:
    print("\nExiting...")
    exit(1)
except FileNotFoundError:
    print("Wordlist file not found")
    exit(1)
except:
    pass
