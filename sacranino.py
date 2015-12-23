import lxml.html as LH
import socket,datetime
from datetime import timedelta
from sys import platform as _platform
#
print 'running with lxml.html and socket modules'
# Get the daily rainfall file, website appears to be updated between 8 am and 10 am PT
station_id = ['SAE']
timeout = 1200                 
socket.setdefaulttimeout(timeout)
#
for item in station_id:       
	#Parse the webpage 
    	tree = LH.parse('http://cdec.water.ca.gov/cgi-progs/queryDaily?SAE')
	print('getting station '+item)  
	stationfromweb = tree.find('body').findall('div')[1].find('div').find('h1')
	print stationfromweb.text
	#Since the webpage always provides a month of data, Get the rainfall value for the
	#29th row which should be at tr = 30
	rownum = 30
	rainfall = tree.find('body').findall('div')[1].find('div').find('table').findall('tr')[rownum].findall('td')[3]
	rainsofar2015season = str.strip(rainfall.text)
	print rainfall.text+'  '+rainsofar2015season
        if _platform == "linux" or _platform == "linux2":
            f = open('/var/www/SacraNino/data/gauge'+item,'a')
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
