import tkinter as tk
from playsound import playsound
import time

class AudioPlayer(tk.Tk):
    
    def __init__(self,master):
        super().__init__()
        
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.geometry('400x50')
        self.master.title('Audio Player')

        self.label = tk.Label(self.frame, text='Song', width=40)
        self.label.pack(side='left')
        self.btn = tk.Button(self.frame, text='Start', width=50, height=10, command=self.play_audio)
        self.btn.pack(side='left')

        self.frame.pack()

    def play_audio(self):
        print('Play audio')
        playsound('./assets/sounds/song.mp3')

if __name__ == '__main__':
    root = tk.Tk()
    app_audioplayer = AudioPlayer(root)
    root.mainloop()


    