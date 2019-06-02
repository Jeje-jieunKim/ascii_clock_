import keyboard
import time

keys = [
    "down arrow",
    "up arrow",
    "left arrow",
    "right arrow",
    "enter"
]

while 1:
    try:
        for key in keys:
            if keyboard.is_pressed(key):
                print(keyboard.key_to_scan_codes(key))
                print(f"{key} pressed")
                time.sleep(0.2)

        if keyboard.is_pressed('esc'):
            print(key + " pressed")
            break

    except:
        print('except')
        break

    # if msvcrt.kbhit():
    #     c = msvcrt.getwch()
    #     if c == u'\x1b':  # ESC key  -> exit
    #         print ('\n -- exit ---\n')
    #         time.sleep(1) 
    #         break
    #     # if c == u'\00' or c == u'\xe0':  # function key
    #     #     msvcrt.getwch() # skip function keycode 
    #     # else :
    #     #     msvcrt.putwch(c)
    #     if c == u'\u2194':
    #         print('left')
    #     elif c == u'\u2191':
    #         print('up')
    #     elif c == u'\u2192':
    #         print('right')
    #     elif c == u'\u2193':
    #         print('down')
    #     else:
    #         msvcrt.putwch(c)
