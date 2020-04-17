import requests
import argparse
import sys
import os
import urllib3


def console_clear():
    try:
        if sys.platform == "win32":
            os.system("cls")
        else:
            os.system("clear")
        
        return 0
    except Exception:
        print("could not clear console")
        return 1

console_clear()

def file_writer(filename, data):
    opnr = open(filename, "a+")
    opnr.write(data)
    opnr.close()

parse = argparse.ArgumentParser(description="Send request to a website using proxies to check if it's online How to: python proxyon.py proxies.txt https://www.google.com/")
parse.add_argument("proxy", type=str, help="Enter the list of proxies Example: proxies.txt")
parse.add_argument("web", type=str, help="Enter a website to send http requests using proxies.txt Example: https://www.google.com/")
args = parse.parse_args()


with open(args.proxy, "r") as opnr:
    for x in opnr:
        if x[0].strip().isdigit():
            try:
                req = requests.get(args.web, headers={"User-Agent":"Mozilla/5.0 CK={ } (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}, proxies={"https":x.strip(), "http":x.strip()})
                if req.status_code == 200:
                    file_writer("onlineProxies.txt", x)
                    print("\033[1;32m[+]Status code: {0} OK Proxy: {1}\033[1;m".format(req.status_code, x))
                else:
                    print("\033[1;35m[-]Status code: {0} Proxy: {1}\033[1;m".format(req.status_code, x))
            except Exception:
                print("\033[1;35m[-]Error: {0}\033[1;m".format(x))
                pass

        else:
            print("This Does not look like a proxy {0}".format(x))
