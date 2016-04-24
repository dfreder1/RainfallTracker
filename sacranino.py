from lxml import etree 
import socket,datetime
from datetime import timedelta
from sys import platform as _platform
#
print 'running with lxml.etree, datetime, sys, and socket modules'
# Get the daily rainfall html, parse it, write data to file
# Website appears to be updated between 8 am and 10 am PT
station_id = ['SAE']
timeout = 1200                 
socket.setdefaulttimeout(timeout)
#
parser=etree.HTMLParser()
#
for item in station_id:       
	#Parse the webpage 
        site = "http://cdec.water.ca.gov/cgi-progs/queryDaily?SAE"
    	tree = etree.parse(site,parser)
        result = etree.tostring(tree.getroot(),pretty_print=True, method="html")
	print('getting station '+item)
        print(result)
#	stationfromweb = tree.find('body').findall('div')[1].find('div').find('h1')
#	print stationfromweb.text
	#
        #Since the webpage always provides a month of data, Get the rainfall value for the
	#29th row which should be at tr = 30
	rownum = 30
	tablerows = tree.xpath('//div/table/tr')
        latestrow = etree.tostring(tablerows[rownum])
        dategrabbed = str.strip(latestrow[24:34])
        print dategrabbed 
        rainsofar2015season = str.strip(latestrow[180:187])
        print rainsofar2015season
        #rainfall = tree.find('body').findall('div')[1].find('div').find('table').findall('tr')[rownum].findall('td')[3]
	print dategrabbed +'  '+rainsofar2015season
        if _platform == "linux" or _platform == "linux2":
            f = open('/var/www/html/SacraNino/data/gauge'+item,'a')
        elif _platform == "darwin":
            f = open('data/gauge'+item,'a')
        elif _platform == "win32":
            print 'not supported'
        yesterday =str(datetime.datetime.today() - timedelta(days=1))
        dayselapsed =(datetime.date.today() - datetime.date(2015,10,01))
        dayselapsed = dayselapsed.days - 1
	print dayselapsed
        f.write('\n'+yesterday+','+str(dayselapsed)+','+rainsofar2015season)              
	f.close()
	print ' '
