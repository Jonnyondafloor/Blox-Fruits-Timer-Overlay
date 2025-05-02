import time
from PIL import Image, ImageTk

imagePath = 'Images\\ElitePirate.png'
noti_title = 'The Elite Pirate Has Arrived'
noti_desc = 'Show him who is Really Elite'

def delay_method(_):
    now = time.time()
    delay = 9*60
    end = now + delay
    return end

def reset_method(_):
    now = time.time()
    delay = 8*60+45
    end = now + delay
    return end

image = ImageTk.PhotoImage(Image.open(imagePath).resize((50, 60)))
