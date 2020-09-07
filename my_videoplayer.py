try:
    import vlc
except:
    print('import error')
import pafy
import tkinter as tk
from tkinter import ttk
# from functools import partial
import threading
import time
import sys
import os

TOPBG = '#283035'
COLORTEXT = '#B9BBBC'
COLORTEXTACTIVE = '#0094F0'


def vlc_path_installer():
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    # Python 3.8 things:
    with os.add_dll_directory(os.path.join(base_path, "VLC")):
        import vlc
        print('imported')




class player():
    def __init__(self, page, root, canvas_t, canvas_b, lbl_descr):
        vlc_path_installer()
        with open('play_check/play_status.dll', 'r') as file:
            if file.read() == '0':
                self.page = page
                self.canvas_t = canvas_t
                self.canvas_b = canvas_b
                self.lbl_descr = lbl_descr
                self._geometry = ''
                self.root = root
                self.arr = []
                self.player_stoped = None
                self.second()
                vol = self.player.audio_get_volume()
                if vol > 0:
                    self.volVar.set(vol)
                    self.volSlider.set(vol)
        while True:
            with open('play_check/play_status.dll', 'r') as file:
                if file.read() == '0':
                    pass
                else:
                    self.player.stop()
                    return


    def stopExit(self):
        self.player.stop()
        self.timeSlider.set(0)

    def second(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.icons()
        self.videoStream()

    def icons(self):
        icon_stop = tk.PhotoImage(file="images/stop.gif")
        icon_play = tk.PhotoImage(file="images/play.gif")
        icon_pause = tk.PhotoImage(file="images/pause.gif")
        icon_replay = tk.PhotoImage(file="images/replay.gif")
        icon_volume = tk.PhotoImage(file="images/Volume.gif")
        icon_mute = tk.PhotoImage(file="images/mute.gif")
        self.arr = [icon_play, icon_pause, icon_stop, icon_volume, icon_mute, icon_replay]

    def vidPlrCtrl(self):
        w = 60
        h = 52
        self.playerBtnPlay = ttk.Button(self.canvas_b, style="Player.TButton", image=self.arr[1])
        self.playerBtnPlay.place(x=5, y=10, width=w, height=h)
        playerBtnStop = ttk.Button(self.canvas_b, style="Player.TButton")
        playerBtnStop.place(x=70, y=10, width=w, height=h)
        self.playerBtnVol = ttk.Button(self.canvas_b, style="Player.TButton")
        self.playerBtnVol.place(x=135, y=10, width=w, height=h)
        self.playerLblTime = tk.Label(self.canvas_b, text='00:00 / 00:00', bg='#13171B', fg=COLORTEXT)
        self.playerLblTime.place(x=320, y=10, width=w * 2, height=h)

        self.volMuted = False
        self.volVar = tk.IntVar()
        self.volSlider = tk.Scale(self.canvas_b, bg=COLORTEXTACTIVE, bd=0, highlightthickness=0,
                                   relief='flat', sliderrelief='flat',
                                  variable=self.volVar, command=self.OnVolume,
                                  from_=0, to=100, orient=tk.HORIZONTAL, length=200,
                                  showvalue=0)
        self.volSlider.place(x=210, y=33, width=100, height=5)

        self.timeVar = tk.DoubleVar()
        self.timeSliderLast = 0
        self.timeSlider = tk.Scale(self.canvas_b, bg='red', bd=0, highlightthickness=0,
                                   relief='flat', sliderrelief='flat', troughcolor=TOPBG,
                                   from_=0, to=1000, orient='horizontal', length=500,
                                   showvalue=0)
        self.timeSlider.place(x=0, y=0, height=10, relwidth=1)
        self.timeSliderUpdate = time.time()


        def playEvent():
            if self.player.is_playing():
                self.player.pause()
                self.playerBtnPlay.configure(image=self.arr[0])
            else:
                try:
                    t = self.timeVar.get()
                    print(t)
                    self.player.set_time(int(t * 1e3))  # milliseconds
                    self.player.play()
                    # print(self.player.get_length())
                    vol = self.player.audio_get_volume()
                    if vol > 0:
                        self.volVar.set(vol)
                        self.volSlider.set(vol)
                except:
                    print('somth wrong')
                self.playerBtnPlay.configure(image=self.arr[1])

        self.playEvent = playEvent
        playerBtnStop.configure(image=self.arr[2])
        self.playerBtnVol.configure(image=self.arr[3])

        def stopEvent():
            self.player.stop()
            self.timeSlider.set(0)

        def volEvent():
            if self.volMuted:
                self.playerBtnVol.configure(image=self.arr[3])
            else:
                self.playerBtnVol.configure(image=self.arr[4])
            self.OnMute()

        def setTime(i):
            if self.player:
                t = self.timeVar.get()
                t2 = int(self.player.get_length() * 1e-3)*1000
                if self.timeSliderLast != int(t):
                    if t2 == int(t * 1e3):
                        self.player_stoped = True
                        self.player.stop()
                        self.playerBtnPlay.configure(image=self.arr[5])
                    else:
                        self.player.set_time(int(t * 1e3))
                        if self.player_stoped:
                            self.player_stoped = False
                        self.timeSliderUpdate = time.time()

        self.playerBtnPlay.config(command=playEvent)
        playerBtnStop.config(command=stopEvent)
        self.playerBtnVol.config(command=volEvent)
        self.timeSlider.config(variable=self.timeVar, command=setTime)


    def SliderUpdate(self):
        if self.player:
            t = self.player.get_length() * 1e-3
            t2 = int(self.player.get_length() * 1e-3)
            t3 = int(self.player.get_time() * 1e-3)+1
            sec_all = self.player.get_length() * 1e-3
            minute_all, sec_all = divmod(sec_all, 60)
            hour_all, minute_all = divmod(minute_all, 60)
            sec_cur = self.player.get_time() * 1e-3
            minute_cur, sec_cur = divmod(sec_cur, 60)
            hour_cur, minute_cur = divmod(minute_cur, 60)
            t_all = "%02d:%02d:%02d" % (hour_all, minute_all, sec_all)
            t_cur = "%02d:%02d:%02d" % (hour_cur, minute_cur, sec_cur)
            self.playerLblTime.config(text=t_cur + " / " + t_all)
            if t > 0:
                if t2 == t3:
                    self.player_stoped = True
                    self.player.stop()
                    self.playerBtnPlay.configure(image=self.arr[5])
                else:
                    self.timeSlider.config(to=t)
                    t = self.player.get_time() * 1e-3
                    if t > 0 and time.time() > (self.timeSliderUpdate + 2):
                        self.timeSlider.set(t)
                        self.timeSliderLast = int(self.timeVar.get())
                        if self.player_stoped:
                            # self.playEvent()
                            self.player_stoped = False
        self.root.after(1000, self.SliderUpdate)
        if not self._geometry:
            # self.OnResize()
            pass

    def OnResize(self, *unused):
        g = self.root.geometry()
        if g != self._geometry and self.player:
            u, v = self.player.video_get_size()
            if v > 0 and u > 0:
                g, x, y = g.split('+')
                w, h = g.split('x')
                if u > v:
                    h = round(float(w) * v / u)
                else:
                    w = round(float(h) * u / v)
                self.root.geometry("%sx%s+%s+%s" % (w, h, x, y))
                self._geometry = self.root.geometry()

    def videoStream(self):
        self.video = pafy.new(self.page)
        mystream = self.video.streams[0]
        playurl = mystream.url
        self.media = self.instance.media_new(playurl)
        # vlc_events = self.media.event_manager()
        self.media.get_mrl()
        self.player.set_media(self.media)
        h = self.canvas_t.winfo_id()
        self.player.set_hwnd(h)
        t = threading.Thread(target=self.player.play)
        t2 = threading.Thread(target=self.video_info_getting)
        t.start()
        t2.start()
        self.vidPlrCtrl()
        self.SliderUpdate()


    def OnVolume(self, *unused):
        vol = min(self.volVar.get(), 100)
        v_M = "%d%s" % (vol, " (Muted)" if self.volMuted else '')
        if self.player and not self.player_stoped:
            if self.player.audio_set_volume(vol):
                pass

    def OnMute(self, *unused):
        self.volMuted = m = not self.volMuted
        self.player.audio_set_mute(m)
        self.OnVolume()


    def video_info_getting(self):
        try:
            title = self.video.title
            author = self.video.author
            thumb_img = self.video.thumb
            duration = self.video.duration
            length = self.video.length
            likes = self.video.likes
            views = self.video.viewcount
            self.video_info = [title, author, thumb_img, duration, length, likes, views]
        except:
            self.video_info = ['title', 'author', 0, 00+':'+00, 0, 0, 0]
        self.video_info_post()

    def video_info_post(self):
        self.lbl_descr.configure(text=self.video_info[0])

