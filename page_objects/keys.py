from pynput import keyboard
from pynput.keyboard import Controller
import time

class VirtualKeys:

    @staticmethod
    def send_key(gesture_id):
        virtual_keyboard = Controller()
        keys = {
            'play_key':269025044,
            'prev_key':269025046,
            'next_key':269025047,
            'audio_lower_key': 0x1008FF11,
            'audio_higher_key':0x1008FF13
            }
        gesture_ids = {
            0:'play_key',
            1:'prev_key',
            2:'next_key',
            3:'audio_lower_key',
            4:'audio_higher_key'
        }
        key = keys[gesture_ids[gesture_id]]
        steps = 1
        if gesture_id == 3 or gesture_id == 4:
            steps = 11
        for i in range(steps):
            virtual_keyboard.press(keyboard.KeyCode.from_vk(key))
            virtual_keyboard.release(keyboard.KeyCode.from_vk(key))
            time.sleep(0.05)
