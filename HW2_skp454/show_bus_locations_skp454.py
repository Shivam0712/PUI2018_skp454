from __future__ import print_function
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import os
import sys

apikey = sys.argv[1]
bus_route= sys.argv[2]

mta_url = "http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&LineRef=%s"%(apikey, bus_route)

mta_response = urllib.urlopen(mta_url)
mta_data = mta_response.read().decode("utf-8")
dataDict = json.loads(mta_data)

print("Bus Line :", bus_route)
dataDictLevel1 = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
print("Number of Active Buses :", len(dataDictLevel1))

for i in range(len(dataDictLevel1)):
    Lon=dataDictLevel1[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    Lat=dataDictLevel1[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    print("Bus ",i," is at latitude ",Lat," and longitude ",Lon)