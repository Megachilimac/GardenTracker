import urllib2
import json
year = raw_input("Please enter year as YYYY: ")
month = raw_input("Please enter month as MM: ")
day = raw_input("Please enter day as DD: ")
date = year+month+day
#date = '20120916'
openstring = 'http://api.wunderground.com/api/971e4fa8d4bae2a9/history_' + date + '/q/MO/Saint_Peters.json'
f = urllib2.urlopen(openstring)
json_string = f.read()
parsed_json = json.loads(json_string)

maxtempi = parsed_json['history']['dailysummary'][0]['maxtempi']
mintempi = parsed_json['history']['dailysummary'][0]['mintempi']
precipi = parsed_json['history']['dailysummary'][0]['precipi']
maxpressurei = parsed_json['history']['dailysummary'][0]['maxpressurei']
minpressurei = parsed_json['history']['dailysummary'][0]['minpressurei']

print "Max temperature is : %s" % (maxtempi)
print "Min temperature is : %s" % (mintempi)
print "Total precip is    : %s" % (precipi)
print "Max pressure is    : %s" % (maxpressurei)
print "Min pressure is    : %s" % (minpressurei)
f.close()