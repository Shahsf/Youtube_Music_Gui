from tkinter import *
from tkinter import ttk
import threading
from PIL import ImageTk, Image
import subprocess
import sys



def open_song_dict():
    subprocess.Popen('explorer "C:\\Downloads\\Song_Downloader\\"')
def update_progress_label():
    if (pb['value'] == 0):
        return ''
    else:
        return f"Current Progress: {int(pb['value'])}%"

def progress1(i):
    if pb['value'] < 100:
        pb['value'] = i
        value_label['text'] = update_progress_label()
    else:
        value_label['text'](message='The progress completed!')

def downloadhelper():
    try:
        threading.Thread(target=download).start()
    except RuntimeError:
        download()

def download():
    link = txtfld.get()
    lbl2.config(text='START DOWNLOAD!')
    value_label2.config(text='Currect Progress:0%')
    pb.grid(column=0, row=0, columnspan=2, padx=250, pady=300)
    try:
        yt = YouTube(link,on_progress_callback=on_progress)
        song_name = yt.streams[0].title
        if printResults() == 'MP3':
            stream = yt.streams.get_audio_only()
        if printResults() == 'MP4':
            stream = yt.streams.get_highest_resolution()
        finished = stream.download('\\Downloads\\Song_Downloader')
        print(f'{song_name} Download is complete')
        lbl2.config(text=f'{song_name} Download is Complete')
        value_label2.config(text='')
        pb['value'] = 100
    except:
        # try:
            playlist = Playlist(link)
            # print('Number of videos in playlist: %s' % len(playlist.video_urls))
            song_dict = (playlist.video_urls)
            n = len(song_dict)
            the_progress = 100/n
            for i,song in enumerate(song_dict):
                i = float(i*the_progress)
                progress1(i)
                the_link = song
                yt = YouTube(the_link,on_progress_callback=on_progress)
                song_name = yt.streams[0].title
                if (printResults())== 'MP3':
                    stream = yt.streams.get_audio_only()
                if (printResults())== 'MP4':
                    stream = yt.streams.get_highest_resolution()

                finished = stream.download('\\Downloads\\Song_Downloader')
                # Progress += the_progress
                # print(Progress,2)
                print(f'{song_name} Download is complete')
                lbl2.config(text=f'{song_name} Download is Complete')
                value_label2.config(text='')
            print('Playlist Download is Completed')
            value_label['text'](message='The progress completed!')
        # except:

            print('error')
            lbl2.config(text="Wrong URL/Private Playlist")
            value_label2.config(text='')

def printResults():
      if r.get() == 0:
         song_type = 'MP3'
      else:
         song_type = 'MP4'
      return song_type
def stop_download():
    sys.exit()





from pytube import Playlist
import pytube
from pytube import YouTube
from pytube.cli import on_progress #this module contains the built in progress bar.
window=Tk()
img = ImageTk.PhotoImage(Image.open("333.png"))
backgroundimg = Label( window, image = img)
backgroundimg.place(x = 0,y = 0)
txtfld=Entry(window, text="This is Entry Widget", bd=5,width=50)
txtfld.place(x=250, y=100)
btn=Button(window, text="Download", fg='black',width=25,bg='light green',height=2,font=('Times',16),bd=3,command=downloadhelper)
btn.place(x=250, y=150)

btn2=Button(window, text="Song Location", fg='black',width=12,bg='light blue',height=2,font=('Bold Times',10),bd=3,command=open_song_dict)
btn2.place(x=680, y=540)
btn3=Button(window, text="Stop", fg='black',width=12,bg='light blue',height=2,font=('Bold Times',10),bd=3,command=stop_download)
btn3.place(x=680, y=20)

lbl=Label(window, text="Please Enter Playlist/Song URL:", fg='black', font=("Times", 20),bd=3,bg='#99D9EA')
lbl.place(x=235, y=50)

lbl2=Label(window, fg='green', font=("Times", 16),bd=3,bg='#99D9EA')
lbl2.place(y=240,x=400,anchor="center")

pb = ttk.Progressbar(
    window,
    orient='horizontal',
    mode='determinate',
    length=320
)
# place the progressbar

value_label = Label(window, text=update_progress_label(),bg='#99D9EA')
value_label.place(x=350,y=325)
value_label2 = Label(window, text='',bg='#99D9EA')
value_label2.place(x=345,y=325)






# Create a variable for strings, and initialize the variable
# Radiobutton(window, text="MP3", variable=song_type, value="MP3", command=printResults)
#
# Radiobutton(window, text="MP4", variable=song_type, value="MP4", command=printResults)
r = IntVar()
MP3 = Radiobutton(text="MP3(Audio)",
                      variable=r, value=0, highlightthickness=0, command=printResults,bg='#99D9EA',font=("Times", 16))
MP3.place(x=250,y=265)

MP4 = Radiobutton(text="MP4(Video)",
                     variable=r, value=1,    highlightthickness=0, command=printResults,bg='#99D9EA',font=("Times", 16))
MP4.place(x=430,y=265)





window.title('Music Downloader')
window.geometry("800x600")
window.mainloop()