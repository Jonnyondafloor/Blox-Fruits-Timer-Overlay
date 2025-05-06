from Timers import template
import time

def is_week_day():
    day_of_week = time.gmtime().tm_wday
    if day_of_week < 5:
        return True
    else:
        return False

def delay_method(_):
    now = time.time()
    delay = 45*60
    if is_week_day():
        delay += 15*60
    end = now + delay
    return end

def reset_method(_):
    now = time.time()
    delay = 45*60
    if is_week_day():
        delay += 15*60
    end = now + delay
    return end

def get_timer():
    timer = template.Timer('Images\\FruitSpawn.png')
    timer.title = 'A Fruit has Spawned'
    timer.description = 'Search the Sea for the Fruit that be'
    timer.auto_reset_delay = 1200
    timer.delay_method = delay_method
    timer.reset_method = reset_method
    return timer
