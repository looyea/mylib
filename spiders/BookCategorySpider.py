

from bs4 import BeautifulSoup
import requests

def getCategory(li):
    text_item = ''
    if li.children:
        for child in li.children:
            if child.name == 'span':
                text_item += child.get_text()
                text_item += ' '
                of.write(text_item)
                print(child.get_text())
            if child.name == 'a':
                of.write(child.get_text())
                of.writelines('\n')
                print(child.get_text())
                digDownTree(child['href'])

def digDownTree(url):
    response = requests.get(url)
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

link = 'http://www.ztflh.com/'

response = requests.get(link)
web_data = response.content
web_data = str(web_data, "utf-8")
soup = BeautifulSoup(web_data, 'html.parser')
pkgs = soup.findAll("ul")
pkgs = pkgs[0]
urls = list()
layer = 1

with open("output.txt", 'a', encoding='utf-8') as of:
    for li in pkgs:
        getCategory(li)

of.close()