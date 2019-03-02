from pynput import keyboard
from pynput.keyboard import Key, Controller

virtual_keyboard = Controller()

xf86_play = 269025044
xf86_prev = 269025046
xf86_next = 269025047

virtual_keyboard.press(keyboard.KeyCode.from_vk(269025044))
virtual_keyboard.release(keyboard.KeyCode.from_vk(269025044))