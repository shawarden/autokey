import os
from pynput.keyboard import Controller

keyboard_actual = Controller()

if not store.has_key("pulling"):
    store.set_value("pulling",0)

if store.get_value("pulling") == 0:
    store.set_value("pulling",1)
    keyboard_actual.press('3')
    os.system('~/.config/autokey/scripts/keyrelease.sh 88')
    store.set_value("pulling",0)
    keyboard_actual.release('3')

    

