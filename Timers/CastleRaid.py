from Timers import template
import time

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

def get_timer() -> template.Timer:
    timer = template.Timer('Images\\CastleRaid.png')
    timer.title = 'The Castle is Under Attack!'
    timer.description = 'Defeat their Leader and Claim its Treasures'
    timer.auto_reset_delay = 360
    timer.delay_method = delay_method
    timer.reset_method = reset_method
    return timer
