import time
from PIL import Image, ImageTk

imagePath = 'Images\\FullMoon.png'
noti_title = 'The Moon will be Full Tonight.'
noti_desc = 'Race to the danger zones, because its time to hunt kitsune island!'

def cycle_moon(cycles: int | float = 1):
    cycle_time = 24*60
    return cycle_time * cycles

def delay_method(_):
    now = time.time()
    delay = cycle_moon(2) - 6*60 # set to sunrise
    end = now + delay
    return end

def reset_method(_):
    now = time.time()
    delay = cycle_moon(8)
    end = now + delay
    return end

image = ImageTk.PhotoImage(Image.open(imagePath).resize((50, 60)))
