import tkinter as tk
from tkinter import ttk
from tkinter.tix import *
from functools import partial
import threading
import time
import math
import os
import sys
import pafy
import webbrowser

import my_ttk_style
import my_audio_parsing as audPse
import my_video_parsing as vidPse
from my_videoplayer import player as vidPlayer
import my_books_parsing as bkPse
import my_les_books_parsing as lesBkPse
import my_downloads_page as dPage
import my_dwnld as dwnld

# gui window's settings
WINDOWGEOMETRY = '800x500'
HEIGHT = 500
WIDTH = 800
MENUBTNHG = 26
MENUBTNWH = 180
MINHEIGHT = 500
MINWIDTH = 800
FONTFAMILY = 'Arial'
FONTSIZE = 14
FONTSIZEBTN = 12
CONTENTBTEXT = 24
MENUTEXTSIZE = 16

back_count = 0
# ----  TEXTS  ------------------------------------
NAME = 'عبدالرحمن بن عبدالعزيز بن صالح بن محمد العقل'
CLBLTEXT = [
    'للمتابعة يرجى الضغط على أزرار القائمة الرئيسية'
]
MTEXT = [
    'المشاهدات ',
    'الصوتيات ',
    'الكتب ',
    'تفريغات الدروس ',
    'الإعدادات ',
    'التحميل '
]
ERRORS = [
    'مشاكل الإنترنت ، تحقق من الاتصال الخاص بك من فضلك'
]
SOCIAL_LINK = [
    'https://twitter.com/AbduRahmanAlAql',
    'https://www.facebook.com/Dr.abdulrahman.alaql',
    'https://www.youtube.com/channel/UCjm4etMQLqz_ybEJ83eI83w',
    'http://abdulrahmanalaql.com/'
]
# -------------------------------------------------
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


root = tk.Tk()
root.geometry(WINDOWGEOMETRY)
root.minsize(MINWIDTH, MINHEIGHT)
root.title('abdulrahmanalaql.com')
root.iconbitmap('icon.ico')
canvas = tk.Canvas(root)
canvas.pack(fill='both')

# system default style changing
# GUI backgrounds changing
style_palette = my_ttk_style.Style()

frame_top = tk.Frame(canvas, bg=style_palette[3], height=60)
frame_top.pack(side=tk.TOP, fill=tk.X)
frame_left = tk.Frame(canvas, bg=style_palette[5])
frame_left.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH, anchor='nw')
frame_right = tk.Frame(canvas, bg=style_palette[5], width=200, height=2000)
frame_right.pack(side=tk.RIGHT, fill=tk.Y, expand=tk.NO, anchor='ne')

frame_right_menu = tk.Frame(frame_right, bg=style_palette[5])
frame_right_menu.place(x=10, y=10, height=300, width=180)

img_video = tk.PhotoImage(file="images/video.png")
nav_vd_btn = ttk.Button(frame_right_menu, text=MTEXT[0], image=img_video, compound='right', style="Menu.TButton")
nav_vd_btn.place(relx=0, rely=0.1, height=MENUBTNHG, width=MENUBTNWH)

img_audio = tk.PhotoImage(file="images/audio.png")
nav_aud_btn = ttk.Button(frame_right_menu, text=MTEXT[1], image=img_audio, compound='right', style="Menu.TButton")
nav_aud_btn.place(relx=0, rely=0.22, height=MENUBTNHG, width=MENUBTNWH)

img_book = tk.PhotoImage(file="images/book.png")
nav_bks_btn = ttk.Button(frame_right_menu, text=MTEXT[2], image=img_book, compound='right', style="Menu.TButton")
nav_bks_btn.place(relx=0, rely=0.34, height=MENUBTNHG, width=MENUBTNWH)

img_note = tk.PhotoImage(file="images/note.png")
nav_les_bks_btn = ttk.Button(frame_right_menu, text=MTEXT[3], image=img_note, compound='right', style="Menu.TButton")
nav_les_bks_btn.place(relx=0, rely=0.46, height=MENUBTNHG, width=MENUBTNWH)

img_download = tk.PhotoImage(file="images/load.png")
nav_dwnl_btn = ttk.Button(frame_right_menu, text=MTEXT[5], image=img_download, compound='right', style="Menu.TButton")
nav_dwnl_btn.place(relx=0, rely=0.70, height=MENUBTNHG, width=MENUBTNWH)

img_setting = tk.PhotoImage(file="images/settings.png")
nav_set_btn = ttk.Button(frame_right_menu, text=MTEXT[4], image=img_setting, compound='right', style="Menu.TButton")
nav_set_btn.place(relx=0, rely=0.82, height=MENUBTNHG, width=MENUBTNWH)

# icons
img_restart = tk.PhotoImage(file="images/restart.png")

# social icons
img_youtube = tk.PhotoImage(file="images/youtube.png")
img_twitter = tk.PhotoImage(file="images/twitter.png")
img_facebook = tk.PhotoImage(file="images/facebook.png")
img_site = tk.PhotoImage(file="images/site.png")

def browser_snd(url):
    webbrowser.open(url,new=1)

nav_s_fcb_btn = ttk.Button(frame_right_menu, image=img_facebook, command=partial(browser_snd, SOCIAL_LINK[1]))
nav_s_fcb_btn.place(x=35, rely=0.94)

nav_s_twr_btn = ttk.Button(frame_right_menu, image=img_twitter, command=partial(browser_snd, SOCIAL_LINK[0]))
nav_s_twr_btn.place(x=70, rely=0.94)

nav_s_ytb_btn = ttk.Button(frame_right_menu, image=img_youtube, command=partial(browser_snd, SOCIAL_LINK[2]))
nav_s_ytb_btn.place(x=105, rely=0.94)

nav_s_ins_btn = ttk.Button(frame_right_menu, image=img_site, command=partial(browser_snd, SOCIAL_LINK[3]))
nav_s_ins_btn.place(x=140, rely=0.94)
# -----------------------------------------
top_frame_l_cont = tk.Frame(frame_top, bg=style_palette[4], height=60, width=200)
top_frame_l_cont.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH, anchor='nw')
top_frame_r_cont = tk.Frame(frame_top, bg=style_palette[5], width=200, height=60)
top_frame_r_cont.pack(side=tk.RIGHT, fill=tk.Y, expand=tk.NO, anchor='ne')

top_label_main = tk.Label(top_frame_l_cont, text=NAME, fg=style_palette[2], bg=style_palette[3], font=(FONTFAMILY, FONTSIZE))
top_label_main.place(x=10, y=10, relwidth=0.83, height=40)

img_back = tk.PhotoImage(file="images/backspace.png")
back_main_btn = ttk.Button(top_frame_l_cont, text='  العودة ', image=img_back, compound='right', style='Back.TButton')
back_main_btn.place(relx=0.86, rely=0.0, width=100, relheight=1)
top_frame_right_canvas = tk.Canvas(top_frame_r_cont, bg=style_palette[5], highlightthickness=0)
top_frame_right_canvas.place(x=25, y=0, height=60, width=160)
top_frame_right_canvas_img = tk.PhotoImage(file="images/logo.png")  # The PhotoImage class can only read GIF and PGM/PPM
top_frame_right_canvas.create_image(0, 0, anchor='nw', image=top_frame_right_canvas_img)
# -----------------------------------------
scrollbar = ttk.Scrollbar(frame_left, orient=tk.VERTICAL, style='St.Vertical.TScrollbar')
scrollbar.pack(side=tk.LEFT, fill=tk.BOTH)

# --------------------------------------------
canvas2 = tk.Canvas(frame_left, bg=style_palette[4], highlightthickness=0)
canvas2.place(height=300, relwidth=1)
canvas2.pack(expand=True, fill=tk.BOTH)

# photo = tk.PhotoImage(file="Spin3.gif")
icon_folder = tk.PhotoImage(file="images/folder.png")
# photoLoad2 = tk.PhotoImage(file="Spin5.gif")
spin_white_list = ["images\spin_white\spin1.gif","images\spin_white\spin2.gif","images\spin_white\spin3.gif",
             "images\spin_white\spin4.gif","images\spin_white\spin5.gif","images\spin_white\spin6.gif",
             "images\spin_white\spin7.gif","images\spin_white\spin8.gif"]
spin_black_list = ["images\spin_black\spin1.png","images\spin_black\spin2.png","images\spin_black\spin3.png",
             "images\spin_black\spin4.png","images\spin_black\spin5.png","images\spin_black\spin6.png",
             "images\spin_black\spin7.png","images\spin_black\spin8.png"]

news_content = tk.Canvas(canvas2, bg=style_palette[4], highlightthickness=0, width=477)
news_content.pack(side='right', fill='y', expand='yes', anchor='ne', padx=8, pady=8)

news_content_label = tk.Label(news_content, text=CLBLTEXT[0], fg=style_palette[0], bg=style_palette[4], font=(FONTFAMILY, FONTSIZE))
news_content_label.place(relwidth=1,  height=50)




# -----------------------------------------

# -----------------------------------------
def resiseObj1(news_content,event):
    h = root.winfo_height() - 60
    if root.winfo_width() < 1000:
        w = root.winfo_width() - 250
    else:
        w = 750
    try:
        news_content.configure(width=w, height=h)
    except:
        pass

# -----------------------------------------
def back_fl_clearing():
    global back_count
    back_count = 0
    files = os.listdir('bklsn/')
    for f in files:
        os.remove('bklsn/' + f)
    with open('bklsn/back_listen.ini', 'w') as file:
        file.write('0')
        print('writed')
back_fl_clearing()


def btn_back_clicked():
    player_stoper()
    global back_count
    if back_count >= 1:
        back_count -= 1
        try:
            with open('bklsn/back_listen_video'+str(back_count)+'.ini', 'r') as file:
                btn_vid_next2(file.read())
                print('Success back_count is: ' + str(back_count))
                if back_count != 0:
                    back_count -= 1
                    return back_count
        except:
            pass
        try:
            with open('bklsn/back_listen_audio'+str(back_count)+'.ini', 'r') as file:
                btn_aud_next2(file.read())
                print('Success back_count is: ' + str(back_count))
                if back_count != 0:
                    back_count -= 1
                    return back_count
        except:
            pass
        try:
            with open('bklsn/back_listen_book'+str(back_count)+'.ini', 'r') as file:
                btn_bk_next2(file.read())
                print('Success back_count is: ' + str(back_count))
                if back_count != 0:
                    back_count -= 1
                    return back_count
        except:
            pass
        try:
            with open('bklsn/back_listen_note'+str(back_count)+'.ini', 'r') as file:
                btn_lsn_next2(file.read())
                print('Success back_count is: ' + str(back_count))
                if back_count != 0:
                    back_count -= 1
                    return back_count
        except:
            pass
        return back_count

# -----------------------------------------
# The menu buttons action
# 2. VIDEO
def btn_vid_clicked():
    t1 = threading.Thread(target=loadi)
    t2 = threading.Thread(target=btn_vid_parse)
    t1.start()
    t2.start()

def btn_vid_next2(page):
    t1 = threading.Thread(target=loadi)
    t2 = threading.Thread(target=btn_vid_next, args=(page,))
    t1.start()
    t2.start()

ggg = 0
def btn_vid_next(page):
    global back_count
    back_count += 1
    player_stoper()
    i = 0
    iq = 50
    scroll_q = 0
    button = list()
    label = list()
    try:
        l, a, vid, emp = vidPse.audio_folders(page)
        with open('bklsn/back_listen_video%s.ini'%(back_count), 'w') as configfile:
            configfile.write(page)
        clear_contentframe()
        news_content = tk.Canvas(canvas2, bg=style_palette[4], highlightthickness=0, width=560)
        news_content.pack(side='right', fill='y', expand='yes', anchor='ne', padx=8, pady=8)
        if vid == 1:
            global ggg
            ggg = 1
            news_content.pack(fill='both')
            vidLink = l[0]
            descr = a[0]
            curDate = emp
            descr_q = math.ceil(len(descr) / 450) * 30
            lbl_descr = tk.Label(canvas2, text=descr, justify='right', fg=style_palette[1], bg=style_palette[4],
                                 font=(FONTFAMILY, FONTSIZE), width=55)  # , wraplength=470
            videopanel = ttk.Frame(news_content)
            videopanel.configure(height=300, width=550)
            vidControl = tk.Frame(news_content, bg='#13171B')
            vidControl.configure(height=62, width=550)
            news_content.create_window(8, 10, anchor='w', window=lbl_descr)
            news_content.create_window(8, 160 + descr_q, anchor='w', window=videopanel)
            news_content.create_window(8, 335 + descr_q, anchor='w', window=vidControl)

            t1 = threading.Thread(target=loadingPic, args=(videopanel,))
            t1.start()
            with open('play_check/play_status.dll', 'w') as file:
                file.write('0')
            t2 = threading.Thread(target=vidPlayer,
                                  args=(vidLink, news_content, videopanel, vidControl, lbl_descr,))
            t2.start()
            def resiseObj(event):
                if root.winfo_width() < 1000:
                    w = root.winfo_width() - 250
                else:
                    w = 750
                if root.winfo_height() < 620:
                    h = root.winfo_height() - 200
                else:
                    h = 420
                posY = int((h - 300) / 2)
                if root.winfo_width() > 1000:
                    posX = int((root.winfo_width() - 1000))
                else:
                    posX = 0
                news_content.create_window(8 + posX, 10, anchor='w', window=lbl_descr)
                news_content.create_window(8 + posX, posY + 160 + descr_q, anchor='w', window=videopanel)
                news_content.create_window(8 + posX, (h - 300) + 335 + descr_q, anchor='w', window=vidControl)
                videopanel.configure(width=w, height=h)
                vidControl.configure(width=w)
                lbl_descr.configure(width=int(w / 10))
            resiseObj("<Configure>")
            news_content.bind("<Configure>", resiseObj)
        else:
            news_content_label = tk.Label(news_content, text=MTEXT[0], fg=style_palette[1], bg=style_palette[4], font=(FONTFAMILY, CONTENTBTEXT))
            news_content.create_window(0, 0, anchor='nw', window=news_content_label, width=560)
            if l[0] != '0':
                for x in a:
                    page = l[i]
                    button.append(
                        ttk.Button(news_content, text=x, command=partial(btn_vid_next2, page), style="Content.TButton"))
                    label.append(tk.Label(canvas2, image=icon_folder, height=10, width=10, bd=0, bg=style_palette[4]))
                    news_content.create_window(0, iq, anchor='nw', window=button[-1], width=530)
                    news_content.create_window(535, iq, anchor='nw', window=label[-1], width=25, height=40)
                    i += 1
                    iq += 50
                    scroll_q = iq
            elif l[0] == '0':
                news_content_error = tk.Label(news_content, text=a[0], fg=style_palette[1], bg=style_palette[4],
                                              font=(FONTFAMILY, CONTENTBTEXT))
                news_content.create_window(0, iq, anchor='nw', window=news_content_error, width=450)
    except:
        time.sleep(0.1)
        clear_contentframe()
        news_content = tk.Canvas(canvas2, bg=style_palette[4], highlightthickness=0)
        news_content.pack(side='right', fill='both', expand='yes', anchor='nw', padx=8, pady=8)
        news_content_label = tk.Label(news_content, text=ERRORS[0], fg='orange', bg=style_palette[4], font=(FONTFAMILY, MENUTEXTSIZE))
        news_content_button = ttk.Button(news_content, text='  إعادة ', command=partial(btn_vid_next2, page,), image=img_restart, compound='right', style="Content.Attention.Player.TButton")
        news_content.create_window(0, 0, anchor='nw', window=news_content_label, width=477)
        news_content.create_window(200, 100, anchor='nw', window=news_content_button, width=150, height=60)
    news_content.config(yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, scroll_q + 30))
    scrollbar.config(command=news_content.yview)
    root.bind("<MouseWheel>", partial(_on_mousewheel, news_content,))



def btn_vid_parse():
    back_fl_clearing()
    page = 'catsmktba-6.html'
    global back_count
    with open('bklsn/back_listen_video%s.ini'%(back_count), 'w') as configfile:
        configfile.write(page)
    player_stoper()
    y = 0
    i = 0
    iq = 50
    scroll_q = 0
    try:
        l, a, vid, emp = vidPse.audio_folders(page)
        button = list()
        label = list()
        clear_contentframe()
        news_content = tk.Canvas(canvas2, bg=style_palette[4], highlightthickness=0, width=560)
        news_content.pack(side='right', fill='y', expand='yes', anchor='ne', padx=8, pady=8)
        news_content_label = tk.Label(news_content, text=MTEXT[0], fg=style_palette[1], bg=style_palette[4], font=(FONTFAMILY, CONTENTBTEXT))
        news_content.create_window(0, 0, anchor='nw', window=news_content_label, width=560)
        if l[0] != '0':
            for x in a:
                page = l[i]
                button.append(ttk.Button(news_content, text=x, command=partial(btn_vid_next2, page), style="Content.TButton"))
                label.append(tk.Label(canvas2, image=icon_folder, height=10, width=10, bd=0, bg=style_palette[4]))
                news_content.create_window(0, iq, anchor='nw', window=button[-1], width=530)
                news_content.create_window(535, iq, anchor='nw', window=label[-1], width=25, height=40)
                y = y + 0.1
                i += 1
                iq += 50
                scroll_q = iq
        elif l[0] == '0':
            news_content_error = tk.Label(news_content, text=a[0], fg=style_palette[1], bg=style_palette[4],
                                          font=(FONTFAMILY, CONTENTBTEXT))
            news_content.create_window(0, iq, anchor='nw', window=news_content_error, width=450)
    except:
        time.sleep(0.1)
        clear_contentframe()
        news_content = tk.Canvas(canvas2, bg=style_palette[4], highlightthickness=0)
        news_content.pack(side='right', fill='both', expand='yes', anchor='nw', padx=8, pady=8)
        news_content_label = tk.Label(news_content, text=ERRORS[0], fg='orange', bg=style_palette[4], font=(FONTFAMILY, MENUTEXTSIZE))
        news_content_button = ttk.Button(news_content, text='  إعادة ', command=partial(btn_vid_next2, page,), image=img_restart, compound='right', style="Content.Attention.Player.TButton")
        news_content.create_window(0, 0, anchor='nw', window=news_content_label, width=477)
        news_content.create_window(200, 100, anchor='nw', window=news_content_button, width=150, height=60)
    news_content.config(yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, scroll_q + 30))
    scrollbar.config(command=news_content.yview)
    root.bind("<MouseWheel>", partial(_on_mousewheel, news_content,))

def _on_mousewheel(news_content, event):
    news_content.yview_scroll(int(-1*(event.delta/120)), "units")



def btn_aud_next2(page):
    t1 = threading.Thread(target=loadi)
    t2 = threading.Thread(target=btn_aud_next, args=(page,))
    t1.start()
    t2.start()


def loadingPic(place):
    photo = tk.PhotoImage(file=spin_white_list[0])
    label = tk.Label(place, image=photo, bd=0)
    label.place(relx=0.45, rely=0.4)
    giflist = []
    for imagefile in spin_white_list:
        photo = tk.PhotoImage(file=imagefile)
        giflist.append(photo)
    for k in range(0, 1000):
        for gif in giflist:
            try:
                label.config(image=gif)
                time.sleep(0.1)
            except:
                pass

def loadi():
    clear_contentframe()
    photo = tk.PhotoImage(file=spin_black_list[0])
    width = photo.width()
    height = photo.height()
    canvas3 = tk.Canvas(canvas2, width=width, height=height, highlightthickness=0, bg=style_palette[4])
    canvas3.pack(side='right', expand='yes')
    giflist = []
    for imagefile in spin_black_list:
        photo = tk.PhotoImage(file=imagefile)
        giflist.append(photo)
    for k in range(0, 1000):
        for gif in giflist:
            try:
                canvas3.delete(tk.ALL)
                canvas3.create_image(width / 2.0, height / 2.0, image=gif)
                canvas3.update()
                time.sleep(0.1)
            except:
                pass


def clear_contentframe():
    print('the content frame was clear!')
    try:
        for widget in canvas2.winfo_children():
            widget.destroy()
    except:
        pass

def btn_aud_next(page):
    global back_count
    back_count += 1
    player_stoper()
    i = 0
    iq = 50
    scroll_q = 0
    button = list()
    label = list()
    try:
        l, a, mp3, emp, emp2, emp3 = audPse.audio_folders(page)
        with open('bklsn/back_listen_audio%s.ini'%(back_count), 'w') as configfile:
            configfile.write(page)
        clear_contentframe()
        news_content = tk.Canvas(canvas2, bg=style_palette[4], highlightthickness=0, width=560)
        news_content.pack(side='right', fill='y', expand='yes', anchor='ne', padx=8, pady=8)
        if mp3 == 1:
            mp3Link = l
            descr = a
            author = emp
            curDate = emp2
            last_chars = emp3
            descr_q = math.ceil(len(descr) / 450)
            btn_aud_dwnl = ttk.Button(news_content, text='التحميل', style="Content.TButton",
                                      command=partial(btn_dwnld, mp3Link, last_chars))
            lbl_descr = tk.Label(canvas2, text=descr, justify='right', fg=style_palette[1], bg=style_palette[4],
                                 font=(FONTFAMILY, FONTSIZE), wraplength=470)
            lbl_author = tk.Label(canvas2, text=author, fg=style_palette[1], bg=style_palette[4], font=(FONTFAMILY, FONTSIZE))
            lbl_date = tk.Label(canvas2, text=curDate, justify='right', fg=style_palette[1], bg=style_palette[4],
                                font=(FONTFAMILY, FONTSIZE))
            news_content.create_window(0, 0, anchor='nw', window=lbl_descr, width=500)
            news_content.create_window(0, 50 + (descr_q * 30), anchor='nw', window=lbl_author, width=500)
            news_content.create_window(360, 100 + (descr_q * 30), anchor='nw', window=lbl_date, width=140)
            news_content.create_window(0, 170 + (descr_q * 30), anchor='nw', window=btn_aud_dwnl, width=100)
        else:
            news_content_label = tk.Label(news_content, text=MTEXT[1], fg=style_palette[1], bg=style_palette[4], font=(FONTFAMILY, CONTENTBTEXT))
            news_content.create_window(0, 0, anchor='nw', window=news_content_label, width=477)
            if l[0] != '0':
                for x in a:
                    page = l[i]
                    button.append(
                        ttk.Button(news_content, text=x, command=partial(btn_aud_next2, page), style="Content.TButton"))
                    label.append(tk.Label(canvas2, image=icon_folder, height=10, width=10, bd=0, bg=style_palette[4]))
                    news_content.create_window(0, iq, anchor='nw', window=button[-1], width=530)
                    news_content.create_window(535, iq, anchor='nw', window=label[-1], width=25, height=40)
                    i += 1
                    iq += 50
                    scroll_q = iq
            elif l[0] == '0':
                news_content_error = tk.Label(news_content, text=a[0], fg=style_palette[1], bg=style_palette[4],
                                              font=(FONTFAMILY, CONTENTBTEXT))
                news_content.create_window(0, iq, anchor='nw', window=news_content_error, width=450)
    except:
        time.sleep(0.1)
        clear_contentframe()
        news_content = tk.Canvas(canvas2, bg=style_palette[4], highlightthickness=0)
        news_content.pack(side='right', fill='both', expand='yes', anchor='nw', padx=8, pady=8)
        news_content_label = tk.Label(news_content, text=ERRORS[0], fg='orange', bg=style_palette[4], font=(FONTFAMILY, MENUTEXTSIZE))
        news_content_button = ttk.Button(news_content, text='  إعادة ', command=partial(btn_aud_next2, page,), image=img_restart, compound='right', style="Content.Attention.Player.TButton")
        news_content.create_window(0, 0, anchor='nw', window=news_content_label, width=477)
        news_content.create_window(200, 100, anchor='nw', window=news_content_button, width=150, height=60)
    news_content.config(yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, scroll_q + 30))
    scrollbar.config(command=news_content.yview)
    root.bind("<MouseWheel>", partial(_on_mousewheel, news_content,))


def btn_aud_clicked():
    t1 = threading.Thread(target=loadi)
    t2 = threading.Thread(target=btn_aud_parse)
    t1.start()
    t2.start()


def btn_aud_parse():
    page = 'catsmktba-222.html'
    back_fl_clearing()
    global back_count
    with open('bklsn/back_listen_audio%s.ini'%(back_count), 'w') as configfile:
        configfile.write(page)
    player_stoper()
    y = 0
    i = 0
    iq = 50
    scroll_q = 0
    try:
        l, a, mp3, emp, emp2, emp3 = audPse.audio_folders(page)
        button = list()
        label = list()
        clear_contentframe()
        news_content = tk.Canvas(canvas2, bg=style_palette[4], highlightthickness=0, width=560)
        news_content.pack(side='right', fill='y', expand='yes', anchor='ne', padx=8, pady=8)
        news_content_label = tk.Label(news_content, text=MTEXT[1], fg=style_palette[1], bg=style_palette[4], font=(FONTFAMILY, CONTENTBTEXT))
        news_content.create_window(0, 0, anchor='nw', window=news_content_label, width=560)
        if l[0] != '0':
            for x in a:
                page = l[i]
                button.append(
                    ttk.Button(news_content, text=x, command=partial(btn_aud_next2, page), style="Content.TButton"))
                label.append(tk.Label(canvas2, image=icon_folder, height=10, width=10, bd=0, bg=style_palette[4]))
                news_content.create_window(0, iq, anchor='nw', window=button[-1], width=530)
                news_content.create_window(535, iq, anchor='nw', window=label[-1], width=25, height=40)
                y = y + 0.1
                i += 1
                iq += 50
            news_content.config(yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, scroll_q+30))
        elif l[0] == '0':
            news_content_error = tk.Label(news_content, text=a[0], fg=style_palette[1], bg=style_palette[4],
                                          font=(FONTFAMILY, CONTENTBTEXT))
            news_content.create_window(0, iq, anchor='nw', window=news_content_error, width=450)
    except:
        time.sleep(0.1)
        clear_contentframe()
        news_content = tk.Canvas(canvas2, bg=style_palette[4], highlightthickness=0)
        news_content.pack(side='right', fill='both', expand='yes', anchor='nw', padx=8, pady=8)
        news_content_label = tk.Label(news_content, text=ERRORS[0], fg='orange', bg=style_palette[4], font=(FONTFAMILY, MENUTEXTSIZE))
        news_content_button = ttk.Button(news_content, text='  إعادة ', command=partial(btn_aud_next2, page,), image=img_restart, compound='right', style="Content.Attention.Player.TButton")
        news_content.create_window(0, 0, anchor='nw', window=news_content_label, width=477)
        news_content.create_window(200, 100, anchor='nw', window=news_content_button, width=150, height=60)
    news_content.config(yscrollcommand=scrollbar.set, scrollregion=(0, 0, 500, 500))
    scrollbar.config(command=news_content.yview)
    root.bind("<MouseWheel>", partial(_on_mousewheel, news_content,))


def btn_dwnld(page, last_chars):
    dwnld.saveAs(page, last_chars)
# -----------------------------------------

# 6. BOOKS
def btn_bks_clicked():
    t1 = threading.Thread(target=loadi)
    t2 = threading.Thread(target=btn_bks_parse)
    t1.start()
    t2.start()

def btn_bk_next2(page):
    t1 = threading.Thread(target=loadi)
    t2 = threading.Thread(target=btn_bk_next, args=(page,))
    t1.start()
    t2.start()

def btn_bks_parse():
    back_fl_clearing()
    page = 'catsmktba-9.html'
    global back_count
    with open('bklsn/back_listen_book%s.ini'%(back_count), 'w') as configfile:
        configfile.write(page)
    y = 0
    i = 0
    iq = 50
    scroll_q = 0
    try:
        l, a, mp3, emp, emp2, emp3 = bkPse.book_folders(page)
        clear_contentframe()
        button = list()
        label = list()
        news_content = tk.Canvas(canvas2, bg=style_palette[4], highlightthickness=0, width=560)
        news_content.pack(side='right', fill='y', expand='yes', anchor='ne', padx=8, pady=8)
        if l[0] != '0':
            for x in a:
                page = l[i]
                button.append(ttk.Button(news_content, text=x, command=partial(btn_bk_next2, page), style="Content.TButton"))
                label.append(tk.Label(canvas2, image=icon_folder, height=10, width=10, bd=0, bg=style_palette[4]))
                news_content.create_window(0, iq, anchor='nw', window=button[-1], width=530)
                news_content.create_window(535, iq, anchor='nw', window=label[-1], width=25, height=40)
                y = y + 0.1
                i += 1
                iq += 50
        elif l[0] == '0':
            news_content_error = tk.Label(news_content, text=a[0], fg=style_palette[1], bg=style_palette[4],
                                          font=(FONTFAMILY, CONTENTBTEXT))
            news_content.create_window(0, iq, anchor='nw', window=news_content_error, width=450)
        news_content_label = tk.Label(news_content, text=MTEXT[2], fg=style_palette[1], bg=style_palette[4], font=(FONTFAMILY, CONTENTBTEXT))
        news_content.create_window(0, 0, anchor='nw', window=news_content_label, width=477)
        news_content.config(yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, scroll_q+30))
    except:
        time.sleep(0.1)
        clear_contentframe()
        news_content = tk.Canvas(canvas2, bg=style_palette[4], highlightthickness=0)
        news_content.pack(side='right', fill='both', expand='yes', anchor='nw', padx=8, pady=8)
        news_content_label = tk.Label(news_content, text=ERRORS[0], fg='orange', bg=style_palette[4], font=(FONTFAMILY, MENUTEXTSIZE))
        news_content_button = ttk.Button(news_content, text='  إعادة ', command=partial(btn_bk_next2, page,), image=img_restart, compound='right', style="Content.Attention.Player.TButton")
        news_content.create_window(0, 0, anchor='nw', window=news_content_label, width=477)
        news_content.create_window(200, 100, anchor='nw', window=news_content_button, width=150, height=60)
    news_content.config(yscrollcommand=scrollbar.set, scrollregion=(0, 0, 500, 500))
    scrollbar.config(command=news_content.yview)
    root.bind("<MouseWheel>", partial(_on_mousewheel, news_content,))


def btn_bk_next(page):
    global back_count
    back_count += 1
    i = 0
    iq = 50
    scroll_q = 0
    button = list()
    label = list()
    try:
        l, a, bks, emp, emp2, emp3 = bkPse.book_folders(page)
        with open('bklsn/back_listen_book%s.ini'%(back_count), 'w') as configfile:
            configfile.write(page)
        clear_contentframe()
        news_content = tk.Canvas(canvas2, bg=style_palette[4], highlightthickness=0, width=560)
        news_content.pack(side='right', fill='y', expand='yes', anchor='ne', padx=8, pady=8)
        if bks == 1:
            mp3Link = l
            descr = 'اسم الكتاب: ' + a
            author = 'المؤالف: ' + emp
            curDate = emp2
            last_chars = emp3
            descr_q = math.ceil(len(descr)/450)
            btn_aud_dwnl = ttk.Button(news_content, text='التحميل', style="Content.TButton", command=partial(btn_dwnld, mp3Link, last_chars))
            lbl_descr = tk.Label(canvas2, text=descr, justify='right', fg=style_palette[1], bg=style_palette[4], font=(FONTFAMILY, FONTSIZE), wraplength=470)
            lbl_author = tk.Label(canvas2, text=author, fg=style_palette[1], bg=style_palette[4], font=(FONTFAMILY, FONTSIZE))
            lbl_date = tk.Label(canvas2, text=curDate, justify='right', fg=style_palette[1], bg=style_palette[4], font=(FONTFAMILY, FONTSIZE))
            news_content.create_window(0, 0, anchor='nw', window=lbl_descr, width=500)
            news_content.create_window(0, 50 + (descr_q * 30), anchor='nw', window=lbl_author, width=500)
            news_content.create_window(360, 100 + (descr_q * 30), anchor='nw', window=lbl_date, width=140)
            news_content.create_window(0, 170 + (descr_q * 30), anchor='nw', window=btn_aud_dwnl, width=100)
        else:
            news_content_label = tk.Label(news_content, text=MTEXT[2], fg=style_palette[1], bg=style_palette[4], font=(FONTFAMILY, CONTENTBTEXT))
            news_content.create_window(0, 0, anchor='nw', window=news_content_label, width=477)
            if l[0] != '0':
                for x in a:
                    page = l[i]
                    button.append(ttk.Button(news_content, text=x, command=partial(btn_bk_next2, page), style="Content.TButton"))
                    label.append(tk.Label(canvas2, image=icon_folder, height=10, width=10, bd=0, bg=style_palette[4]))
                    news_content.create_window(0, iq, anchor='nw', window=button[-1], width=530)
                    news_content.create_window(535, iq, anchor='nw', window=label[-1], width=25, height=40)
                    i += 1
                    iq += 50
                    scroll_q = iq
            elif l[0] == '0':
                news_content_error = tk.Label(news_content, text=a[0], fg=style_palette[1], bg=style_palette[4],
                                              font=(FONTFAMILY, CONTENTBTEXT))
                news_content.create_window(0, iq, anchor='nw', window=news_content_error, width=450)
            news_content_label = tk.Label(news_content, text=MTEXT[2], fg=style_palette[1], bg=style_palette[4], font=(FONTFAMILY, CONTENTBTEXT))
            news_content.create_window(0, 0, anchor='nw', window=news_content_label, width=477)
    except:
        time.sleep(0.1)
        clear_contentframe()
        news_content = tk.Canvas(canvas2, bg=style_palette[4], highlightthickness=0)
        news_content.pack(side='right', fill='both', expand='yes', anchor='nw', padx=8, pady=8)
        news_content_label = tk.Label(news_content, text=ERRORS[0], fg='orange', bg=style_palette[4], font=(FONTFAMILY, MENUTEXTSIZE))
        news_content_button = ttk.Button(news_content, text='  إعادة ', command=partial(btn_bk_next2, page,), image=img_restart, compound='right', style="Content.Attention.Player.TButton")
        news_content.create_window(0, 0, anchor='nw', window=news_content_label, width=477)
        news_content.create_window(200, 100, anchor='nw', window=news_content_button, width=150, height=60)
    news_content.config(yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, scroll_q+30))
    scrollbar.config(command=news_content.yview)
    root.bind("<MouseWheel>", partial(_on_mousewheel, news_content,))


# -----------------------------------------
# 7. LESSON BOOKS
def btn_les_bks_clicked():
    t1 = threading.Thread(target=loadi)
    t2 = threading.Thread(target=btn_les_bks_parse)
    t1.start()
    t2.start()

def btn_lsn_next2(page):
    t1 = threading.Thread(target=loadi)
    t2 = threading.Thread(target=btn_lsn_next, args=(page,))
    t1.start()
    t2.start()


def btn_les_bks_parse():
    back_fl_clearing()
    page = 'catsmktba-232.html'
    global back_count
    with open('bklsn/back_listen_note%s.ini'%(back_count), 'w') as configfile:
        configfile.write(page)
    y = 0
    i = 0
    iq = 50
    scroll_q = 0
    try:
        l, a, mp3, emp, emp2, emp3 = lesBkPse.book_folders(page)
        clear_contentframe()
        button = list()
        label = list()
        news_content = tk.Canvas(canvas2, bg=style_palette[4], highlightthickness=0, width=560)
        news_content.pack(side='right', fill='y', expand='yes', anchor='ne', padx=8, pady=8)
        if l[0] != '0':
            for x in a:
                page = l[i]
                button.append(ttk.Button(news_content, text=x, command=partial(btn_lsn_next2, page,), style="Content.TButton"))
                label.append(tk.Label(canvas2, image=icon_folder, height=10, width=10, bd=0, bg=style_palette[4]))
                news_content.create_window(0, iq, anchor='nw', window=button[-1], width=530)
                news_content.create_window(535, iq, anchor='nw', window=label[-1], width=25, height=40)
                y = y + 0.1
                i += 1
                iq += 50
        elif l[0] == '0':
            news_content_error = tk.Label(news_content, text=a[0], fg=style_palette[1], bg=style_palette[4],
                                          font=(FONTFAMILY, CONTENTBTEXT))
            news_content.create_window(0, iq, anchor='nw', window=news_content_error, width=450)
        news_content_label = tk.Label(news_content, text=MTEXT[3], fg=style_palette[1], bg=style_palette[4], font=(FONTFAMILY, CONTENTBTEXT))
        news_content.create_window(0, 0, anchor='nw', window=news_content_label, width=477)
    except:
        time.sleep(0.1)
        clear_contentframe()
        news_content = tk.Canvas(canvas2, bg=style_palette[4], highlightthickness=0)
        news_content.pack(side='right', fill='both', expand='yes', anchor='nw', padx=8, pady=8)
        news_content_label = tk.Label(news_content, text=ERRORS[0], fg='orange', bg=style_palette[4], font=(FONTFAMILY, MENUTEXTSIZE))
        news_content_button = ttk.Button(news_content, text='  إعادة ', command=partial(btn_lsn_next2, page,), image=img_restart, compound='right', style="Content.Attention.Player.TButton")
        news_content.create_window(0, 0, anchor='nw', window=news_content_label, width=477)
        news_content.create_window(200, 100, anchor='nw', window=news_content_button, width=150, height=60)
    news_content.config(yscrollcommand=scrollbar.set, scrollregion=(0, 0, 500, 500))
    scrollbar.config(command=news_content.yview)
    root.bind("<MouseWheel>", partial(_on_mousewheel, news_content,))


def btn_lsn_next(page):
    global back_count
    back_count += 1
    i = 0
    iq = 50
    scroll_q = 0
    button = list()
    label = list()
    try:
        l, a, bks, emp, emp2, emp3 = lesBkPse.book_folders(page)
        with open('bklsn/back_listen_note%s.ini'%(back_count), 'w') as configfile:
            configfile.write(page)
        clear_contentframe()
        news_content = tk.Canvas(canvas2, bg=style_palette[4], highlightthickness=0, width=560)
        news_content.pack(side='right', fill='y', expand='yes', anchor='ne', padx=8, pady=8)
        if bks == 1:
            mp3Link = l
            descr = a
            author = emp
            curDate = emp2
            last_chars = emp3
            descr_q = math.ceil(len(descr)/450)
            btn_aud_dwnl = ttk.Button(news_content, text='التحميل', style="Content.TButton", command=partial(btn_dwnld, mp3Link, last_chars))
            lbl_descr = tk.Label(canvas2, text=descr, justify='right', fg=style_palette[1], bg=style_palette[4], font=(FONTFAMILY, FONTSIZE), wraplength=470)
            lbl_author = tk.Label(canvas2, text=author, fg=style_palette[1], bg=style_palette[4], font=(FONTFAMILY, FONTSIZE))
            lbl_date = tk.Label(canvas2, text=curDate, justify='right', fg=style_palette[1], bg=style_palette[4], font=(FONTFAMILY, FONTSIZE))
            news_content.create_window(0, 0, anchor='nw', window=lbl_descr, width=500)
            news_content.create_window(0, 50 + (descr_q * 30), anchor='nw', window=lbl_author, width=500)
            news_content.create_window(360, 100 + (descr_q * 30), anchor='nw', window=lbl_date, width=140)
            news_content.create_window(0, 170 + (descr_q * 30), anchor='nw', window=btn_aud_dwnl, width=100)
        else:
            if l[0] != '0':
                for x in a:
                    page = l[i]
                    button.append(ttk.Button(news_content, text=x, command=partial(btn_lsn_next2, page), style="Content.TButton"))
                    label.append(tk.Label(canvas2, image=icon_folder, height=10, width=10, bd=0, bg=style_palette[4]))
                    news_content.create_window(0, iq, anchor='nw', window=button[-1], width=530)
                    news_content.create_window(535, iq, anchor='nw', window=label[-1], width=25, height=40)
                    i += 1
                    iq += 50
                    scroll_q = iq
                    news_content_label = tk.Label(news_content, text=MTEXT[3], fg=style_palette[1], bg=style_palette[4], font=(FONTFAMILY, CONTENTBTEXT))
                    news_content.create_window(0, 0, anchor='nw', window=news_content_label, width=477)
            elif l[0] == '0':
                news_content_error = tk.Label(news_content, text=a[0], fg=style_palette[1], bg=style_palette[4],
                                              font=(FONTFAMILY, CONTENTBTEXT))
                news_content.create_window(0, iq, anchor='nw', window=news_content_error, width=450)
    except:
        time.sleep(0.1)
        clear_contentframe()
        news_content = tk.Canvas(canvas2, bg=style_palette[4], highlightthickness=0)
        news_content.pack(side='right', fill='both', expand='yes', anchor='nw', padx=8, pady=8)
        news_content_label = tk.Label(news_content, text=ERRORS[0], fg='orange', bg=style_palette[4], font=(FONTFAMILY, MENUTEXTSIZE))
        news_content_button = ttk.Button(news_content, text='  إعادة ', command=partial(btn_lsn_next2, page,), image=img_restart, compound='right', style="Content.Attention.Player.TButton")
        news_content.create_window(0, 0, anchor='nw', window=news_content_label, width=477)
        news_content.create_window(200, 100, anchor='nw', window=news_content_button, width=150, height=60)
    news_content.config(yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, scroll_q+30))
    scrollbar.config(command=news_content.yview)
    root.bind("<MouseWheel>", partial(_on_mousewheel, news_content,))


# -----------------------------------------
# 8. DOWNLOADS
def btn_dwl_clicked():
    player_stoper()
    clear_contentframe()
    news_content = tk.Canvas(canvas2, bg=style_palette[4], highlightthickness=0)
    news_content.pack(side='right', expand='yes', anchor='ne', padx=8, pady=8)
    dPage.loop(news_content, scrollbar, style_palette)
    root.bind("<Configure>", partial(resiseObj1, news_content))
    root.bind("<MouseWheel>", partial(_on_mousewheel, news_content,))




# -----------------------------------------
# 9 Settings
style_img_1 = tk.PhotoImage(file="images/style/style_1.png")
style_img_2 = tk.PhotoImage(file="images/style/style_2.png")
style_img_3 = tk.PhotoImage(file="images/style/style_3.png")
style_img_4 = tk.PhotoImage(file="images/style/style_4.png")
style_img_5 = tk.PhotoImage(file="images/style/style_5.png")

style_txt_1 = 'شكل 1'
style_txt_2 = 'شكل 2'
style_txt_3 = 'شكل 3'
style_txt_4 = 'شكل 4'
style_txt_5 = 'شكل 5'

def btn_set_clicked():
    player_stoper()
    clear_contentframe()
    news_content = tk.Canvas(canvas2, bg=style_palette[4], highlightthickness=0, width=477)
    news_content.pack(side='right', expand='yes', anchor='ne', padx=8, pady=8)
    news_content_label = tk.Label(news_content, text=MTEXT[4], fg=style_palette[1], bg=style_palette[4], font=(FONTFAMILY, CONTENTBTEXT))
    news_content_label_bg = tk.Label(news_content, text='اختر الشكل للنظام', fg=style_palette[1], bg=style_palette[4], font=(FONTFAMILY, MENUTEXTSIZE))

    news_content_button1 = ttk.Button(news_content, text=style_txt_1, image=style_img_1, compound='top', command=partial(message_style, '1',))
    news_content_button2 = ttk.Button(news_content, text=style_txt_2, image=style_img_2, compound='top', command=partial(message_style, '2',))
    news_content_button3 = ttk.Button(news_content, text=style_txt_3, image=style_img_3, compound='top', command=partial(message_style, '3',))
    news_content_button4 = ttk.Button(news_content, text=style_txt_4, image=style_img_4, compound='top', command=partial(message_style, '4',))
    news_content_button5 = ttk.Button(news_content, text=style_txt_5, image=style_img_5, compound='top', command=partial(message_style, '5',))

    news_content.create_window(0, 0, anchor='nw', window=news_content_label, width=477)
    news_content.create_window(0, 60, anchor='nw', window=news_content_label_bg, width=477)
    news_content.create_window(0, 100, anchor='nw', window=news_content_button1)
    news_content.create_window(100, 100, anchor='nw', window=news_content_button2)
    news_content.create_window(200, 100, anchor='nw', window=news_content_button3)
    news_content.create_window(300, 100, anchor='nw', window=news_content_button4)
    news_content.create_window(400, 100, anchor='nw', window=news_content_button5)

    root.bind("<Configure>", partial(resiseObj1, news_content))



def message_style(i):
    result = tkinter.messagebox.askquestion('تغيير الشكل', 'هل تريد تغيير الشكل؟')
    if result == 'yes':
        with open('style.dll', 'w') as file:
            file.write(i)
        print(i)
        result2 = tkinter.messagebox.askquestion('تغيير الشكل', 'هل تريد إعادة تشغيل التطبيق لتغيير الشكل؟')
        if result2 == 'yes':
            restart_program()
        else: pass
    else: pass
# -----------------------------------------------------------------------------
def player_stoper():
    with open('play_check/play_status.dll', 'w') as file:
        file.write('1')

# -----------------------------------------------------------------------------

nav_vd_btn.configure(command=btn_vid_clicked)
nav_aud_btn.configure(command=btn_aud_clicked)
nav_bks_btn.configure(command=btn_bks_clicked)
nav_les_bks_btn.configure(command=btn_les_bks_clicked)
nav_dwnl_btn.configure(command=btn_dwl_clicked)
nav_set_btn.configure(command=btn_set_clicked)
back_main_btn.configure(command=btn_back_clicked)


def confirmExit():
    player_stoper()
    root.destroy()

root.protocol('WM_DELETE_WINDOW', confirmExit)
root.mainloop()