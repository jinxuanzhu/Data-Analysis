# coding:utf-8
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

#获取1月份所有文章链接
#链接中 active 为课程或者活动，其他为文章

class RRpmData(object):

    def __init__(self, headers, url):
        self.headers = headers;
        self.url = url;

    @property
    def get_url(self):
        response = requests.get(url=self.url, headers=self.headers)
        html0 = response.text
        soup0 = BeautifulSoup(html0, 'html.parser')  # BeautifulSoup HTML/XML的解析器
        getUrl = soup0.find_all("loc")
        getDate = soup0.find_all("lastmod")
        for (u, g) in zip(getUrl, getDate):
            #lastmod = g.get_text().split('T')[0]
            if u.get_text().find('active') == -1 :
                u1r1 = u.get_text()
                response1 = requests.get(url=u1r1, headers=self.headers)
                html1 = response1.text
                soup1 = BeautifulSoup(html1, 'html.parser')
                # 获取标题
                title = soup1.select("h2[class=article-title]")[0].contents[0]
                # 获取阅读览量
                read = soup1.find_all("div", class_="postMetaInline postMetaInlineSupplemental post-meta-items")[0].contents[3].get_text()
                # 获取收藏量
                collection = soup1.find_all("div", class_="postMetaInline postMetaInlineSupplemental post-meta-items")[0].contents[5].get_text()
                # 获取点赞量
                like = soup1.find_all("div", class_="postMetaInline postMetaInlineSupplemental post-meta-items")[0].contents[7].get_text().replace("\n", "")
                with open('rrcp.csv', 'a+', encoding='utf-8-sig') as f:
                    f.write(u1r1 + ','  + title + ',' + read  + ',' + collection + ',' + like + '\n')


if __name__ == '__main__':
    starttime = datetime.datetime.now()
    with open('rrcp.csv', 'w', encoding='utf-8-sig') as f:
        f.write('url' + ',' + 'title'+ ',' + 'read' + ',' + 'collection' + ',' + 'like' + '\n')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
    }
    url = 'http://www.woshipm.com/sitemap-pt-post-2019-01.xml'

    rrpmData = RRpmData(headers , url)
    rrpmData.get_url
    endtime = datetime.datetime.now()
    print(endtime - starttime)





