from Timers import template
import time

def delay_method(_):
    now = time.time()
    end = now + 4*60*60 # 4 hours
    return end

def reset_method(_):
    now = time.time()
    end = now + 4*60*60 # 4 hours
    return end

def get_timer():
    timer = template.Timer()
    timer.image_path = 'Images\\GodsChaliceChest.png'
    timer.title = 'The Chalice has Spawned'
    timer.description = 'The Gods Chalice has Spawned in a chest.\nits time for a Treasure hunt :>'
    timer.auto_reset_delay = 0
    timer.delay_method = delay_method
    timer.reset_method = reset_method
    return timer
