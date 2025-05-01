import time
from PIL import Image, ImageTk

imagePath = 'Images\\SilverChest.png'

def delay_method(_):
    now = time.time()
    delay = 0
    end = now + delay
    return end

def reset_method(_):
    now = time.time()
    delay = 3*60
    end = now + delay
    return end

image = ImageTk.PhotoImage(Image.open(imagePath).resize((50, 60)))