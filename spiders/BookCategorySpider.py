

from bs4 import BeautifulSoup
import requests
import yaml
from yaml import Loader
import os


def getCategory(li):
    global layer
    if li.children:
        text_item = ""
        alink = ""
        for child in li.children:
            text_item += child.get_text()
            if child.name == 'span':
                text_item += ' '
            if child.name == 'a':
                alink = child['href']
        for i in range(1, layer-1):
            of.write('\t')
        of.write(text_item)
        of.write('\n')
        print(text_item)
        if alink :
            digDownTree(alink)


def digDownTree(url):
    global layer
    global headers
    layer += 1
    if layer > MAX_LAYER:
        layer -= 1
        return
    response = requests.get(url, headers)
    web_data = str(response.content, "utf-8")
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


config_file = open("config.yaml", 'r')
config = yaml.load(config_file, Loader)
config_file.close()

headers = {
    "Cookie": config["Cookie"],
    "User-Agent": config["UserAgent"]
}

response = requests.get(config["RootURL"], headers)
web_data = str(response.content, "utf-8")
soup = BeautifulSoup(web_data, 'html.parser')
pkgs = soup.findAll("ul")
pkgs = pkgs[0]
urls = list()
layer = 1
MAX_LAYER = int(config["MaxLayer"])

with open(config["OutputFile"], 'a', encoding='utf-8') as of:
    for li in pkgs:
        getCategory(li)

of.close()