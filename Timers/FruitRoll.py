from Timers import template
import time
import json

def delay_method(savedatajsonpath):
    with open(savedatajsonpath, 'r') as f:
        savedata_json = json.load(f)
    return savedata_json['NextRollEpoch']

def reset_method(savedatajsonpath):
    now = time.time()
    delay = 2*60*60
    end = now + delay
    with open(savedatajsonpath, 'r') as f:
        savedata_json = json.load(f)
    savedata_json['NextRollEpoch'] = end
    with open(savedatajsonpath, 'w') as f:
        json.dump(savedata_json, f, indent=4)
    return end

def get_timer():
    timer = template.Timer('Images\\FruitRoll.png')
    timer.title = 'You can now Roll a Fruit.'
    timer.description = 'The Blox Fruit Gacha has Something for You :>'
    timer.auto_reset_enabled = False
    timer.delay_method = delay_method
    timer.reset_method = reset_method
    return timer
