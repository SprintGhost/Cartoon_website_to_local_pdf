import ssl
import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities 

total_pitcures = 0
picture_list = list()
headers = {'User-Agent': '(Linux;U;Android 2.3;en-us;Nexus One Build/FRF91)AppleWebKit/999+(KHTML, like Gecko)Version/4.0 Mobile Safari/999.9'}
def screen_shot(url):
    global total_pitcures
    global picture_list
    global headers
    png_name = "picture/" + str(total_pitcures) + ".png"
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = headers['User-Agent']
    total_pitcures += 1
    picture_list.append(png_name)
    brower = webdriver.PhantomJS(desired_capabilities=dcap)
    brower.get(url)
    brower.maximize_window()
    brower.save_screenshot(png_name)
    brower.close()

def get_link(url):
    global headers
    context = ssl._create_unverified_context()
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request,context=context)
    data = response.read()
    soup = BeautifulSoup(data, 'html.parser')
    tags = soup.find('div', class_='UdPag').find_all('mip-link')
    imags = soup.find_all('mip-img')
    print(imags)
    for each in imags:
        print (each.get('src'),end= "\n")
    # imags = imags.find("mip-img", class_= "mip-element mip-layout-container mip-img-loaded")
    # imags = soup('img')
    for tag in tags:
        print(tag.get('href', None), end = "\n")
        return tag.get('href', None)

if __name__ == '__main__':
    url ="https://m.xialashimanhua.com/manhua/huibuqudexiatian/1335161.html"
    screen_shot(url)
    while total_pitcures < 2 and url != "https://m.xialashimanhua.com/manhua/huibuqudexiatian/1335232-133.html":
        url = get_link(url)
        total_pitcures += 1
        # screen_shot(url)




