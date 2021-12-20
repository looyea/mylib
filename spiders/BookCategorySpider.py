

from bs4 import BeautifulSoup
import requests

def getCategory(li):
    text_item = ''
    if li.children:
        text_item = ""
        alink = ""
        for child in li.children:
            text_item += child.get_text()
            if child.name == 'span':
                text_item += ' '
            if child.name == 'a':
                alink = child['href']
        # of.write(text_item)
        print(text_item)
        if alink :
            digDownTree(alink)

def digDownTree(url):
    global layer
    global headers
    layer += 1
    if layer > 2:
        layer -= 1
        return
    response = requests.get(url, headers)
    web_data = response.content
    web_data = str(web_data, "utf-8")
    soup = BeautifulSoup(web_data, 'html.parser')
    # 判定是否到了页面根部
    if soup.find("div", id="lost"):
        print("到头了")
        return
    pkgs = soup.findAll("ul")
    pkgs = pkgs[0]
    for li in pkgs:
        getCategory(li)
    layer -=1
    print(layer)

'''
H http://www.ztflh.com/?c=5668
I http://www.ztflh.com/?c=6191
J http://www.ztflh.com/?c=6495
K http://www.ztflh.com/?c=7464
L 
M 
N http://www.ztflh.com/?c=9484
O http://www.ztflh.com/?c=9580
P http://www.ztflh.com/?c=11634
Q http://www.ztflh.com/?c=13945
R http://www.ztflh.com/?c=17417
S http://www.ztflh.com/?c=21152
T http://www.ztflh.com/?c=25844
U http://www.ztflh.com/?c=40585
V http://www.ztflh.com/?c=44097
W
X http://www.ztflh.com/?c=45419
Y
Z http://www.ztflh.com/?c=45735
'''
link = 'http://www.ztflh.com/'

headers = {
    "Cookie" : '__tins__1870281=%7B%22sid%22%3A%201639990132995%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201639991932995%7D; __51cke__=; __51laig__=1',
    "User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36'
}

response = requests.get(link, headers)
web_data = response.content
web_data = str(web_data, "utf-8")
soup = BeautifulSoup(web_data, 'html.parser')
pkgs = soup.findAll("ul")
pkgs = pkgs[0]
urls = list()
layer = 1

with open("output1.txt", 'a', encoding='utf-8') as of:
    for li in pkgs:
        getCategory(li)

of.close()