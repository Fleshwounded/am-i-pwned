#!/bin/env python

#   Author      :   Stavros Grigoriou
#   GitHub      :   https://github.com/unix121
#   Date        :   25 September 2017
#   Last Update :   25 September 2017
#   Description :   Python script that uses the APIs of:
#                   https://haveibeenpwned.com
#                   https://hacked-emails.com
#                   To tell you which emails from a given list of
#                   emails have been leaked
#
#   Usage       :   ./am-i-pwned.py /path/to/email/file

import json
import requests
import time
import sys


def prnt (option, message):
    if option == 0:
        print ( "\033[94mSearching\033[0m %s" % message )
    elif option == 1 :
        print ( "\033[94m>\033[0m %s \033[92m is safe!\033[0m" % message )
    elif option == 2 :
        print ( "\033[94m>\033[0m %s \033[93m is leaked!\033[0m" % message )
    elif option == 3 :
        print ( "\33[93m===>\033[0m %s" % message )

def search_haveibeenpwned ( accounts ):

    prnt (0,"https://www.haveibeenpwned.com ...")
    api_url = "https://haveibeenpwned.com/api/v2/breachedaccount/"

    for account in accounts:

        request = api_url + account
        response = requests.get(request)
        response = response.text

        if response:

            prnt (2, account)
            data = json.loads(response)

            for info in data:

                prnt (3, info["Name"])
        
        else:

            prnt (1, account)

        time.sleep(1.5)

def search_hackedemails ( accounts ):
    prnt (0,"https://www.hacked-emails.com ...")
    api_url = "https://hacked-emails.com/api?q="

    for account in accounts:

        request = api_url + account
        response = requests.get(request)
        response = response.text
        data = json.loads(response)

        if data["status"] == "found":

            prnt (2, account)

            for entry in data["data"]:
                prnt (3, entry["title"])
        
        else:
            prnt (1, account)
        
        time.sleep(1.5)


if __name__ == "__main__" :

    folder = sys.argv[1]

    with open(folder) as file:
        content = file.readlines()

    accounts = [x.strip() for x in content]

    search_haveibeenpwned(accounts)
    search_hackedemails(accounts)

