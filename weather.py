from urllib.request import urlopen, Request
import urllib
import bs4
from asciicanvas import AsciiCanvas

def get_weather():
    enc_location = urllib.parse.quote('날씨')

    url = 'https://search.naver.com/search.naver?ie=utf8&query='+ enc_location

    req = Request(url)
    page = urlopen(req)
    html = page.read()
    soup = bs4.BeautifulSoup(html,'html5lib')

    location = soup.find('div', class_='weather_box').find('em').text
    temperature = soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text

    enc_location = urllib.parse.quote('영어로+' + location)
    url = 'https://search.naver.com/search.naver?ie=utf8&query='+ enc_location

    req = Request(url)
    page = urlopen(req)
    html = page.read()
    soup = bs4.BeautifulSoup(html,'html5lib')

    en_location = soup.find('div', class_='sentence en').find('strong').text

    en_location = en_location.replace(' 전체듣기', '')
    return en_location , temperature
# print('ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ')
# print('ㅁ　　　　　　　　　　　　　　　　　　　　　　　　　　ㅁ')
# print('ㅁ      현재 ' + en_location + ' 날씨는 ' + temperature + '도 입니다.       ㅁ')
# print('ㅁ　　　　　　　　　　　　　　　　　　　　　　　　　　ㅁ')
# print('ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ')
