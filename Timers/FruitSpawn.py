import time
from PIL import Image, ImageTk

imagePath = 'Images\\FruitSpawn.png'
noti_title = 'A Fruit has Spawned'
noti_desc = 'Search the Sea for the Fruit that be'
auto_reset_enabled = True
auto_reset_delay = 1200

def is_week_day():
    day_of_week = time.gmtime().tm_wday
    if day_of_week < 5:
        return True
    else:
        return False

def delay_method(_):
    now = time.time()
    delay = 45*60
    if is_week_day():
        delay += 15*60
    end = now + delay
    return end

def reset_method(_):
    now = time.time()
    delay = 45*60
    if is_week_day():
        delay += 15*60
    end = now + delay
    return end

image = ImageTk.PhotoImage(Image.open(imagePath).resize((50, 60)))