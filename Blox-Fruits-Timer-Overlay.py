import tkinter as tk
import time
from PIL import Image
import threading

saveDataJsonPath = 'SaveData.json'

class Timer:
    def __init__(self,
                 master: tk.Tk | tk.Frame | tk.Toplevel,
                 image: Image.Image,
                 delay_method, # A Function that returns the length of time the timer should wait
                 reset_method, # A Function that returns the length of time the timer should wait after clicking reset
                 auto: int | None = None # time in seconds after the ready that it will reset automatically
                 ):
        
        self.master = master
        self.image = image
        self.reset_method = reset_method
        self.time = tk.StringVar(master)
        self.end_epoch = delay_method(saveDataJsonPath)
        self.create_frame()
        updater = threading.Thread(target=self.update_time, daemon=True)
        updater.start()

    def create_frame(self):
        frame = tk.Frame(self.master)
        frame.config(width=50, height=60)
        icon = tk.Label(frame, image=self.image)
        icon.bind('<Button-1>', self.reset)
        icon.pack()
        tk.Label(frame, textvariable=self.time).place(relx=0.5, rely=1.0, anchor=tk.S)
        frame.pack_propagate(False)
        frame.pack(side=tk.LEFT, padx=5)

    @staticmethod
    def format_time(seconds: int) -> str:
        suffixes = ['m', 'h']
        suffix_str = 's'
        for suffix in suffixes:
            if seconds >= 60:
                seconds /= 60
                suffix_str = suffix
            else:
                break
        seconds = round(seconds)
        return f'{seconds}{suffix_str}'

    def reset(self, *args):
        self.end_epoch = self.reset_method(saveDataJsonPath)
        now = time.time()
        remaining_time = int(self.end_epoch - now)
        formatted_time = self.format_time(remaining_time)
        self.master.after(0, self.time.set, formatted_time)

    def update_time(self):
        while True:
            now = time.time()
            remaining_time = int(self.end_epoch - now)
            formatted_time = self.format_time(remaining_time)
            self.master.after(0, self.time.set, formatted_time)
            if remaining_time <= 0:
                self.master.after(0, self.time.set, 'Ready ✅')
            
            time.sleep(1)


root = tk.Tk()
root.overrideredirect(True)
root.attributes('-topmost', True)
root.attributes('-transparentcolor', '#010101')
root.geometry('1650x60+179+0')
root.config(bg='#010101')

from Timers import FruitRoll, CastleRaid, ElitePirate, FullMoon, SilverChest, GoldenChest, DiamondChest

# Fruit
Timer(root, FruitRoll.image, FruitRoll.delay_method, FruitRoll.reset_method)
Timer(root, CastleRaid.image, CastleRaid.delay_method, CastleRaid.reset_method)
# Money
Timer(root, SilverChest.image, SilverChest.delay_method, SilverChest.reset_method)
Timer(root, GoldenChest.image, GoldenChest.delay_method, GoldenChest.reset_method)
Timer(root, DiamondChest.image, DiamondChest.delay_method, DiamondChest.reset_method)
# Misc
Timer(root, ElitePirate.image, ElitePirate.delay_method, ElitePirate.reset_method)
Timer(root, FullMoon.image, FullMoon.delay_method, FullMoon.reset_method)

root.mainloop()
