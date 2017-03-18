# Leaky.py
										 
<b>[+] Website:</b> https://intellipedia.ch<br />
<b>[+] Name:</b> Leaky.py<br />
<b>[+] Author:</b> xakep<br />
<b>[+] Date:</b> March 2017<br />
<b>[+] OS:</b> Linux<br />
<hr>
<b>[+] Usage Examples:</b><br />

screen python Leaky.py<br />
python Leaky.py -c allclients.txt -s allsources.txt<br />
python Leaky.py -c client1.txt  -s source1.txt -o output.txt<br />
python Leaky.py -c client2.txt -s source2.txt -t 9001 -v<br />
python Leaky.py --clients client3.txt --sources source3.txt --timeout 9001 --output CustomOutput.txt --verbose<br />
<hr>

<b>[+] Description:</b><br />

This is a simple script which uses google to define search terms to search sites that have been indexed.<br />
For example if your client signed up to a small business website, which ended up being a victim of a data breach.<br />
The results could appear on various different paste sites, or other sources. This tool searches for domains on those specified sources.
<hr>

<b>[+] To-Do:</b><br />

Implement proxy or tor method, where it cycles between addresses to avoid being detected.<br />
Implmenet email or SNMP alerting when results are found.<br />
Implement cron-tasks so it can be above googles data request threshold.<br />
<hr>
