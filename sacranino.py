from lxml import etree 
import socket,datetime,shutil
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
        #Since the webpage always provides a month of data, Get the rainfall value for the
	#29th row which should be at tr = 30
	rownum = 30
	tablerows = tree.xpath('//div/table/tr')
        latestrow = etree.tostring(tablerows[rownum])
        dategrabbed = str.strip(latestrow[24:34])
        print dategrabbed 
        rainsofarseason = str.strip(latestrow[180:187])
        print rainsofarseason
	print dategrabbed +'  '+rainsofarseason
        if _platform == "linux" or _platform == "linux2":
            e = '/var/www/html/16-17/data/gauge'
            f = open(e,'a')
            g = '/var/www/html/16-17/data/gauge'+item+'backup'
            shutil.copy(e,g)
        elif _platform == "darwin":
            e = 'data/gauge'+item
            f = open(e,'a')
            g = 'data/gauge'+item+'backup'
            shutil.copy(e, g)
        elif _platform == "win32":
            print 'not supported'
        yesterday = datetime.datetime.today() - timedelta(days=1)
        yesterday = yesterday.strftime("%m" "/" "%d")
        dayselapsed = (datetime.date.today() - datetime.date(2016,10,01))
        dayselapsed = dayselapsed.days - 1
	print dayselapsed
        f.write('\n'+yesterday+','+str(dayselapsed)+','+rainsofarseason)              
	f.close()
	print ' '
