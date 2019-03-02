from pynput import keyboard
from pynput.keyboard import Controller

virtual_keyboard = Controller()

def send_key(key):
    keys = {
        'play_key':269025044,
        'prev_key':269025046,
        'next_key':269025047,
        'audio_lower_key':0x1008FF11,
        'audio_higher_key':0x1008FF13
        }
    virtual_keyboard.press(keyboard.KeyCode.from_vk(keys[key]))
    virtual_keyboard.release(keyboard.KeyCode.from_vk(keys[key]))