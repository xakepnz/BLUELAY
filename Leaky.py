#!/usr/bin/python
# /##                           /##
#| ##                          | ##
#| ##        /######   /###### | ##   /## /##   /##      /######  /##   /##
#| ##       /##__  ## |____  ##| ##  /##/| ##  | ##     /##__  ##| ##  | ##
#| ##      | ########  /#######| ######/ | ##  | ##    | ##  \ ##| ##  | ##
#| ##      | ##_____/ /##__  ##| ##_  ## | ##  | ##    | ##  | ##| ##  | ##
#| ########|  #######|  #######| ## \  ##|  ####### /##| #######/|  #######
#|________/ \_______/ \_______/|__/  \__/ \____  ##|__/| ##____/  \____  ##
#                                         /##  | ##    | ##       /##  | ##
#                                        |  ######/    | ##      |  ######/
#                                         \______/     |__/       \______/
#[+] Website: https://intellipedia.ch
#[+] Name: Leaky.py
#[+] Author: xakep
#[+] Date: March 2017
###################################################################################################################
# Imports - May need to sudo pip install <module-name> || sudo apt-get install python-<module-name>
###################################################################################################################

import argparse
import json
import requests
import sys
import os
import time
from bs4 import BeautifulSoup

###################################################################################################################
# Variables
###################################################################################################################

domains = []
sites = []
bots = []

class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

###################################################################################################################
# See if there's some input, else move back to defaults
###################################################################################################################

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--clients', help='Conf containing client domains.',required=False)
parser.add_argument('-s', '--sources', help='Conf containing sites to search on.',required=False)
parser.add_argument('-p', '--proxies', help='Conf containing proxies to run searches through.',required=False)
parser.add_argument('-t', '--timeout', help='Timeout in seconds between each request.',required=False, type=int)
parser.add_argument('-v', '--verbose', help='Verbose Output.',required=False, action='store_true')
args = parser.parse_args()
clients = args.clients
sources = args.sources
proxies = args.proxies
timeout = args.timeout
verbose = args.verbose

if (verbose is True):
    print bcolors.OKBLUE,'[+] Verbose Mode: On',bcolors.ENDC
else:
    pass

if (timeout is None):
    timeout = 30
    print bcolors.OKBLUE,'[+] Using Default Timeout:',timeout,bcolors.ENDC
elif (timeout is not None):
    print bcolors.OKBLUE,'[+] Using Timeout:',timeout, bcolors.ENDC

if (clients is None):
    clients = 'clients.conf'
    print bcolors.OKBLUE,'[+] Using Default Clients File:',clients,bcolors.ENDC
elif (clients is not None):
    print bcolors.OKBLUE,'[+] Using Clients from:',clients,bcolors.ENDC

if (sources is None):
    sources = 'sources.conf'
    print bcolors.OKBLUE,'[+] Using Default Sources File:',sources,bcolors.ENDC
elif (sources is not None):
    print bcolors.OKBLUE,'[+] Using Sources File:',sources,bcolors.ENDC

if (proxies is None):
    print bcolors.WARNING,'[+] Using Default Connection - No proxies added',bcolors.ENDC
elif (proxies is not None):
    print bcolors.OKBLUE,'[+] Using Proxies File:',proxies,bcolors.ENDC

###################################################################################################################
# Read all the conf
###################################################################################################################

def readClients():
            try:
               tempDomains = tuple(open(clients, 'r'))
               for d in tempDomains:
                   domains.append(d.strip())
               if verbose is True:
                   for d in domains:
                       print bcolors.BOLD,'[*] Client Loaded:',d,bcolors.ENDC
               else:
                   pass
            except IOError:
               print bcolors.FAIL,'[!] Error: Clients file:',clients,'could not be read',bcolors.ENDC
               exit(0)
            except KeyboardInterrupt:
               print bcolors.FAIL,'[!] Stopped by User',bcolors.ENDC
               exit(0)

def readSources():
            try:
               tempSources = tuple(open(sources, 'r'))
               for s in tempSources:
                   sites.append(s.strip())
               if verbose is True:
                   for s in sites:
                       print bcolors.BOLD,'[*] Source Loaded:',s,bcolors.ENDC
               else:
                   pass
            except IOError:
                print bcolors.FAIL,'[!] Error: Sources file:',sources,'could not be read',bcolors.ENDC
                exit(0)
            except KeyboardInterrupt:
                print bcolors.FAIL,'[!] Stopped by User',bcolors.ENDC
                exit(0)

def readProxies():
        if (proxies is not None):
            try:
               tempProxies = tuple(open(proxies, 'r'))
               for b in tempProxies:
                   bots.append(b.strip())
               if verbose is True:
                   for b in bots:
                       print bcolors.BOLD,'[*] Proxy Loaded:',b,bcolors.ENDC
               else:
                   pass
            except IOError:
                print bcolors.FAIL,'[!] Error: Proxies file:',proxies,'could not be read',bcolors.ENDC
                exit(0)
            except KeyboardInterrupt:
                print bcolors.FAIL,'[!] Stopped by User',bcolors.ENDC
                exit(0)
        else:
            pass

def readLists():
        try:
           if verbose is True:
               print bcolors.BOLD,'[+] Total Proxies:',len(bots),bcolors.ENDC
               print bcolors.BOLD,'[+] Total Clients:',len(domains),bcolors.ENDC
               print bcolors.BOLD,'[+] Total Sources:',len(sites),bcolors.ENDC
               print bcolors.BOLD,'[+] Timeout:',timeout,'seconds',bcolors.ENDC
        except KeyboardInterrupt:
           print bcolors.FAIL,'[!] Stopped by User',bcolors.ENDC
           exit(0)

###################################################################################################################
# Output
###################################################################################################################

readClients()
readSources()
readProxies()
readLists()

###################################################################################################################
# Dork the crap outta the input
###################################################################################################################

try:
   for d in domains:
       for s in sites:
           url = ('http://www.google.com/search?hl=en&as_q=&as_epq=' + d + '&as_qdr=all&as_sitesearch=' + s + '&as_occt=any')
           if proxies is not None:
              result = requests.get(url, proxies=bots, timeout=timeout)
           else:
               result = requests.get(url, timeout=timeout)
               soup = BeautifulSoup(result.text, 'html.parser')
           if ('No results found' in result.content):
               print bcolors.OKGREEN,'[+] Client:',d,'[+] Was not found on source:',s,'[+] Search param:',d,'site:google.com',bcolors.ENDC
           if ('did not match' in result.content):
               print bcolors.OKGREEN,'[+] Client:',d,'[+] Did not match onsource:',s,'[+] Search param:',d,'site:google.com',bcolors.ENDC
           if ('Our systems have detected unusual traffic from your computer' in result.content):
               print bcolors.FAIL,'[!] Google have implemented blocking. Try longer timeout, different host, or -p',bcolors.ENDC
               exit(0)
           elif soup is None:
               print bcolors.OKGREEN,'[+] Client:',d,'[+] Was not found on source:',s,'[+] Search param:',d,'site:google.com',bcolors.ENDC
           else:
               gold = (soup.find('div',{'id':'resultStats'}).text)
               location = (soup.find('cite').text)
               print bcolors.FAIL,'[!] Client:',d,' [!] Found: ' + gold + ' [!] URL: ' + location + ' [+] Search param:',d,'site:google.com',bcolors.ENDC
except requests.exceptions.Timeout:
    print bcolors.FAIL,'[!] Proxy timed out',bcolors.ENDC
except KeyboardInterrupt:
    print bcolors.FAIL,'[!] Stopped by User',bcolors.ENDC
    exit(0)
