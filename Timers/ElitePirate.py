from Timers import template
import time

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

def get_timer():
    timer = template.Timer('Images\\ElitePirate.png')
    timer.title = 'The Elite Pirate Has Arrived'
    timer.description = 'Show him who is Really Elite'
    timer.auto_reset_enabled = False
    timer.delay_method = delay_method
    timer.reset_method = reset_method
    return timer
