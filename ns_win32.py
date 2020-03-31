import win32api, win32gui, win32con
import time
import subprocess

MOUSE_MOVE = 0x0001
MOUSE_LEFTDOWN = 0x0002
MOUSE_LEFTUP = 0x0004
MOUSE_RIGHTDOWN = 0x0008
MOUSE_RIGHTUP = 0x0010
MOUSE_WHEEL = 0x0800


def mouse_click(x, y):
    before_pos = win32api.GetCursorPos()
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(MOUSE_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    win32api.SetCursorPos(before_pos)


def keyboard_press(k):
    win32api.keybd_event(k, 0, 0x00, 0)  # KeyDown
    win32api.keybd_event(k, 0, 0x02, 0)  # KeyUp

if __name__ == '__main__':
    time.sleep(3)
    print('s')
    #key_press(0x25)
    key_press(0x0D)
    print('e')
