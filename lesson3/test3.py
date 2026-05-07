# 1. Practice how to establish a class
# 2. Practice how to use with ... as 
# 3. How to open a Jason file
# 4. How to grab the data in the Jason file

import json


class Site():
    def __init__(self):
        self.sitename = "City name"
        self.aqi = "aqi"
        self.pollutant = "pollutant"
        self.status = "status"
        self.pm2_5 = "pm2_5"
        self.pm2_5_avg = "pm2_5_avg"
        self.latitude = "latitude"
        self.longitude = "longitude"
        self.date = "date"

s1 = Site()

with open('aqx_p_488.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

data_record: list = data['records'] 

#for i in range(2):
    #print(data_record[i]['sitename'], data_record[i]['aqi'], data_record[i]['pollutant'], data_record[i]['status'], data_record[i]['pm2.5'], data_record[i]['pm2.5_avg'], data_record[i]['latitude'], data_record[i]['longitude'], data_record[i]['datacreationdate'])

for i in data_record:
    s1.sitename = i['sitename']
    s1.aqi = i['aqi']
    s1.pollutant = i['pollutant']
    s1.status = i['status']
    s1.pm2_5 = i['pm2.5']
    s1.pm2_5_avg = i['pm2.5_avg']
    s1.latitude = i['latitude']
    s1.longitude = i['longitude']
    s1.date = i['datacreationdate']
    print(s1.sitename, s1.aqi, s1.pollutant, s1.status, s1.pm2_5, s1.pm2_5_avg, s1.latitude, s1. longitude, s1.date)
