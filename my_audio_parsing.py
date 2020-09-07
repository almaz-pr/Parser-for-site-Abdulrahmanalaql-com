import requests
from bs4 import BeautifulSoup as bs
import asyncio

URL = 'http://abdulrahmanalaql.com/'
TEXTLEN = 45


def audio_folders(page):
    page_num = 2
    mp3 = 0
    empty = ''
    mp3Link = ''
    descr = ''
    author = ''
    curDate = ''
    aTLIST = []
    aLList = []
    error = 'هذه صفحة خالية من المعلومات!'
    soup = parsing(page)
    container = soup.find_all('div', attrs={'class', 'cats-3'})
    if len(container) > 0:
        for x in container:
            link = x.find('a').get('href')
            title = x.find('h4').get_text()
            title = title.replace("\n", "")
            if len(title) > TEXTLEN: title = "... " + title[:TEXTLEN]
            aLList.append(link)
            aTLIST.append(title)
            if len(aLList) >= 20:
                w = True
                while w:
                    page_str_format = (''.join(i for i in page if not i.isdigit())).replace('-.html', '')
                    page_int_format = ''.join(i for i in page if i.isdigit())
                    page_constr = 'catplay.php?' + page_str_format + '=' + page_int_format + '&page=' + str(page_num)
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
        container = soup.find_all('div', attrs={'class', 'cats-4'})
        if len(container) > 0:
            for x in container:
                link = x.find('a').get('href')
                title = x.find('h4').get_text()
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
            container = soup.find('div', attrs={'class', 'panel-body'})
            if container is not None:
                if len(container) > 0:
                    link = container.find('a').get('href')
                    title = container.find('h4').get_text()
                    title = title.replace("\n", "")
                    last_chars = link[-3:]
                    print(last_chars)
                    if len(title) > TEXTLEN: title = "... " + title[:TEXTLEN]
                    if link[-1] == '3':
                        container = soup.find_all('div', attrs={'class', 'pull-right'})
                        for x in container:
                            descr = x.find('p').get_text()
                            descr = descr.replace("\n", "")
                        container = soup.find('div', attrs={'class', 'panel-body'})
                        for x in container:
                            mp3Link = container.find('a').get('href')
                        container = soup.find('div', attrs={'class', 'col-sm-6'})
                        author = container.find('h4').get_text()
                        container = soup.find_all('div', attrs={'class', 'col-xs-5'})
                        for x in container:
                            curDate = x.find('span').get_text()
                        mp3 = 1
                    aLList.append(link)
                    aTLIST.append(title)
                else:
                    aTLIST = [error]
                    aLList = ['0']
            else:
                aTLIST = [error]
                aLList = ['0']
    if mp3 == 0:
        return aLList, aTLIST, mp3, empty, empty, empty
    else:
        return mp3Link, descr, mp3, author, curDate, last_chars


def parsing(page):
    req = requests.get(URL + str(page))
    soup = bs(req.text, 'lxml')
    return soup

