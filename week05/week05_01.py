import urllib.request
import urllib.parse

api = "https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
station_id = input("지역 코드 : ")
values = {'stnId': station_id}

url = api + '?' + urllib.parse.urlencode(values)
print(url)