# BLUELAY

## Description:

Searches online paste sites for certain search terms which can indicate a possible data breach.<br />
For example if your client signed up to a small business website, which ended up being a victim of a data breach.<br />
The results could appear on various different paste sites, or other sources. This tool searches for domains on those specified sources.

## Poc:

<b>keyword: BLUELAY source: github.com</b>

![Alt](/poc.jpg "Proof of Concept")

## Install:

```bash
git clone https://github.com/xakepnz/BLUELAY.git
cd BLUELAY
pip install -r requirements.txt
python3 bluelay.py
```

## Usage:

Edit the three config files.<br />
* keywords.conf containing all the keywords you want to search for.<br />
* sources.conf all of the sites you want to search against.<br />
* proxies.conf proxies to route requests through, to avoid Google ban.<br />

## Examples:

<b>keywords.conf</b>
```bash
# These are the keywords to search against Google. They can be simply domain names, or specific terminology.
# Anything behind a hashtag like this line, will be ignored.
BLUELAY
```

<b>sources.conf</b>
```bash
# These are new line separated domain names that you want to search against.
# The domain names must be able to be indexed/spidered by Google.
# Anything behind a hashtag like this line, will be ignored.
# pastebin.com
# pastie.org.ru
# paste.org
# hackforums.net
# antichat.ru
github.com
```

<b>proxies.conf</b>
```bash
# Enter new proxies below on a new line
# Anything behind a hashtag like this line, will be ignored.
# Format: schema://ip_or_domain:port
# http://1.1.1.1:80
# https://1.1.1.1:443
```
