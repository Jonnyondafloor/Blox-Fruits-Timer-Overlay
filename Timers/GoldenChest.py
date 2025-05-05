import time
from PIL import Image, ImageTk

imagePath = 'Images\\GoldenChest.png'
noti_title = 'Golden Chest is Ready'
noti_desc = 'The Golden Chest Route is Ready.\ngo Collect your money!'
auto_reset_enabled = False
auto_reset_delay = 0

def delay_method(_):
    now = time.time()
    delay = 0
    end = now + delay
    return end

def reset_method(_):
    now = time.time()
    delay = 6*60
    end = now + delay
    return end

image = ImageTk.PhotoImage(Image.open(imagePath).resize((50, 60)))
