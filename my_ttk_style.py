from tkinter import ttk


WINDOWGEOMETRY = '800x500'
HEIGHT = 500
WIDTH = 800
MENUBTNHG = 26
MENUBTNWH = 180
MINHEIGHT = 500
MINWIDTH = 800
FONTFAMILY = 'Arial'
# FONTSIZE = 14
FONTSIZE = 22
FONTSIZEBTN = 12
CONTENTBTEXT = 24
MENUTEXTSIZE = 16


def style_status():
    try:
        with open('style.dll', 'r') as file:
            style = file.read()
    except:
        with open('style.dll', 'w') as file:
            file.write('1')
            style = '1'
    return style


style = style_status()

if style == '1':
    COLORTEXTACTIVE = '#0094F0'
    COLORTEXT = '#B9BBBC'
    COLORTEXTDSB = '#7E8285'
    TOPBG = '#283035'
    CONTENTBG = '#1E252B'
    MENUBG = '#171A1E'
    SCROLL_ONE = '#1E2228'
    SCROLL_TWO = '#13171B'
    style_palette = [COLORTEXTACTIVE, COLORTEXT, COLORTEXTDSB, TOPBG, CONTENTBG, MENUBG, SCROLL_ONE, SCROLL_TWO]

elif style == '2':
    COLORTEXTACTIVE = '#0078d7'
    COLORTEXT = '#000000'
    COLORTEXTDSB = '#747474'
    TOPBG = '#F2F2F2'
    CONTENTBG = '#FFFFFF'
    MENUBG = '#F2F2F2'
    SCROLL_ONE = '#c2c2c2'
    SCROLL_TWO = MENUBG
    style_palette = [COLORTEXTACTIVE, COLORTEXT, COLORTEXTDSB, TOPBG, CONTENTBG, MENUBG, SCROLL_ONE, SCROLL_TWO]

elif style == '3':
    COLORTEXTACTIVE = '#0078d7'
    COLORTEXT = '#f2e9e4'
    COLORTEXTDSB = '#c9ada7'
    TOPBG = '#9a8c98'
    CONTENTBG = '#4a4e69'
    MENUBG = '#22223b'
    SCROLL_ONE = '#c2c2c2'
    SCROLL_TWO = MENUBG
    style_palette = [COLORTEXTACTIVE, COLORTEXT, COLORTEXTDSB, TOPBG, CONTENTBG, MENUBG, SCROLL_ONE, SCROLL_TWO]

elif style == '4':
    COLORTEXTACTIVE = '#0078d7'
    COLORTEXT = '#e9c46a'
    COLORTEXTDSB = '#f4a261'
    TOPBG = '#e76f51'
    CONTENTBG = '#2a9d8f'
    MENUBG = '#264653'
    SCROLL_ONE = '#c2c2c2'
    SCROLL_TWO = MENUBG
    style_palette = [COLORTEXTACTIVE, COLORTEXT, COLORTEXTDSB, TOPBG, CONTENTBG, MENUBG, SCROLL_ONE, SCROLL_TWO]

elif style == '5':
    COLORTEXTACTIVE = '#0078d7'
    COLORTEXT = '#f4f1de'
    COLORTEXTDSB = '#f2cc8f'
    TOPBG = '#81b29a'
    CONTENTBG = '#e07a5f'
    MENUBG = '#3d405b'
    SCROLL_ONE = '#c2c2c2'
    SCROLL_TWO = MENUBG
    style_palette = [COLORTEXTACTIVE, COLORTEXT, COLORTEXTDSB, TOPBG, CONTENTBG, MENUBG, SCROLL_ONE, SCROLL_TWO]


def Style():
    s = ttk.Style()
    # print(s.theme_names())
    s.theme_use('default')

    s.theme_settings("default", {
        "TEntry": {
            "configure": {"padding": 5, "borderwidth ": 0, "relief": "solid"},
            "map": {
                "background": [("active", "MENUBG"),
                               ("!disabled", "MENUBG")],
                "fieldbackground": [("!disabled", MENUBG)],
                "foreground": [("focus", COLORTEXT),
                               ("!disabled", "#707273")]
            }
        }
    })  # text disabled color #8A8C8E

    s.theme_settings("default", {
        "TButton": {
            "configure": {"padding": 2, "relief": "flat", "borderwidth": 0},
            "map": {
                "background": [("active", CONTENTBG),
                               ("!disabled", MENUBG)],
                "foreground": [("focus", COLORTEXTACTIVE),
                               ("!disabled", COLORTEXT)]
            }
        }
    })

    s.theme_settings("default", {
        "Back.TButton": {
            "configure": {"padding": 2, "relief": "flat", "borderwidth": 0},
            "map": {
                "background": [("active", TOPBG),
                               ("!disabled", CONTENTBG)],
                "foreground": [("focus", COLORTEXTACTIVE),
                               ("!disabled", COLORTEXT)]
            }
        }
    })

    s.theme_settings("default", {
        "TScrollbar": {
            "configure": {"padding": 0, "relief": "flat", "borderwidth": 0, "width": 15, "arrowsize": 15},
            "map": {
                "background": [("active", SCROLL_ONE),
                               ("!disabled", SCROLL_TWO),
                               ("disabled", SCROLL_TWO)]
            }
        }
    })

    s.theme_settings("default", {
        "Attention.Player.TButton": {
            "configure": {"relief": "solid", "borderwidth": 0},
            "map": {
                "background": [("active", "#2EAFFF"),
                               ("!disabled", COLORTEXTACTIVE)],
                "foreground": [("focus", "black"),
                               ("!disabled", "black")]
            }
        }
    })

    s.theme_settings("default", {
        "Player.TButton": {
            "map": {
                "background": [("active", "#1E2228"),
                               ("!disabled", "#13171B"),
                               ("disabled", "#13171B")]
            }
        }
    })

    s.theme_settings("default", {
        "Horizontal.TProgressbar": {
            "configure": {"relief": "flat", "borderwidth": 0},
            "map": {
                "background": [("disabled", COLORTEXTACTIVE)],
                "troughcolor": [("disabled", TOPBG)]
            }
        }
    })
    s.configure("Menu.TButton", font=(FONTFAMILY, MENUTEXTSIZE), anchor='e', justify='right')
    s.configure("Content.Attention.Player.TButton", font=(FONTFAMILY, MENUTEXTSIZE+5))
    s.configure("Content.TButton", font=(FONTFAMILY, FONTSIZE))
    s.configure("St.Vertical.TScrollbar", troughcolor='#363B41', arrowcolor=COLORTEXT)

    return style_palette

