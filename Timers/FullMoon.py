from Timers import template
import time

def cycle_moon(cycles: int | float = 1):
    cycle_time = 24*60
    return cycle_time * cycles

def delay_method(_):
    now = time.time()
    delay = cycle_moon(2) - 5*60 # set to sunrise
    end = now + delay
    return end

def reset_method(_):
    now = time.time()
    delay = cycle_moon(8)
    end = now + delay
    return end

def get_timer():
    timer = template.Timer()
    timer.image_path = 'Images\\FullMoon.png'
    timer.title = 'The Moon will be Full Tonight.'
    timer.description = 'Race to the danger zones, because its time to hunt kitsune island!'
    timer.auto_reset_delay = 0
    timer.delay_method = delay_method
    timer.reset_method = reset_method
    return timer
