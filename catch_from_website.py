# import pdfkit
# import urllib.request
# import ssl
 

# url = "https://m.xialashimanhua.com/manhua/huibuqudexiatian/1335231-15.html"
 
# headers = {'User-Agent': '(Linux;U;Android 2.3;en-us;Nexus One Build/FRF91)AppleWebKit/999+(KHTML, like Gecko)Version/4.0 Mobile Safari/999.9'}
# context = ssl._create_unverified_context()
# request = urllib.request.Request(url, headers=headers)
# response = urllib.request.urlopen(request,context=context)
# data = response.read()
 
# #设置解码方式
# data = data.decode('utf-8')

# with open("test.html",'w') as f:
#     f.writelines(data)

# pdfkit.from_file("test.html",'out.pdf')


from selenium import webdriver 
def screen_shot(url,png_name):
    brower = webdriver.PhantomJS()
    brower.get(url)
    brower.maximize_window()
    brower.save_screenshot(png_name)
    brower.close()
if __name__ == '__main__':
    url ="https://m.xialashimanhua.com/manhua/huibuqudexiatian/1335231-15.html"
    screen_shot(url,'1.png')

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import os
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--start-maximized')
# path = os.getcwd()


# for i in range(60):
#     url = "test.html"
#     print(url)
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.get(url)
#     width = driver.execute_script("return Math.max(document.body.scrollWidth,document.body.offsetWidth, document.documentElement.clientWidth, document.documentElement.scrollWidth, document.documentElement.offsetWidth);")
#     height = driver.execute_script("return Math.max(document.body.scrollHeight, document.body.offsetHeight,document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")
#     driver.set_window_size(width,height)
    
#     driver.save_screenshot('test.png')
#     driver.close()

