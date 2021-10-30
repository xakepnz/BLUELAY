#------------------------------------------------------------------------------#
# Author: xakepnz
# Description: Searches Google to find indexed keywords from online paste sites.
#------------------------------------------------------------------------------#
# Imports:
#------------------------------------------------------------------------------#

import requests
import urllib.parse
from bs4 import BeautifulSoup

#------------------------------------------------------------------------------#
# Data Files:
#------------------------------------------------------------------------------#

proxies_file = 'proxies.conf'
keywords_file = 'keywords.conf'
sources_file = 'sources.conf'

#------------------------------------------------------------------------------#
# Banner:
#------------------------------------------------------------------------------#

def banner():
    print('\n  /#######  /##       /##   /## /######## /##        /######  /##     /##')
    print(' | ##__  ##| ##      | ##  | ##| ##_____/| ##       /##__  ##|  ##   /##/')
    print(' | ##  \ ##| ##      | ##  | ##| ##      | ##      | ##  \ ## \  ## /##/')
    print(' | ####### | ##      | ##  | ##| #####   | ##      | ########  \  ####/') 
    print(' | ##__  ##| ##      | ##  | ##| ##__/   | ##      | ##__  ##   \  ##/')   
    print(' | ##  \ ##| ##      | ##  | ##| ##      | ##      | ##  | ##    | ##') 
    print(' | #######/| ########|  ######/| ########| ########| ##  | ##    | ##')   
    print(' |_______/ |________/ \______/ |________/|________/|__/  |__/    |__/\n')
    print('                            Author: xakepnz')
    print('               Repo: https://www.github.com/xakepnz/BLUELAY\n')

#------------------------------------------------------------------------------#
# Read keywords:
#------------------------------------------------------------------------------#

def read_keywords_and_sources(source_file):
    l_ = []
    
    try:
        with open(source_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.replace('\n','')
                if not line.startswith('#'):
                    l_.append(line)
    except (FileNotFoundError, PermissionError, IsADirectoryError) as e:
        print('Error, failed to read file: "{}" check path.'.format(source_file))
        exit(1)
    
    return l_

#------------------------------------------------------------------------------#
# Read proxies:
#------------------------------------------------------------------------------#

def read_proxies(proxy_file):
    proxies_ = {}
    
    try:
        with open(proxy_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.replace('\n','')
                if not line.startswith('#'):
                    l_ = line.split('://')
                    if isinstance(l_, list) and len(l_) > 1:
                        proxies_['{}://'.format(l_[0])] = l_[1]
    except (FileNotFoundError, PermissionError, IsADirectoryError) as e:
        print('Error, failed to read proxy file: "{}" check path.'.format(proxy_file))
        exit(1)
    
    return proxies_

#------------------------------------------------------------------------------#
# Search Google:
#------------------------------------------------------------------------------#

def crawl_google(params=None, proxies=None):
    r = requests.get(
        'https://www.google.com/search',
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
            'Referer': 'https://www.google.com/',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
        },
        params=params,
        proxies=proxies,
    )

    if r.ok:
        soup_obj = BeautifulSoup(r.text, 'html.parser')
        links_found = find_links(soup_obj)
        if links_found:
            return links_found
    return None

#------------------------------------------------------------------------------#
# Create full search terms:
#------------------------------------------------------------------------------#

def create_search_terms(keywords, sources):
    terms_ = []
    for k in keywords:
        for s in sources:
            t_ = {
                'hl': 'en',
                'as_q': None,
                'as_epq': '{}'.format(k),
                'as_qdr': 'all',
                'as_sitesearch': '{}'.format(s),
                'as_occt': 'any'
            }
            if t_ not in terms_:
                terms_.append(t_)
    return terms_

#------------------------------------------------------------------------------#
# Parse response from Google:
#------------------------------------------------------------------------------#

def find_links(soup_obj):
    links_ = []

    data = soup_obj.find_all('a')

    if data:
        for d in data:
            if d.attrs.get('href'):
                h_ = d.attrs.get('href')
                if 'google.com' not in h_ and h_.startswith('http') and h_ not in links_:
                    links_.append(h_)
    return links_

#------------------------------------------------------------------------------#
# Main:
#------------------------------------------------------------------------------#

# Print banner:
banner()

# Grab the keywords, paste sites and proxy addresses:
keywords = read_keywords_and_sources(keywords_file)
sources = read_keywords_and_sources(sources_file)
proxies = read_proxies(proxies_file)

# Create search terms from the keywords & sources:
search_queries = create_search_terms(keywords, sources)
print('Generated: {} search queries from {} keywords and {} source sites.'.format(len(search_queries),len(keywords),len(sources)))

# Query Google, and print result:
results = []
print('Searching...')
for query_params in search_queries:
    res_ = crawl_google(query_params, proxies)
    if res_ not in results:
        results.append(res_)

# Print results:
print('\nResults for all keywords:\n')
for result_list in results:
    print('\n'.join(result_list))
