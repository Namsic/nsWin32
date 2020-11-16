import win32api, win32gui
import time, threading

MOUSE_MOVE = 0x0001
MOUSE_LEFTDOWN = 0x0002
MOUSE_LEFTUP = 0x0004
MOUSE_RIGHTDOWN = 0x0008
MOUSE_RIGHTUP = 0x0010
MOUSE_WHEEL = 0x0800

key_code = {
    # mouse
    'mouse_left': 0x01, 'mouse_right': 0x02, 
    # func_1
    'backspace': 0x08,
    'tab': 0x09,
    'enter':0x0D,
    'shift':0x10,
    'ctrl': 0x11,
    'alt': 0x12,
    'capslock': 0x14,
    'hangul': 0x15,
    'esc': 0x1B,
    'space': 0x20,
    'pageup': 0x21,
    'pagedown': 0x22,
    'end': 0x23,
    'home': 0x24,
    'left': 0x25, 'up': 0x26, 'right': 0x27, 'down': 0x28,
    'insert': 0x2D,
    'delete': 0x2E,
    'window': 0x5B,
    # number
    '0': 0x30, '1': 0x31, '2': 0x32, '3': 0x33, '4': 0x34, '5': 0x35, '6': 0x36, '7': 0x37, '8': 0x38, '9': 0x39,
    # alphabet
    'a': 0x41, 'b': 0x42, 'c': 0x43, 'd': 0x44, 'e': 0x45, 'f': 0x46, 'g': 0x47, 'h': 0x48, 'i': 0x49, 'j': 0x4A,
    'k': 0x4B, 'l': 0x4C, 'm': 0x4D, 'n': 0x4E, 'o': 0x4F, 'p': 0x50, 'q': 0x51, 'r': 0x52, 's': 0x53, 't': 0x54,
    'u': 0x55, 'v': 0x56, 'w': 0x57, 'x': 0x58, 'y': 0x59, 'z': 0x5A,
    # numpad
    'num0': 0x60, 'num1': 0x61, 'num2': 0x62, 'num3': 0x63, 'num4': 0x64,
    'num5': 0x65, 'num6': 0x66, 'num7': 0x67, 'num8': 0x68, 'num9': 0x69,
    '*': 0x6A, '+': 0x6B, 'numenter': 0x6C,
    'num-': 0x6D, 'num.': 0x6E, 'num/': 0x6F,
    # f1 ~ f12
    'f1': 0x70, 'f2': 0x71, 'f3': 0x72, 'f4': 0x73, 'f5': 0x74, 'f6': 0x75,
    'f7': 0x76, 'f8': 0x77, 'f9': 0x78, 'f10': 0x79, 'f11': 0x7A, 'f12': 0x7B,
    # func_2
    'numlock': 0x90,
    ';': 0xBA, '=': 0xBB, ',': 0xBC, '-': 0xBD, '.': 0xBE, '/': 0xBF, 
    '`': 0xC0,
    '[': 0xDB, '\\': 0xDC, ']': 0xDD,  "'": 0xDE,
    # with Shift
    '!': ('shift', '1'), '@': ('shift', '2'), '#': ('shift', '3'), '$': ('shift', '4'), '%': ('shift', '5'),
    '^': ('shift', '6'), '&': ('shift', '7'), '(': ('shift', '9'), ')': ('shift', '0'), '|': ('shift', '\\'),
    '~': ('shift', '`'), '_': ('shift', '-'), 
    '!': ('shift', '1'), '!': ('shift', '1'), 
    'A': ('shift', 'a'), 'B': ('shift', 'b'), 'C': ('shift', 'c'), 'D': ('shift', 'd'), 'E': ('shift', 'e'), 
    'F': ('shift', 'f'), 'G': ('shift', 'g'), 'H': ('shift', 'h'), 'I': ('shift', 'i'), 'J': ('shift', 'j'),
    'K': ('shift', 'k'), 'L': ('shift', 'l'), 'M': ('shift', 'm'), 'N': ('shift', 'n'), 'O': ('shift', 'o'),
    'P': ('shift', 'p'), 'Q': ('shift', 'q'), 'R': ('shift', 'r'), 'S': ('shift', 's'), 'T': ('shift', 't'),
    'U': ('shift', 'u'), 'V': ('shift', 'v'), 'W': ('shift', 'w'), 'X': ('shift', 'x'), 'Y': ('shift', 'y'),
    'Z': ('shift', 'z'), 
    ':': ('shift', ';'), '?': ('shift', '/')
    }


class Mouse:
    def position(x=None, y=None, relative=False):
        x0, y0 = win32api.GetCursorPos()
        if x == None:
            x = x0
        if y == None:
            y = y0

        if relative:
            win32api.SetCursorPos( (x0+x, y0+y) )
        else:
            win32api.SetCursorPos( (x, y) )
        return x, y


    def down(btn_type=0):
        if btn_type == 0:
            e_code = 0x0002
        else:
            e_code = 0x0008
        win32api.mouse_event(e_code, 0, 0, 0, 0)


    def up(btn_type=0):
        if btn_type == 0:
            e_code = 0x0004
        else:
            e_code = 0x0010
        win32api.mouse_event(e_code, 0, 0, 0, 0)


    def click(x=None, y=None, relative=False, comeback=True, btn_type=0):
        x0, y0 = win32api.GetCursorPos()

        Mouse.position(x, y, relative)

        Mouse.down(btn_type)
        Mouse.up(btn_type)
        
        if comeback:
            Mouse.position(x0, y0)


    def wheel(amount):
        win32api.mouse_event(MOUSE_WHEEL, 0, 0, amount, 0)


class Keyboard:
    def down(k):
        if type(key_code[k]) == list or type(key_code[k]) == tuple:
            for e in key_code[k]:
                win32api.keybd_event(key_code[e], 0, 0x00, 0)
        else:
            win32api.keybd_event(key_code[k], 0, 0x00, 0)


    def up(k):
        if type(key_code[k]) == list or type(key_code[k]) == tuple:
            for e in key_code[k]:
                win32api.keybd_event(key_code[e], 0, 0x02, 0)
        else:
            win32api.keybd_event(key_code[k], 0, 0x02, 0)


    def press(k):
        if type(k) == list or type(k) == tuple:
            for e in k:
                Keyboard.down(e)
            for e in k:
                Keyboard.up(e)
        else:
            Keyboard.down(k)
            Keyboard.up(k)


    def input_str(s):
        for c in s:
            Keyboard.press(c)


class Event:
    detect_pause = False
    on_detect = True
    
    def check(target):
        if type(target) == list or type(target) == tuple:
            for e in target:
                if not win32api.GetAsyncKeyState(key_code[e]) & 0x8000:
                    return False
            return True
        else:
            return win32api.GetAsyncKeyState(key_code[target]) & 0x8000


    def event(cmd, func, args):
        while Event.on_detect:
            if Event.detect_pause:
                continue
            
            if Event.check(cmd):
                while Event.check(cmd):
                    pass
                if args == None:
                    func()
                elif type(args) != tuple:
                    func(args)
                else:
                    func(*args)


    def add(cmd, func, args=None):
        tmp_t = threading.Thread(target=Event.event, args=(cmd, func, args))
        tmp_t.daemon = True
        tmp_t.start()


    def detect(func, stop_command=('ctrl', 'f1')):
        pressed = []
        Event.add(stop_command, Event.stop)
        while Event.on_detect:
            if Event.detect_pause:
                continue
            
            for k in key_code:
                if type(key_code[k]) == tuple:
                    continue
                if k not in pressed and Event.check(k):
                    pressed.append(k)
                    func(k, True)
                if k in pressed and not Event.check(k):
                    pressed.remove(k)
                    func(k, False)
    def pause():
        Event.detect_pause = not Event.detect_pause
    def stop():
        Event.on_detect = False


class Window:
    width = win32api.GetSystemMetrics(0)
    height = win32api.GetSystemMetrics(1)


    def handle(w_title, position=None, size=None, active=False):
        hwnd = win32gui.FindWindow(None, w_title)
        info = win32gui.GetWindowRect(hwnd)
        if position == None:
            x, y = info[0:2]
        else:
            x, y = position
        
        if size == None:
            w, h = (info[2]-info[0], info[3]-info[1])
        else:
            w, h = size
        win32gui.MoveWindow(hwnd, x, y, w, h, True)
        if active:
            win32gui.SetForegroundWindow(hwnd)
        return x, y, w, h



if __name__ == '__main__':
    before_press = None
    before_mouse = None
    def print_action(key, press):
        global before_press, before_mouse
        if press:
            output = '[_Pressed] '
            before_press = key
            before_mouse = Mouse.position()
        else:
            if key == before_press:
                if key[:5] != "mouse":
                    return
                elif before_mouse == Mouse.position():
                    return
            output = '[Released] '
        print(output + key)
        if key[:5] == "mouse":
            x, y = Mouse.position()
            print("    x:", x)
            print("    y:", y)

    Event.detect(print_action)
