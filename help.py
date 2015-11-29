#! /usr/bin/env python

import sys
from RedSec_toolkit import * 

print Ver
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import RedSec_GUI_ABOUT_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.title('New_Toplevel_1')
    root.geometry('600x362+622+197')
    w = New_Toplevel_1 (root)
    RedSec_GUI_ABOUT_support.init(root, w)
    root.mainloop()

w = None
'''def create_New_Toplevel_1 (root, param=None):
    #Starting point when module is imported by another program.
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    w.title('New_Toplevel_1')
    w.geometry('600x362+622+197')
    w_win = New_Toplevel_1 (w)
    RedSec_GUI_ABOUT_support.init(w, w_win, param)
    return w_win'''
	
def create_New_Toplevel_1 (root, param=None):
   #Starting point when module is imported by another program.
    global w, w_win, rt
    if w:
		return
    rt = root
    w = Toplevel (root)
    w.title('About Red-Sec ToolKit')
    w.geometry('500x274+730+457')#613x274+678+157
    w_win = New_Toplevel_1 (w)
    w.protocol("WM_DELETE_WINDOW", destroy_New_Toplevel_1)
    return w_win

def destroy_New_Toplevel_1 ():
    global w
    w.destroy()
    w = None


class New_Toplevel_1:
    def __init__(self, master=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Segoe UI} -size 9 -weight normal -slant  " + \
            "roman -underline 0 -overstrike 0"
        font12 = "-family Arial -size 14 -weight normal -slant roman "  \
        "-underline 0 -overstrike 0"
        font13 = "-family Arial -size 18 -weight normal -slant roman  " + \
            "-underline 0 -overstrike 0"
        font22 = "-family {Footlight MT Light} -size 15 -weight normal " + \
            " -slant roman -underline 0 -overstrike 0"
        font23 = "TkDefaultFont " + \
        ""
        master.configure(borderwidth="1")
        master.configure(background=_bgcolor)


        self.Message1 = Message (master)
        self.Message1.place(relx=0.05,rely=0.48,relheight=0.52,relwidth=0.98)
        self.Message1.configure(background=_bgcolor)
        self.Message1.configure(borderwidth="4")
        self.Message1.configure(font=font12)
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''Red-Sec Encryption ToolKit %s
GUI application for file and directory encryption using AES

Shay@red-sec.com       
@Red_Sec_Shay
''' % Ver)
        self.Message1.configure(width=350)

        self.menubar = Menu(master,font=font10,bg=_bgcolor,fg=_fgcolor)
        master.configure(menu = self.menubar)



        self.Label1 = Label (master)
        self.Label1.place(relx=0.02,rely=0.03,height=111,width=474)
        self.Label1.configure(background=_bgcolor)
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self._img1 = PhotoImage(file=gif)
        self.Label1.configure(image=self._img1)
        self.Label1.configure(text='''Label''')
        self.Label1.configure(width=494)





if __name__ == '__main__':
    vp_start_gui()



