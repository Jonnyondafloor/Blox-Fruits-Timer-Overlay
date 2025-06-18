import tkinter as tk
import time
import threading
import pygetwindow as gw
import math
import winsound
from Timers import template

saveDataJsonPath = 'SaveData.json'
app_name = 'Release'
window_whitelist = ['Roblox', app_name]

class Timer:
    def __init__(self,
                 master: tk.Tk | tk.Frame | tk.Toplevel, # Root Tkinter Object
                 timer: template.Timer # File containing Timer Functions and Constants
                 ):
        
        self.master = master

        self.image = timer.load_image()
        self.title = timer.title
        self.description = timer.description

        self.reset_method = timer.reset_method
        self.time = tk.StringVar(master)
        self.end_epoch = timer.delay_method(saveDataJsonPath)

        self.reset_enabled = timer.auto_reset_enabled
        self.reset_time = self.end_epoch + timer.auto_reset_delay

        self.notified = False

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
            if self.reset_enabled and self.reset_time <= now and remaining_time <= 0:
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

        notifier_thread = threading.Thread(target=self._display_notifications, daemon=True)
        notifier_thread.start()
    
    def new_notification(self, title: str, description: str):
        self.notification_queue.append({'Title': title, 'Description': description})
    
    def _display_notifications(self):
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
root.title(app_name)
root.overrideredirect(True)
root.attributes('-topmost', True)
root.attributes('-transparentcolor', '#010101')
root.geometry('1650x60+179+0')
root.config(bg='#010101')

notifications = Notifications(root)

from Timers import FruitRoll, CastleRaid, ElitePirate, FullMoon, SilverChest, GoldenChest, DiamondChest, FruitSpawn

# Fruit
Timer(root, FruitRoll.get_timer())
Timer(root, CastleRaid.get_timer())
Timer(root, FruitSpawn.get_timer())
# Money
Timer(root, SilverChest.get_timer())
Timer(root, GoldenChest.get_timer())
Timer(root, DiamondChest.get_timer())
# Misc
Timer(root, ElitePirate.get_timer())
Timer(root, FullMoon.get_timer())

overlay_lock_thread = threading.Thread(target=lock_to_roblox, args=[root], daemon=True)
overlay_lock_thread.start()

root.mainloop()
