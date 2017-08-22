# -*- coding: cp949 -*-
from RestaurantInfo import *
import HtmlParser

michelinGuideUrl = 'https://guide.michelin.co.kr/ko/restaurant/'

htmlParser = HtmlParser.init(michelinGuideUrl)
htmlRestList = HtmlParser.findAll(htmlParser, 'article', 'restaurant-list-wrap')

restInfoList = []

while 1 :
    for i in range(0, len(htmlRestList)) :
        restInfo = RestaurantInfo()
        restInfo.category = HtmlParser.find(htmlRestList[i], 'span', 'restaurant-list-category').text
        restInfo.title = HtmlParser.find(htmlRestList[i], 'h3', '').text
        restInfo.imgUrl = HtmlParser.find(htmlRestList[i], 'img', '')['src']
        restInfo.grade = HtmlParser.find(htmlRestList[i], 'i', '')['class'][2]
        restInfo.addr = HtmlParser.findAll(htmlRestList[i], 'p', 'ellipsis')[0].text.strip()
        restInfo.phone = HtmlParser.findAll(htmlRestList[i], 'p', 'ellipsis')[1].text.strip()
        restInfo.homepage = HtmlParser.findAll(htmlRestList[i], 'p', 'ellipsis')[2].text.strip()
        restInfoList.append(restInfo)

    if HtmlParser.find(htmlParser, 'li', 'next').a.has_attr('href') :
        nextPageUrl = HtmlParser.find(htmlParser, 'li', 'next').a['href']
        htmlParser = HtmlParser.init(nextPageUrl)
        htmlRestList = HtmlParser.findAll(htmlParser, 'article', 'restaurant-list-wrap')
    else :
        break;

#for i in restInfoList :
    #i.printInfo()
