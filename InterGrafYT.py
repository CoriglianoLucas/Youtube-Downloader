from cProfile import label
from tkinter import *
from tkinter import messagebox
from pytube import YouTube
import re
 
class PythonYT(Frame):
 
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.parent = master
        self.grid()
        self.yt()
    
    def set_url(self):
        self.display.get()
        
    # end def
    def yt(self):
        
        pad = 5
        url = StringVar()
        self.label = Label(self, text="Ingrese la URL del video",font=("Roboto", 18), relief=RAISED, justify=RIGHT, bg='gray', fg='white', borderwidth=0)
        self.label.grid(row=0, column=0, columnspan=4, sticky="nsew")
        self.display = Entry(self, font=("Roboto", 18), relief=RAISED, justify=RIGHT, bg='lightgray', fg='red', borderwidth=0, textvariable=url)
        self.display.grid(row=1, column=0, columnspan=4, sticky="nsew", ipadx=pad, ipady=pad)
        def set_url():
            url2 = url.get()
            yt = YouTube(url2)
            filename = yt.title + ".mp3"
            try:
                yt.streams.filter(progressive=False, abr='160kbps').first().download(filename=filename)
            except OSError:
                title = re.sub(r"[^a-zA-Z0-9 ]","",yt.title)
                filename = title + ".mp3"
                yt.streams.filter(progressive=False, abr='160kbps').first().download(filename=filename)
            except AttributeError:
                yt.streams.filter(progressive=False, abr='128kbps').first().download(filename=filename)
            # print("Descarga realizada con exito! \n")
            label2 = Label(self, text="Descarga realizada con exito!",font=("Roboto", 18), relief=RAISED, justify=RIGHT, bg='gray', fg='white', borderwidth=0)
            label2.grid(row=3, column=0, columnspan=4, sticky="nsew")
        self.button = Button(self, text='Descargar', command=lambda:set_url())
        self.button.grid(row=2, column=0, columnspan=4, sticky="nsew", ipadx=pad, ipady=pad)


tk = Tk()
root = PythonYT(tk).grid()
tk.title('YouTubeDownloader')
tk.iconbitmap('icon.ico')
tk.config(bg='gray')
tk.mainloop()

