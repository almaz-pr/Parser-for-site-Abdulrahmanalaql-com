import requests
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile
import threading
import configparser

URL = 'http://abdulrahmanalaql.com/'


def saveAs(page, last_chars):
    file = asksaveasfile(mode="wb", defaultextension="." + last_chars)
    messagebox.showinfo("التحميل", "بدأ التحميل")
    if file is None:
        return
    else:
        t1 = threading.Thread(target=download, args=(file.name, page,))
        t1.start()



def download(way, page):
    config = configparser.ConfigParser()
    print('way is: %s page is: %s' % (way, page))
    req = requests.get(URL + str(page), stream=True)
    total_length = req.headers.get('content-length')
    total_length = int(total_length)
    print('total_length: ' + str(total_length))
    # open(str(way), 'wb').write(downloaded_obj.content)
    dl = 0
    file_name = page.split("/")[-1]
    with open(str(way), 'wb') as file:
        for chunk in req.iter_content(chunk_size=1024 * 1024):
            dl += len(chunk)
            done = int(50 * dl / total_length)
            print("\r[%s%s]" % ('=' * done, ' ' * (50 - done)))
            config[file_name] = {
                "name": str(way),
                "total": str(total_length),
                "percent": str(done * 2),
                "done": str(dl)
            }

            if chunk:
                file.write(chunk)
            with open('downloads/' + file_name + '.dll', 'w') as configfile:
                config.write(configfile)
                print(file_name)
