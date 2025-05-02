import time
from PIL import Image, ImageTk

imagePath = 'Images\\FullMoon.png'
noti_title = 'The Full Moon has Risen'
noti_desc = 'The Temple of Time is Ready for Another Trial'

def delay_method(_):
    now = time.time()
    delay = 24*60*2
    end = now + delay
    return end

def reset_method(_):
    now = time.time()
    delay = 24*60*8
    end = now + delay
    return end

image = ImageTk.PhotoImage(Image.open(imagePath).resize((50, 60)))
