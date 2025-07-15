import json


class Site:
    def __init__(self, sitename, county, aqi, pollutant, status, pm2_5, pm2_5_avg, latitude, longitude, datacreationdate):
        self.sitename = sitename
        self.county = county
        self.aqi = aqi
        self.pollutant = pollutant
        self.status = status
        self.pm2_5 = pm2_5
        self.pm2_5_avg = pm2_5_avg
        self.latitude = latitude
        self.longitude = longitude
        self.datacreationdate = datacreationdate

def parse_sites_from_json(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    site_list = []
    for sitename in data['records']:
        site = Site(
            sitename=sitename['sitename'],
            county=sitename['county'],
            aqi=sitename['aqi'],
            pollutant=sitename['pollutant'],
            status=sitename['status'],
            pm2_5=sitename['pm2.5'],
            pm2_5_avg=sitename['pm2.5_avg'],
            latitude=sitename['latitude'],
            longitude=sitename['longitude'],
            datacreationdate=sitename['datacreationdate']
        )
        site_list.append(site)
    return site_list

# 使用範例
json_file_path = 'aqx_p_488.json'  # 替換為你的 JSON 檔案路徑
allData = parse_sites_from_json(json_file_path)
for site in allData:
    print(f"站點名稱: {site.sitename}, 縣市: {site.county}, 空氣品質指數: {site.aqi}, 主要污染物: {site.pollutant}, 狀態: {site.status}, PM2.5: {site.pm2_5}, PM2.5 平均值: {site.pm2_5_avg}, 緯度: {site.latitude}, 經度: {site.longitude}, 資料創建日期: {site.datacreationdate}")
