from __future__ import print_function
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import os
import sys
import pandas as pd

apikey = sys.argv[1]
bus_route= sys.argv[2]

mta_url = "http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&LineRef=%s"%(apikey, bus_route)

mta_response = urllib.urlopen(mta_url)
mta_data = mta_response.read().decode("utf-8")
dataDict = json.loads(mta_data)

dataDictLevel1 = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
df_busInfo=pd.DataFrame()

for i in range(len(dataDictLevel1)):
    df_busInfoTemp=pd.DataFrame()
    df_busInfoTemp.loc[0,'Longitude'] = dataDictLevel1[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    df_busInfoTemp.loc[0,'Latitude'] = dataDictLevel1[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    try:
        df_busInfoTemp.loc[0,'Stop Name'] = dataDictLevel1[i]['MonitoredVehicleJourney']['MonitoredCall']['StopPointName']
        df_busInfoTemp.loc[0,'Stop Status'] = dataDictLevel1[i]['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance']
    except:
        df_busInfoTemp.loc[0,'Stop Name'] = "N/A"
        df_busInfoTemp.loc[0,'Stop Status'] = "N/A"
    df_busInfo=df_busInfo.append(df_busInfoTemp)
    
df_busInfo.to_csv(sys.argv[3], index=False)