import time
from PIL import Image, ImageTk

imagePath = 'Images\\SilverChest.png'
noti_title = 'Silver Chest is Ready'
noti_desc = 'The Silver Chest Route is Ready.\ngo Collect your money!'

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
