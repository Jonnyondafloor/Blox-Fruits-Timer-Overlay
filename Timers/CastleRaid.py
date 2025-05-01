import time
from PIL import Image, ImageTk

imagePath = 'Images\\CastleRaid.png'

def delay_method(_):
    now = time.time()
    delay = 60*60+15*60
    end = now + delay
    return end

def reset_method(_):
    now = time.time()
    delay = 60*60+15*60
    end = now + delay
    return end

image = ImageTk.PhotoImage(Image.open(imagePath).resize((50, 50)))
