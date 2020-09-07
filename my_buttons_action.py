import tkinter as tk

def btn_news_clicked():
#     btn_back.destroy()
#     btn_next.destroy()
    btn_back=tk.Button(content_frame,text='back',width=25,height=5,bg='black',fg='red',font='arial 14')
    btn_back.configure(command=btn_back_clicked)
    btn_back.place(relx=0.1, rely=0.1,  height =20, width =50)
    btn_next=tk.Button(content_frame,text='next',width=25,height=5,bg='black',fg='red',font='arial 14')
    btn_next.configure(command=btn_next_clicked)
    btn_next.place(relx=0.2, rely=0.1, height =20, width =50)
    TP.test()
url = "http://docs.python.org/library/webbrowser.html"
# 2. VIDEO
def btn_vd_clicked():
    global url
    browser.browser(url)

# 3. NEXT
i=0
def btn_next_clicked():
    global i
    news_content['text'] = data[i].get_text(), data_img[i].img['src']
    print(data_img[i].img['src'])
    img_url = data_img[i].img['src']
    response = requests.get(img_url)
    img_data = response.content
    #img = ImageTk.PhotoImage((Image.open(BytesIO(img_data)))) #.resize((50, 50), Image.ANTIALIAS)
    #imglabel = tk.Label(news_content, image=img)
    #imglabel.place(height =100, width =200)
    if i < 6 : i += 1
# 4. BACK
def btn_back_clicked():
    global i
    news_content['text'] = data[i].get_text()
    if i > 0 : i -= 1