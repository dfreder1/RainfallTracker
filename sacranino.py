import lxml.html as LH
#from lxml import etree
import socket,datetime
from datetime import timedelta
print 'running with lxml.html and socket modules'
##Get the daily rainfall file
station_id = ['SAE']
timeout = 1200                 
socket.setdefaulttimeout(timeout)

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
	f = open('data/gauge'+item,'a')
        yesterday =str(datetime.datetime.today() - timedelta(days=1))
        dayselapsed =(datetime.date.today() - datetime.date(2015,10,01))
        dayselapsed = dayselapsed.days - 1
	print dayselapsed
        f.write('\n'+yesterday+','+str(dayselapsed)+','+rainsofar2015season)              
	f.close()
	print ' '
	#print([td.text_content() for td in tree.xpath('//td')])
	#Get the value for the number of the days elapsed since 10/1
	#numofdaysyesterday = datetime.date.today().timetuple().tm_mday - 1
	#There are a number of rows ('tr') before the day count starts so offset by that much
	#rownumber = numofdaysyesterday+2
	#Get the rainfall value for that row
	#rainfall = tree.find('body').findall('div')[1].find('div').find('table').findall('tr')[rownumber].findall('td')[3]
	#print rainfall.text
