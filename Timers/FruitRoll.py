from PIL import Image, ImageTk
import time
import json

imagePath = 'Images\\FruitRoll.png'

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

image = ImageTk.PhotoImage(Image.open(imagePath).resize((50, 50)))
