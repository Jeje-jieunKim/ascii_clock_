import os
import time
import keyboard
from asciicanvas import AsciiCanvas

check = 0
choose = 0
memo_x, memo_y = 0, 0
ascii_canvas_memo = ''

enter_line = list(range(100))
keys = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "enter",
    "backspace",
    "space",
    "esc",
    "ctrl+s"
]

def draw_memo(cols, lines, x, y, specificDate):
    global check
    global choose
    global ascii_canvas_memo

    ascii_canvas = AsciiCanvas(cols * 2, lines)

    ascii_canvas.add_text(0, 0, '[CHECK]: ' + str(check))
    if check == 0:
        if choose == 0:
            ascii_canvas.add_text(x, y + 0, '[Memo Read  ]')
        else:
            ascii_canvas.add_text(x, y + 0, ' Memo Read   ')
        
        if choose == 1:
            ascii_canvas.add_text(x, y + 2, '[Memo Modify]')
        else:
            ascii_canvas.add_text(x, y + 2, ' Memo Modify ')

        if choose == 2:
            ascii_canvas.add_text(x, y + 4, '[Memo Insert]')
        else:
            ascii_canvas.add_text(x, y + 4, ' Memo Insert ')

        if choose == 3:
            ascii_canvas.add_text(x, y + 6, '[Memo Remove]')
        else:
            ascii_canvas.add_text(x, y + 6, ' Memo Remove ')

        # print out canvas
        ascii_canvas.print_out()

    elif check == 1:
        if choose == 0:
            try:
                f = open(specificDate +".txt", 'r')
                for i in range(lines):
                    line = f.readline()
                    ascii_canvas_memo.add_text(0, i, line)
                f.close()
            except:
                print()

            check = 2
        elif choose == 1:
            try:
                f = open(specificDate +".txt", 'r')
                for i in range(lines):
                    line = f.readline()
                    ascii_canvas_memo.add_text(0, i, line)
                f.close()
            except:
                print()
                
            check = 2
        elif choose == 2:
            ascii_canvas_memo.clear()
            check = 2
        elif choose == 3:
            f = open(specificDate +".txt", 'w')
            f.write('')
            f.close()
            check = 0

        # print out canvas
        ascii_canvas.print_out()
    elif check == 2:
        # print out canvas
        ascii_canvas_memo.print_out()

def draw_memo_read():
    return
    
def draw_memo_modify():
    return

def draw_memo_insert():
    return

def draw_memo_remove():
    return

def main(cols, lines, Y, M, D):
    global check
    global choose
    global memo_x, memo_y
    global ascii_canvas_memo

    ascii_canvas_memo = AsciiCanvas(cols * 2, lines, fill_char='\0')

    specificDate = str(Y) + '-' + str(M).rjust(2, '0') + '-' + str(D).rjust(2, '0')

    while True:

        # elif keyboard.is_pressed('left arrow'):
        #     todays = todays - 1
        #     if todays < 1:
        #         todays = 1
        #     time.sleep(0.1)

        # elif keyboard.is_pressed('right arrow'):
        #     todays = todays + 1
        #     if lastday < todays:
        #         todays = lastday
        #     time.sleep(0.1)
        if check == 2:
            for key in keys:
                if keyboard.is_pressed(key):
                    # print(keyboard.key_to_scan_codes(key))
                    # print(f"{key} pressed")
                    if choose != 0:
                        if key == 'backspace':
                            ascii_canvas_memo.add_text(memo_x, memo_y, ' ')
                            memo_x = memo_x - 1
                            if memo_x < 0:
                                memo_y = memo_y - 1
                                memo_x = enter_line[memo_y]
                        elif key == 'space':
                            memo_x = memo_x + 1
                        elif key == 'enter':
                            enter_line[memo_y] = memo_x
                            memo_y = memo_y + 1
                            memo_x = 0
                        elif key == 'ctrl+s':
                            f = open(specificDate +".txt", 'w')
                            f.write(ascii_canvas_memo.get_canvas_as_str())
                            f.close()
                            check = 0
                            print('save_success')
                            time.sleep(2.0)
                        elif key == 'esc':
                            check = 0
                        elif 'a' <= key and key <= 'z':
                            if ascii_canvas_memo.cols < memo_x:
                                enter_line[memo_y] = memo_x
                                memo_x = 0
                                memo_y = memo_y + 1
                            ascii_canvas_memo.add_text(memo_x, memo_y, key)
                            memo_x = memo_x + 1
                        elif '0' <= key and key <= '9':
                            if ascii_canvas_memo.cols < memo_x:
                                enter_line[memo_y] = memo_x
                                memo_x = 0
                                memo_y = memo_y + 1
                            ascii_canvas_memo.add_text(memo_x, memo_y, key)
                            memo_x = memo_x + 1
                    else:
                        if key == 'esc':
                            check = 0
        else:
            if keyboard.is_pressed('esc'):
                break

            elif keyboard.is_pressed('up arrow'):
                choose = choose - 1
                if choose < 0:
                    choose = 0
                time.sleep(0.1)

            elif keyboard.is_pressed('down arrow'):
                choose = choose + 1
                if 3 < choose:
                    choose = 3
                time.sleep(0.1)

            elif keyboard.is_pressed('enter'):
                check = 1

        # elif keyboard.is_pressed('<'):
        #     M = M - 1
        #     time.sleep(0.1)
        
        # elif keyboard.is_pressed('>'):
        #     M = M + 1
        #     time.sleep(0.1)

        # elif keyboard.is_pressed('['):
        #     Y = Y - 1
        #     time.sleep(0.1)

        # elif keyboard.is_pressed(']'):
        #     Y = Y + 1
        #     time.sleep(0.1)

        # elif keyboard.is_pressed('/'):
        #     if check == 1:
        #         check = 0
        #     else:
        #         check = 1

        # elif keyboard.is_pressed('enter'):
        #     if check != 2:
        #         savecheck = check
        #         check = 2
        #     elif check == 2:
        #         if choose == 0:
        #             # 보기
        #             draw_memo_read()
        #         elif choose == 1:
        #             # 수정
        #             draw_memo_modify()
        #         elif choose == 2:
        #             # 삽입
        #             draw_memo_insert()
        #         elif choose == 3:
        #             # 삭제
        #             draw_memo_remove()
        #     time.sleep(0.1)

        os.system('cls' if os.name == 'nt' else 'clear')
        
        draw_memo(cols, lines, 40, 3, specificDate)

        # k = keyboard.read_key()  # in my python interpreter, this captures "enter up"
        # k = keyboard.read_key()  # so repeat the line if in the python interpreter

        # print('k: ' + k)
        # time.sleep(1.1)

        time.sleep(0.1)

if __name__ == '__main__':
    t=time.localtime()
    Y=str(t.tm_year)
    M=str(t.tm_mon)
    D=str(t.tm_mday)
    main(int(40 * 1.75), 40, Y, M, D)