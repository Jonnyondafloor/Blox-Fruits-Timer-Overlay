from Timers import template
import time

def delay_method(_):
    now = time.time()
    delay = 0
    end = now + delay
    return end

def reset_method(_):
    now = time.time()
    delay = 12*60
    end = now + delay
    return end

def get_timer():
    timer = template.Timer()
    timer.image_path = 'Images\\DiamondChest.png'
    timer.title = 'Diamond Chest is Ready'
    timer.description = 'The Diamond Chest Route is Ready.\ngo Collect your money!'
    timer.auto_reset_enabled = False
    timer.delay_method = delay_method
    timer.reset_method = reset_method
    return timer
