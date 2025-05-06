from Timers import template
import time

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

def get_timer():
    timer = template.Timer('Images\\SilverChest.png')
    timer.title = 'Silver Chest is Ready'
    timer.description = 'The Silver Chest Route is Ready.\ngo Collect your money!'
    timer.auto_reset_enabled = False
    timer.delay_method = delay_method
    timer.reset_method = reset_method
    return timer
