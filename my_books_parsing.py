import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup as bs
# import asyncio
from functools import partial
import threading
import math
import time
import my_dwnld as dwnld
import my_downloads_page as dPage

URL = 'http://abdulrahmanalaql.com/'
TEXTLEN = 45

def book_folders(page):
    page_num = 2
    bks = 0
    curDate = ''
    empty = ''
    aTLIST = []
    aLList = []
    error = 'هذه صفحة خالية من المعلومات!'
    req = requests.get(URL + str(page))
    soup = bs(req.text, 'lxml')
    container = soup.find_all('div', attrs={'class', 'cats-4'})
    if len(container) > 0:
        for x in container:
            link = x.find('a').get('href')
            title = x.find('a').get_text()
            title = title.replace("\n", "")
            if len(title) > TEXTLEN: title = "... " + title[:TEXTLEN]
            aLList.append(link)
            aTLIST.append(title)
            if len(aLList) >= 20:
                w = True
                while w:
                    page_str_format = (''.join(i for i in page if not i.isdigit())).replace('-.html', '')
                    page_int_format = ''.join(i for i in page if i.isdigit())
                    page_constr = 'catplay.php?' + page_str_format + '=' + page_int_format + '&page=' + str(
                        page_num)
                    soup = parsing(page_constr)
                    container = soup.find_all('div', attrs={'class', 'cats-4'})
                    if len(container) > 0:
                        for x in container:
                            link = x.find('a').get('href')
                            title = x.find('h4').get_text()
                            title = title.replace("\n", "")
                            if len(title) > TEXTLEN: title = "... " + title[:TEXTLEN]
                            aLList.append(link)
                            aTLIST.append(title)
                    else:
                        w = False
                    page_num += 1
    else:
        container = soup.find_all('div', attrs={'class', 'cats-3'})
        if len(container) > 0:
            for x in container:
                link = x.find('a').get('href')
                title = x.find('a').get_text()
                title = title.replace("\n", "")
                if len(title) > TEXTLEN: title = "... " + title[:TEXTLEN]
                aLList.append(link)
                aTLIST.append(title)
                if len(aLList) >= 20:
                    w = True
                    while w:
                        page_str_format = (''.join(i for i in page if not i.isdigit())).replace('-.html', '')
                        page_int_format = ''.join(i for i in page if i.isdigit())
                        page_constr = 'catplay.php?' + page_str_format + '=' + page_int_format + '&page=' + str(
                            page_num)
                        soup = parsing(page_constr)
                        container = soup.find_all('div', attrs={'class', 'cats-3'})
                        if len(container) > 0:
                            for x in container:
                                link = x.find('a').get('href')
                                title = x.find('h4').get_text()
                                title = title.replace("\n", "")
                                if len(title) > TEXTLEN: title = "... " + title[:TEXTLEN]
                                aLList.append(link)
                                aTLIST.append(title)
                        else:
                            w = False
                        page_num += 1
        else:
            container = soup.find('div', attrs={'class', 'panel-body'})
            if len(container) > 0:
                bks = 1
                link1 = container.find_all('a')
                link = link1[1].get('href')
                if link[-4] == '.':
                    last_chars = link[-3:]
                    print(last_chars)
                else:
                    last_chars = link[-4:]
                    print(last_chars)
                author = container.find('h4').get_text()
                author = author.replace("\n", "")
                container = soup.find_all('div', attrs={'class', 'pull-right'})
                for x in container:
                    descr = x.find('span').get_text()
                    descr = descr.replace("\n", "")
                    print(descr)
                    if len(descr) > TEXTLEN: title = "... " + descr[:TEXTLEN]
                container = soup.find_all('div', attrs={'class', 'col-xs-5'})
                for x in container:
                    curDate = x.find('span').get_text()
                aLList.append(link)
                aTLIST.append(descr)
                time.sleep(0.5)
            else:
                aTLIST = [error]
                aLList = ['0']
    if bks == 0:
        return aLList, aTLIST, bks, empty, empty, empty
    else:
        return link, descr, bks, author, curDate, last_chars

def parsing(page):
    req = requests.get(URL + str(page))
    soup = bs(req.text, 'lxml')
    return soup
