import time
from PIL import Image, ImageTk

imagePath = 'Images\\CastleRaid.png'
noti_title = 'The Castle is Under Attack!'
noti_desc = 'Defeat their Leader and Claim its Treasures'
auto_reset_enabled = True
auto_reset_delay = 360

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

image = ImageTk.PhotoImage(Image.open(imagePath).resize((50, 60)))
