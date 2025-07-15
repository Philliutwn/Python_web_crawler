import json
import argparse


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

def main():
    parser = argparse.ArgumentParser(description='查詢指定縣市的空氣品質資料')
    parser.add_argument('json_file', help='JSON 檔案路徑')
    parser.add_argument('--county', help='縣市名稱', required=True)
    args = parser.parse_args()

    allData = parse_sites_from_json(args.json_file)
    filtered = [site for site in allData if site.county == args.county]

    if not filtered:
        print(f"找不到縣市：{args.county} 的資料")
    else:
        for site in filtered:
            print(f"站點名稱: {site.sitename}, 縣市: {site.county}, 空氣品質指數: {site.aqi}, 主要污染物: {site.pollutant}, 狀態: {site.status}, PM2.5: {site.pm2_5}, PM2.5 平均值: {site.pm2_5_avg}, 緯度: {site.latitude}, 經度: {site.longitude}, 資料創建日期: {site.datacreationdate}")

if __name__ == '__main__':
    main()

# 使用範例
# python lesson3_5_CLI.py aqx_p_488.json --county 新北市