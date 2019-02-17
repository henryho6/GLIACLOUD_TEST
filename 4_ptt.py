# -*- coding: utf-8 -*-
from PttWebCrawler.crawler import PttWebCrawler as crawler
import codecs, json, os


link = 'https://www.ptt.cc/bbs/PublicServan/M.1409529482.A.9D3.html'
link_split = link.split('/')
print(link_split[4])

article_id = link_split[5].replace('.html','')
board = link_split[4]

jsondata = json.loads(crawler.parse(link, article_id, board))


print('日期:', jsondata['date'])
print('作者:', jsondata['author'])
print('標題:', jsondata['article_title'])
print('內文:', jsondata['content'])
print('看版名稱:', jsondata['board'])

