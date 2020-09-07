import tkinter as tk
from tkinter import ttk
import requests
from functools import partial
import threading
import math
import time
import tkinter.messagebox
import os


FONTFAMILY = 'Arial'
FONTSIZE = 14
FONTSIZE = 8
CONTENTBTEXT = 24
style_palette = []

CLBLTEXT = [
    'للمتابعة يرجى الضغط على أزرار القائمة الرئيسية',
    'لا شيء هنا إلى الآن تستطيع أن تحمل صوتيات وكتب'
]


def loop(news_content, scrollbar, style_palette_s):
    global style_palette
    style_palette = style_palette_s
    t2 = threading.Thread(target=files_update, args=(news_content, scrollbar,))
    t2.start()

def callback_enter(label_title, event):
    label_title.config(bg=style_palette[5])

def callback_leave(label_title, event):
    label_title.config(bg=style_palette[4])

def callback_press(file, news_content, scrollbar, dict, event):
    global style_palette
    result = tkinter.messagebox.askquestion('حذف', 'هل تريد حذفه؟')
    if result == 'yes':
        print('yes')
        if os.path.exists(dict):
            os.remove(dict)
            print(dict + " was deleted!")
        if os.path.exists("downloads/"+file):
            os.remove("downloads/"+file)
            loop(news_content, scrollbar, style_palette)
    else:
        pass

def files_update(news_content, scrollbar):
    news_content.delete("all")
    news_content_title = tk.Label(news_content, text='التحميل', fg=style_palette[1], bg=style_palette[4], font=(FONTFAMILY, CONTENTBTEXT))
    news_content.create_window(0, 0, anchor='nw', window=news_content_title, width=477)
    files = os.listdir('downloads/')
    label_title = list()
    label_progress = list()
    progressBar = list()
    iq = 50
    i = 0
    scroll_q = 0
    if len(files) > 0:
        for file in files:
            with open('downloads/'+file, 'r') as f:
                dict = f.readlines()
            total = convert_size(int(dict[2].replace('total = ', '')))
            done = convert_size(int(dict[4].replace('done = ', '')))
            progress = str(total) + '/' + str(done)
            label_title.append(tk.Label(news_content, text=dict[1].split("/")[-1], bd=0, bg=style_palette[4], fg=style_palette[1], font=(FONTFAMILY, FONTSIZE)))
            label_progress.append(tk.Label(news_content, text=progress, bd=0, bg=style_palette[4], fg=style_palette[1], font=(FONTFAMILY, FONTSIZE)))
            progressBar.append(ttk.Progressbar(news_content, orient='horizontal', length=200, mode='determinate', variable=100))
            news_content.create_window(265, iq, anchor='nw', window=label_title[-1], width=300, height=50)
            news_content.create_window(5, iq, anchor='nw', window=label_progress[-1], width=100, height=50)
            news_content.create_window(110, iq, anchor='nw', window=progressBar[-1], width=150, height=50)
            iq += 70
            scroll_q = iq
            i += 1
            persent = int(dict[3].replace('percent = ', ''))
            progressBar[-1].config(value=persent)
            label_title[-1].bind("<Enter>", partial(callback_enter, label_title[-1]))
            label_title[-1].bind("<Leave>", partial(callback_leave, label_title[-1]))
            label_title[-1].bind("<Button-1>", partial(callback_press, file, news_content, scrollbar, dict[1].replace('name = ', '').replace('\n','')))
        progressBar.reverse()
        label_progress.reverse()
        # progressbar_q = int(progressBar[0].winfo_name().split('progressbar', 1)[-1])
        if scroll_q < news_content.winfo_height():
            scroll_q = news_content.winfo_height()
        else:
            scroll_q = scroll_q + 30
        news_content.config(yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, scroll_q))
        scrollbar.config(command=news_content.yview)
        while news_content.winfo_exists():
            bar = -1
            files = os.listdir('downloads/')
            for file in files:
                with open('downloads/' + file, 'r') as f:
                    dict = f.readlines()
                persent = int(dict[3].replace('percent = ', ''))
                total = convert_size(int(dict[2].replace('total = ', '')))
                done = convert_size(int(dict[4].replace('done = ', '')))
                progress = str(total) + '/' + str(done)
                # try:
                progressBar[bar].config(value=persent)
                label_progress[bar].config(text=progress)
                # except:
                #     pass
                bar -= 1
            time.sleep(1.0)
    else:
        news_content_label = tk.Label(news_content, text=CLBLTEXT[1], fg=style_palette[0], bg=style_palette[4], font=(FONTFAMILY, 16))
        news_content.create_window(0, 50, anchor='nw', window=news_content_label, width=477)


def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])
