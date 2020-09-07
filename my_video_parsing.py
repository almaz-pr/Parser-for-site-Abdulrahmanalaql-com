import requests
from bs4 import BeautifulSoup as bs
import asyncio

URL = 'http://abdulrahmanalaql.com/'
TEXTLEN = 45


def audio_folders(page):
    page_num = 2
    vid = 0
    curDate = ''
    aTLIST = []
    aLList = []
    error = 'هذه صفحة خالية من المعلومات!'
    req = requests.get(URL + str(page))
    soup = bs(req.text, 'lxml')
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
        container = soup.find_all('div', attrs={'class', 'col-md-12'})
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
                        container = soup.find_all('div', attrs={'class', 'col-md-12'})
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
                    link = container.find(attrs={"name": "movie"}).get("value")  # attrs={'name": "movie"}
                    title = container.find("p", align="center").get_text()
                    curDate = container.find('div', 'col-xs-5').get_text()
                    link = link.replace("/v/", "/watch?v=")
                    title = title.replace('\n', "").replace('\r', "")
                    if len(title) > TEXTLEN: title = "... " + title[:TEXTLEN]
                    vid = 1
                    aLList.append(link)
                    aTLIST.append(title)
                else:
                    aTLIST = [error]
                    aLList = ['0']
            else:
                aTLIST = [error]
                aLList = ['0']
    if vid == 0:
        return aLList, aTLIST, vid, curDate
    else:
        return aLList, aTLIST, vid, curDate


def parsing(page):
    req = requests.get(URL + str(page))
    soup = bs(req.text, 'lxml')
    return soup
