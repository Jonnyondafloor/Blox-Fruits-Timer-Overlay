import tkinter as tk
import time
from PIL import Image
import threading
import pygetwindow as gw
import math
import winsound

saveDataJsonPath = 'SaveData.json'
app_name = 'Release'
window_whitelist = ['Roblox', app_name]

class Timer:
    def __init__(self,
                 master: tk.Tk | tk.Frame | tk.Toplevel,
                 image: Image.Image,
                 notification_title: str, # used for notification
                 notification_description: str, # used for notification
                 delay_method, # A Function that returns the length of time the timer should wait
                 reset_method, # A Function that returns the length of time the timer should wait after clicking reset
                 auto_reset_enabled: bool,
                 auto_reset_delay: int
                 ):
        
        self.master = master

        self.image = image
        self.title = notification_title
        self.description = notification_description
        self.notified = False

        self.reset_method = reset_method
        self.time = tk.StringVar(master)
        self.end_epoch = delay_method(saveDataJsonPath)

        self.reset_enabled = auto_reset_enabled
        self.reset_time = auto_reset_delay

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
        self.notified = False

    def update_time(self):
        now = time.time()
        remaining_time = int(self.end_epoch - now)
        if remaining_time <= 0:
            self.notified = True
        
        while True:
            time.sleep(1)
            now = time.time()
            remaining_time = int(self.end_epoch - now)
            if remaining_time > 0:
                formatted_time = self.format_time(remaining_time)
                self.master.after(0, self.time.set, formatted_time)
                continue
            if self.reset_enabled:
                if self.reset_time <= now and remaining_time <= 0:
                    self.reset(1)
            else:
                self.master.after(0, self.time.set, 'Ready ✅')
            if not self.notified:
                notifications.new_notification(self.title, self.description)
                self.notified = True

class Notifications:
    def __init__(self, master: tk.Tk):
        self.size = '300x108'
        self.root = tk.Toplevel(master)
        self.root.overrideredirect(True)
        self.root.attributes('-topmost', True)
        self.root.geometry(f'{self.size}+-300+338')
        self.root.config(bg='#000000')

        self.title = tk.StringVar(self.root)
        self.description = tk.StringVar(self.root)
        tk.Label(self.root, textvariable=self.title, font=('Arial', 12, 'bold'), fg='white', bg='#000000').pack(anchor='nw')
        tk.Label(self.root, textvariable=self.description, font=('Arial', 12), fg='white', bg='#000000', wraplength=300, justify='left').pack(anchor='sw')
        self.notification_queue = []

        notifier_thread = threading.Thread(target=self.display_notifications, daemon=True)
        notifier_thread.start()
    
    def new_notification(self, title: str, description: str):
        self.notification_queue.append({'Title': title, 'Description': description})
    
    def display_notifications(self):
        while True:
            if self.notification_queue and self.notification_queue[0]:
                self.title.set(self.notification_queue[0]['Title'])
                self.description.set(self.notification_queue[0]['Description'])
                def animate_slide_in():
                    travel_time = 0.5
                    fps = 60
                    start = -300
                    end = 0
                    dist = end - start
                    delay = travel_time / fps
                    current = start
                    dist_per_frame = dist / fps
                    frames = dist / dist_per_frame

                    self.root.geometry(f'{self.size}+{start}+338')
                    self.root.deiconify()

                    for _ in range(int(frames)):
                        current += dist_per_frame
                        self.root.geometry(f'{self.size}+{math.ceil(current)}+338')

                        time.sleep(delay)
                
                animate_slide_in()
                winsound.PlaySound(R'SFX\notification.wav', winsound.SND_FILENAME)
                time.sleep(7.5)
                self.root.withdraw()
                del self.notification_queue[0]
            time.sleep(2.5)

def lock_to_roblox(master: tk.Tk):
    def check_active_window():
        active_window = gw.getActiveWindow()
        if not active_window:
            return
        
        if active_window.title in window_whitelist:
            master.deiconify()
        else:
            master.withdraw()
        
        master.after(500, check_active_window)
    master.after(0, check_active_window)



root = tk.Tk()
root.overrideredirect(True)
root.attributes('-topmost', True)
root.attributes('-transparentcolor', '#010101')
root.geometry('1650x60+179+0')
root.config(bg='#010101')

notifications = Notifications(root)

from Timers import FruitRoll, CastleRaid, ElitePirate, FullMoon, SilverChest, GoldenChest, DiamondChest, FruitSpawn

# Fruit
Timer(root, FruitRoll.image, FruitRoll.noti_title, FruitRoll.noti_desc, FruitRoll.delay_method, FruitRoll.reset_method)
Timer(root, CastleRaid.image, CastleRaid.noti_title, CastleRaid.noti_desc, CastleRaid.delay_method, CastleRaid.reset_method)
Timer(root, FruitSpawn.image, FruitSpawn.noti_title, FruitSpawn.noti_desc, FruitSpawn.delay_method, FruitSpawn.delay_method)
# Money
Timer(root, SilverChest.image, SilverChest.noti_title, SilverChest.noti_desc, SilverChest.delay_method, SilverChest.reset_method)
Timer(root, GoldenChest.image, GoldenChest.noti_title, GoldenChest.noti_desc, GoldenChest.delay_method, GoldenChest.reset_method)
Timer(root, DiamondChest.image, DiamondChest.noti_title, DiamondChest.noti_desc, DiamondChest.delay_method, DiamondChest.reset_method)
# Misc
Timer(root, ElitePirate.image, ElitePirate.noti_title, ElitePirate.noti_desc, ElitePirate.delay_method, ElitePirate.reset_method)
Timer(root, FullMoon.image, FullMoon.noti_title, FullMoon.noti_desc, FullMoon.delay_method, FullMoon.reset_method)

overlay_lock_thread = threading.Thread(target=lock_to_roblox, args=[root], daemon=True)
overlay_lock_thread.start()

root.mainloop()
