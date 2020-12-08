from ebird.api import get_observations
from requests.auth import HTTPBasicAuth
from tabulate import tabulate
import webbrowser
import requests
import json
import random
import math

import keys
from webscraper import checkAvailability

api_key = keys.API_KEY
header = {'X-eBirdApiToken': api_key}

text = '''
Welcome to Domain Finder, a service that suggests bird names as your new domain!
           Suggested domains are available for purchase from GoDaddy              
                   Please wait while we pick a domian for you                    
'''

table = [[text]]
print(tabulate(table, tablefmt='grid'))

while 1:
    response = requests.get('https://api.ebird.org/v2/data/obs/KZ/recent?maxResults=300', headers=header)

    def jprint(obj):
        text = json.dumps(obj, indent=4)
        print(text)

    birdsInfo = response.json()

    birdNames = []

    for p in birdsInfo:
        name = p['comName']
        birdNames.append(name)

    searchName = random.choice(birdNames)
    isAvailable, isPremium, domainName, url = checkAvailability(searchName)
    
    if isAvailable == False:
        ask = input('\n' + domainName + '\ndo you wish to search for another domain?\nIf not, the application will close[Y/n]')
        if ask == 'y':
            print('\nOk, finding another domain, please wait')
            continue
        else:
            print('\nExiting the application, have a great day!')
            break
    elif isAvailable and isPremium == False:
        ask = input('\n' + domainName + ' is available.\nWould you like to visit GoDaddy and check it out?[Y/n]')
        if ask == 'y':
            webbrowser.open(url)
            leave = input('Do you want to exit the application?[Y/n]')
            if leave == 'y':
                print('\nHave a great day!')
                break
            else:
                print('\nOk, finding another domain, please wait')
                continue
        else:
            leave = input('Do you want to exit the application?[Y/n]')
            if leave == 'y':
                print('\nHave a great day!')
                break
            else:
                print('\nOk, finding another domain, please wait')
                continue
    elif isAvailable and isPremium:
        ask = input('\n' + domainName + ' is available.\nThis is a premium domain.\nWould you like to visit GoDaddy and check it out?[Y/n]')
        if ask == 'y':
            webbrowser.open(url)
            leave = input('Do you want to exit the application?[Y/n]')
            if leave == 'y':
                print('\nHave a great day!')
                break
            else:
                print('\nOk, finding another domain, please wait')
                continue
        else:
            leave = input('Do you want to exit the application?[Y/n]')
            if leave == 'y':
                print('\nHave a great day!')
                break
            else:
                print('\nOk, finding another domain, please wait')
                continue