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
import memo
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

#----------------------------------------------------------------------------------------
# digital clock
#----------------------------------------------------------------------------------------

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
    ascii_canvas.add_text(x, y + 0, line1[sec//10] + " " + line1[sec%10])
    ascii_canvas.add_text(x, y + 1, line2[sec//10] + " " + line2[sec%10])
    ascii_canvas.add_text(x, y + 2, line3[sec//10] + " " + line3[sec%10])
    ascii_canvas.add_text(x, y + 3, line4[sec//10] + " " + line4[sec%10])
    ascii_canvas.add_text(x, y + 4, line5[sec//10] + " " + line5[sec%10])
    ascii_canvas.add_text(x, y + 5, line6[sec//10] + " " + line6[sec%10])
    ascii_canvas.add_text(x, y + 6, line7[sec//10] + " " + line7[sec%10])
    ascii_canvas.add_text(x, y + 7, line8[sec//10] + " " + line8[sec%10])
    ascii_canvas.add_text(x, y + 8, line9[sec//10] + " " + line9[sec%10])


def draw_digital_minute_hand(ascii_canvas, x, y, min):
    """
    Draw minute hand
    """
    ascii_canvas.add_text(x, y + 0, line1[min//10] + " " + line1[min%10] + " ")
    ascii_canvas.add_text(x, y + 1, line2[min//10] + " " + line2[min%10] + " ")
    ascii_canvas.add_text(x, y + 2, line3[min//10] + " " + line3[min%10] + " ")
    ascii_canvas.add_text(x, y + 3, line4[min//10] + " " + line4[min%10] + " ")
    ascii_canvas.add_text(x, y + 4, line5[min//10] + " " + line5[min%10] + " ")
    ascii_canvas.add_text(x, y + 5, line6[min//10] + " " + line6[min%10] + " ")
    ascii_canvas.add_text(x, y + 6, line7[min//10] + " " + line7[min%10] + " ")
    ascii_canvas.add_text(x, y + 7, line8[min//10] + " " + line8[min%10] + " ")
    ascii_canvas.add_text(x, y + 8, line9[min//10] + " " + line9[min%10] + " ")


def draw_digital_hour_hand(ascii_canvas, x, y, hour):
    """
    Draw hour hand
    """
    ascii_canvas.add_text(x, y + 0, line1[hour//10] + " " + line1[hour%10] + " ")
    ascii_canvas.add_text(x, y + 1, line2[hour//10] + " " + line2[hour%10] + " ")
    ascii_canvas.add_text(x, y + 2, line3[hour//10] + " " + line3[hour%10] + " ")
    ascii_canvas.add_text(x, y + 3, line4[hour//10] + " " + line4[hour%10] + " ")
    ascii_canvas.add_text(x, y + 4, line5[hour//10] + " " + line5[hour%10] + " ")
    ascii_canvas.add_text(x, y + 5, line6[hour//10] + " " + line6[hour%10] + " ")
    ascii_canvas.add_text(x, y + 6, line7[hour//10] + " " + line7[hour%10] + " ")
    ascii_canvas.add_text(x, y + 7, line8[hour//10] + " " + line8[hour%10] + " ")
    ascii_canvas.add_text(x, y + 8, line9[hour//10] + " " + line9[hour%10] + " ")

def draw_digital_calendar(ascii_canvas, startday, lastday, today):

    x, y = 95, 24
    ascii_canvas.add_text(x, y, Back.RED + Fore.WHITE + '[' + str(Y) + '/' + str(M).rjust(2, '0') + '/' + str(todays).rjust(2, '0') + ']' + Fore.WHITE)

    x, y = 87, y + 1
    ascii_canvas.add_text(x, y, '----------------------------')

    x, y = 86, y + 1
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
        #x = x + 3
        ascii_canvas.add_text(x, y, msg + Fore.WHITE)
        msg = ''
        y = y + 1
        if k % 2 == 0:
           x = 86
        else:
           x = 87

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
    ascii_canvas.add_text(25, 18, 'ooooooooooooooooooooooooooooooooooooooooooooooooooooooo')
    ascii_canvas.add_text(25, 19, 'o                                                     o')
    ascii_canvas.add_text(25, 20, 'o' + location + ' ' + temperature + '\" o')
    ascii_canvas.add_text(25, 21, 'o                                                     o')
    ascii_canvas.add_text(25, 22, 'ooooooooooooooooooooooooooooooooooooooooooooooooooooooo')
    
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
    ascii_canvas.add_text(25, y, '<Infomation>')
    ascii_canvas.add_text(25, y + 2, '  [    key:  year - 1')
    ascii_canvas.add_text(25, y + 4, '  ]    key:  year + 1')
    ascii_canvas.add_text(25, y + 6, '  <    key: month - 1')
    ascii_canvas.add_text(25, y + 8, '  >    key: month + 1')
    ascii_canvas.add_text(25, y + 10, 'enter  key:   go memo')
    ascii_canvas.add_text(51, y + 2, '|')
    ascii_canvas.add_text(51, y + 3, '|')
    ascii_canvas.add_text(51, y + 4, '|')
    ascii_canvas.add_text(51, y + 5, '|')
    ascii_canvas.add_text(51, y + 6, '|')
    ascii_canvas.add_text(51, y + 7, '|')
    ascii_canvas.add_text(51, y + 8, '|')
    ascii_canvas.add_text(51, y + 9, '|')
    ascii_canvas.add_text(51, y + 10, '|')
    ascii_canvas.add_text(53, y + 2, '  →   key:   day + 1')
    ascii_canvas.add_text(53, y + 4, '  ←   key:   day - 1')
    ascii_canvas.add_text(53, y + 6, '  ↑   key:   day - 7')
    ascii_canvas.add_text(53, y + 8, '  ↓   key:   day + 7')
    ascii_canvas.add_text(53, y + 10, 'slash  key:   change clock')

     #draw change mode
    x, y = 87, 20
    ascii_canvas.add_text(x, y, '[ ] Analog')
    x, y = 104, 20
    ascii_canvas.add_text(x, y,  Style.BRIGHT + Fore.YELLOW + '[v] Digital' + Style.DIM)

    # print out canvas
    ascii_canvas.print_out()

#----------------------------------------------------------------------------------------
# analog clock
#----------------------------------------------------------------------------------------
def draw_second_hand(ascii_canvas, seconds, length, fill_char):
    """
    Draw second hand
    """
    x0 = int(math.ceil(ascii_canvas.cols / 4.0))
    y0 = int(math.ceil(ascii_canvas.lines / 2.0))
    x1 = x0 + int(math.cos((seconds + 45) * 6 * math.pi / 180) * length * x_scale_ratio)
    y1 = y0 + int(math.sin((seconds + 45) * 6 * math.pi / 180) * length)
    ascii_canvas.add_line(int(x0), int(y0), int(x1), int(y1), fill_char=fill_char)


def draw_minute_hand(ascii_canvas, minutes, length, fill_char):
    """
    Draw minute hand
    """
    x0 = int(math.ceil(ascii_canvas.cols / 4.0))
    y0 = int(math.ceil(ascii_canvas.lines / 2.0))
    x1 = x0 + int(math.cos((minutes + 45) * 6 * math.pi / 180) * length * x_scale_ratio)
    y1 = y0 + int(math.sin((minutes + 45) * 6 * math.pi / 180) * length)
    ascii_canvas.add_line(int(x0), int(y0), int(x1), int(y1), fill_char=fill_char)


def draw_hour_hand(ascii_canvas, hours, minutes, length, fill_char):
    """
    Draw hour hand
    """
    x0 = int(math.ceil(ascii_canvas.cols / 4.0))
    y0 = int(math.ceil(ascii_canvas.lines / 2.0))
    total_hours = hours + minutes / 60.0
    x1 = x0 + int(math.cos((total_hours + 45) * 30 * math.pi / 180) * length * x_scale_ratio)
    y1 = y0 + int(math.sin((total_hours + 45) * 30 * math.pi / 180) * length)
    ascii_canvas.add_line(int(x0), int(y0), int(x1), int(y1), fill_char=fill_char)


def draw_clock_face(ascii_canvas, radius, mark_char):
    """
    Draw clock face with hour and minute marks
    """
    x0 = ascii_canvas.cols // 4
    y0 = ascii_canvas.lines // 2
    # draw marks first
    for mark in range(1, 12 * 5 + 1):
        x1 = x0 + int(math.cos((mark + 45) * 6 * math.pi / 180) * radius * x_scale_ratio)
        y1 = y0 + int(math.sin((mark + 45) * 6 * math.pi / 180) * radius)
        if mark % 5 != 0:
            ascii_canvas.add_text(x1, y1, mark_char)
    # start from 1 because at 0 index - 12 hour
    for mark in range(1, 12 + 1):
        x1 = x0 + int(math.cos((mark + 45) * 30 * math.pi / 180) * radius * x_scale_ratio)
        y1 = y0 + int(math.sin((mark + 45) * 30 * math.pi / 180) * radius)
        ascii_canvas.add_text(x1, y1, '%s' % mark)

def draw_calendar(ascii_canvas, startday, lastday, today):

    x, y = 78, 13
    ascii_canvas.add_text(x, y, Back.RED + Fore.WHITE + '[' + str(Y) + '/' + str(M).rjust(2, '0') + '/' + str(todays).rjust(2, '0') + ']' + Fore.WHITE)

    x, y = 70, 14
    ascii_canvas.add_text(x, y, '----------------------------')

    x, y = 70, 15
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

                    # msg = msg + Fore.RED + str(m).rjust(4, ' ')
                    # ascii_canvas.add_text(x, y, str(m).rjust(3, ' '))
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
        x = 70

def draw_clock(cols, lines):
    """
    Draw clock
    """
    if cols < 25 or lines < 25:
        print('Too little columns/lines for print out the clock!')
        exit()
    # prepare chars
    single_line_border_chars = ('.', '-', '.', '|', ' ', '|', '`', '-', "'")
    second_hand_char = '.'
    minute_hand_char = '#'
    hour_hand_char = '+'
    mark_char = '`'
    if os.name == 'nt':
        single_line_border_chars = ('.', '-', '.', '|', ' ', '|', '`', '-', "'")  # ('\xDA', '\xC4', '\xBF', '\xB3', '\x20', '\xB3', '\xC0', '\xC4', '\xD9')
        second_hand_char = '.'  # '\xFA'
        minute_hand_char = '#'  # '\xF9'
        hour_hand_char = '+'  # 'o'
        mark_char = '`'  # '\xF9'
    # create ascii canvas for clock and eval vars
    ascii_canvas = AsciiCanvas(cols * 2, lines)
    center_x = int(math.ceil(cols / 4.0))
    center_y = int(math.ceil(lines / 2.0))
    radius = center_y - 5
    second_hand_length = int(radius / 1.17)
    minute_hand_length = int(radius / 1.25)
    hour_hand_length = int(radius / 1.95)
    # add clock region and clock face
    ascii_canvas.add_rect(5, 3, int(math.floor(cols / 2.0)) * 2 - 9, int(math.floor(lines / 2.0)) * 2 - 5)
    draw_clock_face(ascii_canvas, radius, mark_char)
    now = datetime.datetime.now()
    # add regions with weekday and day if possible
    if center_x > 25:
        left_pos = int(radius * x_scale_ratio) / 2 - 4
        ascii_canvas.add_nine_patch_rect(int(center_x + left_pos), int(center_y - 1), 5, 3, single_line_border_chars)
        ascii_canvas.add_text(int(center_x + left_pos + 1), int(center_y), now.strftime('%a'))
        ascii_canvas.add_nine_patch_rect(int(center_x + left_pos + 5), int(center_y - 1), 4, 3, single_line_border_chars)
        ascii_canvas.add_text(int(center_x + left_pos + 1 + 5), int(center_y), now.strftime('%d'))
    # add clock hands
    draw_second_hand(ascii_canvas, now.second, second_hand_length, fill_char=second_hand_char)
    draw_minute_hand(ascii_canvas, now.minute, minute_hand_length, fill_char=minute_hand_char)
    draw_hour_hand(ascii_canvas, now.hour, now.minute, hour_hand_length, fill_char=hour_hand_char)

    # draw weather
    global location
    global temperature
    y = 6
    ascii_canvas.add_text(70, y + 0, 'oooooooooooooooooooooooooooooooooooooooooooooooooooooo')
    ascii_canvas.add_text(70, y + 1, 'o                                                    o')
    ascii_canvas.add_text(70, y + 2, 'o' + location + ' ' + temperature + '\"o')
    ascii_canvas.add_text(70, y + 3, 'o                                                    o')
    ascii_canvas.add_text(70, y + 4, 'oooooooooooooooooooooooooooooooooooooooooooooooooooooo')

    # draw calendar
    global todays
    global lastday
    global startday
    global Y
    global M
    startday, lastday = calendar.calendar(Y, M)
    draw_calendar(ascii_canvas, startday, lastday, todays)

    #draw info
    y = 25
    ascii_canvas.add_text(70, y, '<Infomation>')
    ascii_canvas.add_text(70, y + 2, '  [    key:  year - 1')
    ascii_canvas.add_text(70, y + 4, '  ]    key:  year + 1')
    ascii_canvas.add_text(70, y + 6, '  <    key: month - 1')
    ascii_canvas.add_text(70, y + 8, '  >    key: month + 1')
    ascii_canvas.add_text(70, y + 10, 'enter  key:   go memo')
    ascii_canvas.add_text(92, y + 2, '|')
    ascii_canvas.add_text(92, y + 3, '|')
    ascii_canvas.add_text(92, y + 4, '|')
    ascii_canvas.add_text(92, y + 5, '|')
    ascii_canvas.add_text(92, y + 6, '|')
    ascii_canvas.add_text(92, y + 7, '|')
    ascii_canvas.add_text(92, y + 8, '|')
    ascii_canvas.add_text(92, y + 9, '|')
    ascii_canvas.add_text(92, y + 10, '|')
    ascii_canvas.add_text(94, y + 2, '  →   key:   day + 1')
    ascii_canvas.add_text(94, y + 4, '  ←   key:   day - 1')
    ascii_canvas.add_text(94, y + 6, '  ↑   key:   day - 7')
    ascii_canvas.add_text(94, y + 8, '  ↓   key:   day + 7')
    ascii_canvas.add_text(94, y + 10, 'slash  key:   change clock')

    #draw change mode
    x, y = 70, 4
    ascii_canvas.add_text(x, y, Style.BRIGHT + Fore.YELLOW + '[v] Analog' + Style.DIM)
    x, y = 100, 4
    ascii_canvas.add_text(x, y, '[ ] Digital')


    # print out canvas
    ascii_canvas.print_out()

def main():
    global todays
    global lastday
    global Y
    global M

    check = 1
    savecheck = check

    lines = 40
    cols = int(lines * x_scale_ratio)
    # set console window size and screen buffer size
    if os.name == 'nt':
        os.system('mode con: cols=%s lines=%s' % (cols * 2 + 1, lines + 1))
    while True:
        # try:        
            # for key in keys:
            #     if keyboard.is_pressed(key):
            #         print(keyboard.key_to_scan_codes(key))
            #         print(f"{key} pressed")

        if keyboard.is_pressed('esc'):
            if check == 2:
                check = savecheck
            else:
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

        elif keyboard.is_pressed('<'):
            M = M - 1
            time.sleep(0.1)
        
        elif keyboard.is_pressed('>'):
            M = M + 1
            time.sleep(0.1)

        elif keyboard.is_pressed('['):
            Y = Y - 1
            time.sleep(0.1)

        elif keyboard.is_pressed(']'):
            Y = Y + 1
            time.sleep(0.1)

        elif keyboard.is_pressed('/'):
            if check == 1:
                check = 0
            else:
                check = 1

        elif keyboard.is_pressed('enter'):
            if check != 2:
                savecheck = check
                check = 2
            time.sleep(0.1)

        # except:
        #     print('except')
        #     break

        os.system('cls' if os.name == 'nt' else 'clear')
        if check == 1:
            draw_clock(cols, lines)
        elif check == 0:
            draw_digital_clock(cols, lines)
        elif check == 2:
            memo.main(cols, lines, Y, M, todays)
            check = savecheck
        time.sleep(0.2)


if __name__ == '__main__':
    main()
