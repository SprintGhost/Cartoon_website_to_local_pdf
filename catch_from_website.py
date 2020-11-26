import ssl
import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
from selenium import webdriver 

total_pitcures = 0
picture_list = list()
def screen_shot(url):
    global total_pitcures
    global picture_list

    png_name = "picture/" + str(total_pitcures) + ".png"
    total_pitcures += 1
    picture_list.append(png_name)
    brower = webdriver.PhantomJS()
    brower.get(url)
    brower.maximize_window()
    brower.save_screenshot(png_name)
    brower.close()

def get_link(url):
    headers = {'User-Agent': '(Linux;U;Android 2.3;en-us;Nexus One Build/FRF91)AppleWebKit/999+(KHTML, like Gecko)Version/4.0 Mobile Safari/999.9'}
    context = ssl._create_unverified_context()
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request,context=context)
    data = response.read()
    soup = BeautifulSoup(data, 'html.parser')
    tags = soup.find('div', class_='UdPag').find_all('mip-link')
    for tag in tags:
        print(tag.get('href', None), end = "\n")
        return tag.get('href', None)


if __name__ == '__main__':
    url ="https://m.xialashimanhua.com/manhua/huibuqudexiatian/1335161.html"
    screen_shot(url)
    while url != "https://m.xialashimanhua.com/manhua/huibuqudexiatian/1335232-133.html":
        url = get_link(url)
        screen_shot(url)

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# 

