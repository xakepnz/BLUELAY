# Leaky.py
										 
<b>[+] Website:</b> https://intellipedia.ch<br />
<b>[+] Name:</b> Leaky.py<br />
<b>[+] Author:</b> xakep<br />
<b>[+] Date:</b> March 2017<br />
<b>[+] OS:</b> Linux<br />
<hr>

<b>[+] Defaults:</b><br />

clients.conf - contains line by line of the domain you wish to search.
sources.conf - contains line by line the sites you wish to search against.
proxies.conf - contains the proxies you wish to send requests through (faster).

<b>[+] Usage Examples:</b><br />

screen python Leaky.py<br />
python Leaky.py -c allclients.conf -s allsources.conf<br />
python Leaky.py -c client1.conf  -s source1.conf -v<br />
python Leaky.py -c client2.conf -s source2.conf -t 9001 -v<br />
python Leaky.py -c client2.conf -s source2.conf -p proxies2.conf -t 9001 -v<br />
python Leaky.py --clients client3.conf --sources source3.conf --proxies proxy3.conf --timeout 9001 --verbose<br />
<hr>

<b>[+] Description:</b><br />

Searches online paste sites for certain search terms which can indicate a possible data breach.<br />
For example if your client signed up to a small business website, which ended up being a victim of a data breach.<br />
The results could appear on various different paste sites, or other sources. This tool searches for domains on those specified sources.
<hr>

<b>[+] To-Do:</b><br />

Fix current issues of Attribute None for text.
Fix issue with reading proxy file and creating list.
Implmenet email or SNMP alerting when results are found.<br />
Implement cron-tasks so it can be above googles data request threshold.<br />
<hr>
