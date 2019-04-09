from bs4 import BeautifulSoup
import base64
import re
import requests
import sys
class crawler():
    def __init__(self, url):
        self.url = url
        self.result = ""
    def ignore_non_BMP(self):
            self.result = self.result.encode("Big5","ignore")
            self.result = self.result.decode("Big5","ignore")
    def getRequest(self,key):
        payload = {'slt_k_option':1, 'store_k_word': base64.b64encode(key.encode('ascii'))}
        request = requests.get(self.url, params = payload)
        request.encoding = 'big5'
        soup = BeautifulSoup(request.text, "lxml")
        return soup
    def crawl(self, key):
        contents = self.getRequest(key).find_all("div", "pic2t pic2t_bg")
        for content in contents:
            self.result = self.result + content.find("a").text + "\n"
        self.ignore_non_BMP()
if __name__ == '__main__':
    sample = crawler("https://www.pcstore.com.tw/adm/psearch.htm")
    f = open("result.txt","w")
    text =input()
    sample.crawl(text)
    print(sample.result)
    f.write(sample.result)
    f.close()    
        
