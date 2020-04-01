import win32api, win32gui
import time
import subprocess

MOUSE_MOVE = 0x0001
MOUSE_LEFTDOWN = 0x0002
MOUSE_LEFTUP = 0x0004
MOUSE_RIGHTDOWN = 0x0008
MOUSE_RIGHTUP = 0x0010
MOUSE_WHEEL = 0x0800


def mouse_move(x, y, rel=False):
    x1, y1 = win32api.GetCursorPos()
    if rel:
        win32api.SetCursorPos((x1+x, y1+y))
    else:
        win32api.SetCursorPos((x, y))


def mouse_click(x, y):
    before_pos = win32api.GetCursorPos()
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(MOUSE_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    win32api.SetCursorPos(before_pos)


def keyboard_press(k):
    win32api.keybd_event(k, 0, 0x00, 0)  # KeyDown
    win32api.keybd_event(k, 0, 0x02, 0)  # KeyUp


def window_set(w_title, position=None, size=None):
    hwnd = win32gui.FindWindow(None, w_title)
    info = win32gui.GetWindowRect(hwnd)
    if position == None:
        position = (info[0], info[1])
    if size == None:
        size = (info[2]-info[0], info[3]-info[1])
    win32gui.MoveWindow(hwnd, position[0], position[1], size[0], size[1], True)
    return position


if __name__ == '__main__':
    osk_init()
