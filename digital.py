#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-----------------------------------------------------------------------
# Author: delimitry
#-----------------------------------------------------------------------

import os
import time
import math
import datetime
import keyboard
from asciicanvas import AsciiCanvas
from weather import get_weather
import calendar
from colorama import init, Fore, Back, Style

init(autoreset=True)
x_scale_ratio = 1.75
location, temperature = get_weather()

t=time.localtime()
Y=int(t.tm_year)
M=int(t.tm_mon)
todays = int(t.tm_mday)
startday = 0
lastday = 0

keys = [
    "down arrow",
    "up arrow",
    "left arrow",
    "right arrow",
    "enter",
    "<",
    ">",
    "[",
    "]"
]

line1={1:"        []", 2:"[][][][][]", 3:"[][][][][]", 4:"[]      []", 5:"[][][][][]", 6:"[][][][][]", 7:"[][][][][]", 8:"[][][][][]", 9:"[][][][][]", 0:"[][][][][]"}
line2={1:"        []", 2:"        []", 3:"        []", 4:"[]      []", 5:"[]        ", 6:"[]        ", 7:"        []", 8:"[]      []", 9:"[]      []", 0:"[]      []"}
line3={1:"        []", 2:"        []", 3:"        []", 4:"[]      []", 5:"[]        ", 6:"[]        ", 7:"        []", 8:"[]      []", 9:"[]      []", 0:"[]      []"}
line4={1:"        []", 2:"        []", 3:"        []", 4:"[]      []", 5:"[]        ", 6:"[]        ", 7:"        []", 8:"[]      []", 9:"[]      []", 0:"[]      []"}
line5={1:"        []", 2:"[][][][][]", 3:"[][][][][]", 4:"[][][][][]", 5:"[][][][][]", 6:"[][][][][]", 7:"        []", 8:"[][][][][]", 9:"[][][][][]", 0:"[]      []"}
line6={1:"        []", 2:"[]        ", 3:"        []", 4:"        []", 5:"        []", 6:"[]      []", 7:"        []", 8:"[]      []", 9:"        []", 0:"[]      []"}
line7={1:"        []", 2:"[]        ", 3:"        []", 4:"        []", 5:"        []", 6:"[]      []", 7:"        []", 8:"[]      []", 9:"        []", 0:"[]      []"}
line8={1:"        []", 2:"[]        ", 3:"        []", 4:"        []", 5:"        []", 6:"[]      []", 7:"        []", 8:"[]      []", 9:"        []", 0:"[]      []"}
line9={1:"        []", 2:"[][][][][]", 3:"[][][][][]", 4:"        []", 5:"[][][][][]", 6:"[][][][][]", 7:"        []", 8:"[][][][][]", 9:"[][][][][]", 0:"[][][][][]"}


def draw_digital_second_hand(ascii_canvas, x, y, sec):
    """
    Draw second hand
    """
    ascii_canvas.add_text(x, y + 0, line1[sec//10] + " " + line1[sec%10]);
    ascii_canvas.add_text(x, y + 1, line2[sec//10] + " " + line2[sec%10]);
    ascii_canvas.add_text(x, y + 2, line3[sec//10] + " " + line3[sec%10]);
    ascii_canvas.add_text(x, y + 3, line4[sec//10] + " " + line4[sec%10]);
    ascii_canvas.add_text(x, y + 4, line5[sec//10] + " " + line5[sec%10]);
    ascii_canvas.add_text(x, y + 5, line6[sec//10] + " " + line6[sec%10]);
    ascii_canvas.add_text(x, y + 6, line7[sec//10] + " " + line7[sec%10]);
    ascii_canvas.add_text(x, y + 7, line8[sec//10] + " " + line8[sec%10]);
    ascii_canvas.add_text(x, y + 8, line9[sec//10] + " " + line9[sec%10]);


def draw_digital_minute_hand(ascii_canvas, x, y, min):
    """
    Draw minute hand
    """
    ascii_canvas.add_text(x, y + 0, line1[min//10] + " " + line1[min%10] + " ");
    ascii_canvas.add_text(x, y + 1, line2[min//10] + " " + line2[min%10] + " ");
    ascii_canvas.add_text(x, y + 2, line3[min//10] + " " + line3[min%10] + " ");
    ascii_canvas.add_text(x, y + 3, line4[min//10] + " " + line4[min%10] + " ");
    ascii_canvas.add_text(x, y + 4, line5[min//10] + " " + line5[min%10] + " ");
    ascii_canvas.add_text(x, y + 5, line6[min//10] + " " + line6[min%10] + " ");
    ascii_canvas.add_text(x, y + 6, line7[min//10] + " " + line7[min%10] + " ");
    ascii_canvas.add_text(x, y + 7, line8[min//10] + " " + line8[min%10] + " ");
    ascii_canvas.add_text(x, y + 8, line9[min//10] + " " + line9[min%10] + " ");


def draw_digital_hour_hand(ascii_canvas, x, y, hour):
    """
    Draw hour hand
    """
    ascii_canvas.add_text(x, y + 0, line1[hour//10] + " " + line1[hour%10] + " ");
    ascii_canvas.add_text(x, y + 1, line2[hour//10] + " " + line2[hour%10] + " ");
    ascii_canvas.add_text(x, y + 2, line3[hour//10] + " " + line3[hour%10] + " ");
    ascii_canvas.add_text(x, y + 3, line4[hour//10] + " " + line4[hour%10] + " ");
    ascii_canvas.add_text(x, y + 4, line5[hour//10] + " " + line5[hour%10] + " ");
    ascii_canvas.add_text(x, y + 5, line6[hour//10] + " " + line6[hour%10] + " ");
    ascii_canvas.add_text(x, y + 6, line7[hour//10] + " " + line7[hour%10] + " ");
    ascii_canvas.add_text(x, y + 7, line8[hour//10] + " " + line8[hour%10] + " ");
    ascii_canvas.add_text(x, y + 8, line9[hour//10] + " " + line9[hour%10] + " ");

def draw_digital_calendar(ascii_canvas, startday, lastday, today):

    x, y = 79, 22
    ascii_canvas.add_text(x, y, Back.RED + Fore.WHITE + '[' + str(Y) + '/' + str(M).rjust(2, '0') + '/' + str(todays).rjust(2, '0') + ']' + Fore.WHITE)

    x, y = 71, 23
    ascii_canvas.add_text(x, y, '----------------------------')

    x, y = 71, 24
    ascii_canvas.add_text(x, y, Fore.RED + ' Sun' + Fore.WHITE + ' Mon Tue Wed Thu Fri ' + Fore.CYAN + 'Sat' + Fore.WHITE)

    y = y + 1

    if startday == 6:
        s = 1
    else:
        s = startday + 2

    c = 0
    m = 0

    msg = ''

    for k in range(6):
        for i in range(7):
            c = c + 1
            if c < s:
                x = x + 4
                # ascii_canvas.add_text(x, y, ' '.center(4, ' '))
            else:
                if lastday > m:
                    m = m + 1

                    if m == today:
                        msg = msg + '  ' + Fore.GREEN + str(m).rjust(2, ' ')
                    elif (c - 1) % 7 == 0:
                        msg = msg + Fore.RED + str(m).rjust(4, ' ')
                    #     ascii_canvas.add_text(x, y, Fore.RED + str(m).rjust(3, ' ') + Fore.WHITE)
                    elif c % 7 == 0:
                        msg = msg + Fore.CYAN + str(m).rjust(4, ' ')
                    #     ascii_canvas.add_text(x, y, Fore.CYAN + str(m).rjust(3, ' ') + Fore.WHITE)
                    else:
                        msg = msg + Fore.WHITE + str(m).rjust(4, ' ')
                    #         ascii_canvas.add_text(x, y, str(m).rjust(3, ' '))
            # x = x + 3
        ascii_canvas.add_text(x, y, msg + Fore.WHITE)
        msg = ''
        y = y + 1
        if k % 2 == 0:
            x = 70
        else:
            x = 71

def draw_digital_clock(cols, lines):
    """
    Draw clock
    """
    if cols < 25 or lines < 25:
        print('Too little columns/lines for print out the clock!')
        exit()

    # create ascii canvas for clock and eval vars
    ascii_canvas = AsciiCanvas(cols * 2, lines)
    
    # add clock region and clock face
    now = datetime.datetime.now()
    ascii_canvas.add_rect(27, 2, 86, 15)

    # add clock hands
    x, y = int(math.ceil(ascii_canvas.cols / 4.0)) - 4, 5
    draw_digital_hour_hand(ascii_canvas, x, y, now.hour)
    x = x + 25
    draw_digital_minute_hand(ascii_canvas, x, y, now.minute)
    x = x + 25
    draw_digital_second_hand(ascii_canvas, x, y, now.second)

    # draw weather
    global location
    global temperature
    ascii_canvas.add_text(17, 18, 'ooooooooooooooooooooooooooooooooooooooooooooooooo')
    ascii_canvas.add_text(17, 19, 'o                                               o')
    ascii_canvas.add_text(17, 20, 'o       ' + location + ' ' + temperature + '\"       o')
    ascii_canvas.add_text(17, 21, 'o                                               o')
    ascii_canvas.add_text(17, 22, 'ooooooooooooooooooooooooooooooooooooooooooooooooo')
    
    # draw calendar
    global todays
    global lastday
    global startday
    global Y
    global M
    startday, lastday = calendar.calendar(Y, M)
    draw_digital_calendar(ascii_canvas, startday, lastday, todays)

    #draw info
    y = 24
    ascii_canvas.add_text(17, y, '<Infomation>')
    ascii_canvas.add_text(17, y + 2, '  [    key:  year - 1')
    ascii_canvas.add_text(17, y + 4, '  ]    key:  year + 1')
    ascii_canvas.add_text(17, y + 6, '  <    key: month - 1')
    ascii_canvas.add_text(17, y + 8, '  >    key: month + 1')
    ascii_canvas.add_text(17, y + 10, 'enter  key:   go memo')
    ascii_canvas.add_text(39, y + 2, '|')
    ascii_canvas.add_text(39, y + 3, '|')
    ascii_canvas.add_text(39, y + 4, '|')
    ascii_canvas.add_text(39, y + 5, '|')
    ascii_canvas.add_text(39, y + 6, '|')
    ascii_canvas.add_text(39, y + 7, '|')
    ascii_canvas.add_text(39, y + 8, '|')
    ascii_canvas.add_text(39, y + 9, '|')
    ascii_canvas.add_text(39, y + 10, '|')
    ascii_canvas.add_text(41, y + 2, '  →   key:   day + 1')
    ascii_canvas.add_text(41, y + 4, '  ←   key:   day - 1')
    ascii_canvas.add_text(41, y + 6, '  ↑   key:   day - 7')
    ascii_canvas.add_text(41, y + 8, '  ↓   key:   day + 7')
    ascii_canvas.add_text(41, y + 10, 'slash  key:   change clock')

     #draw change mode
    x, y = 73, 19
    ascii_canvas.add_text(x, y, '[v] Analog')
    x, y = 103, 19
    ascii_canvas.add_text(x, y,  Style.BRIGHT + Fore.YELLOW + '[v] Digital' + Style.DIM)

    # print out canvas
    ascii_canvas.print_out()


def main():
    global todays
    global lastday
    global Y
    global M
    lines = 40
    cols = int(lines * x_scale_ratio)
    # set console window size and screen buffer size
    if os.name == 'nt':
        os.system('mode con: cols=%s lines=%s' % (cols * 2 + 1, lines + 1))
    while True:
        try:        
            # for key in keys:
            #     if keyboard.is_pressed(key):
            #         print(keyboard.key_to_scan_codes(key))
            #         print(f"{key} pressed")

            if keyboard.is_pressed('esc'):
                print(key + " pressed")
                break
                
            elif keyboard.is_pressed('left arrow'):
                todays = todays - 1
                if todays < 1:
                    todays = 1
                time.sleep(0.1)

            elif keyboard.is_pressed('right arrow'):
                todays = todays + 1
                if lastday < todays:
                    todays = lastday
                time.sleep(0.1)
                    
            elif keyboard.is_pressed('up arrow'):
                todays = todays - 7
                if todays < 1:
                    todays = 1
                time.sleep(0.1)

            elif keyboard.is_pressed('down arrow'):
                todays = todays + 7
                if lastday < todays:
                    todays = lastday
                time.sleep(0.1)

            elif keyboard.is_pressed('['):
                M = M - 1
                time.sleep(0.1)
            
            elif keyboard.is_pressed(']'):
                M = M + 1
                time.sleep(0.1)

            elif keyboard.is_pressed('<'):
                Y = Y - 1
                time.sleep(0.1)

            elif keyboard.is_pressed('>'):
                Y = Y + 1
                time.sleep(0.1)

            #elif keyboard.is_pressed('enter'):

                #time.sleep(0.1)


        except:
            print('except')
            break

        os.system('cls' if os.name == 'nt' else 'clear')
        draw_digital_clock(cols, lines)
        time.sleep(0.2)


if __name__ == '__main__':
    main()
