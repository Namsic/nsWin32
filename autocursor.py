import pyautogui
import ns_win32
# import subprocess

# Position of Keyboard(Esc-coordinate)
# subprocess.run('C:\Windows\System32\osk.exe')
keyPos = [0, 0, 0, 0]
keyPos[0], keyPos[1], keyPos[2], keyPos[3] = pyautogui.locateOnScreen('image/keyboard_layout.png')
print('Keyboard located', keyPos[0:2], '/ Size is', keyPos[2:4])

keyboard = {
    'esc': (10, 12), '`': (32, 12), '1': (54, 12), '2': (76, 12), '3': (98, 12), '4': (120, 12), '5': (142, 12),
    '6': (164, 12), '7': (186, 12), '8': (208, 12), '9': (230, 12), '0': (252, 12), '-': (274, 12), '=': (296, 12),
    'backspace': (328, 12), 'tab': (15, 34), 'q': (44, 34), 'w': (66, 34), 'e': (88, 34), 'r': (110, 34),
    't': (132, 34), 'y': (154, 34), 'u': (176, 34), 'i': (198, 34), 'o': (220, 34), 'p': (242, 34), '[': (264, 34),
    ']': (286, 34), '\\': (308, 34), 'del': (333, 34), 'caps': (20, 56), 'a': (56, 56), 's': (78, 56), 'd': (100, 56),
    'f': (122, 56), 'g': (144, 56), 'h': (166, 56), 'j': (188, 56), 'k': (210, 56), 'l': (232, 56), ';': (254, 56),
    "'": (276, 56), 'enter': (315, 56), 'shift': (26, 78), 'z': (66, 78), 'x': (88, 78), 'c': (110, 78), 'v': (132, 78),
    'b': (154, 78), 'n': (176, 78), 'm': (198, 78), ',': (220, 78), '.': (242, 78), '/': (264, 78),
    'r_shift': (324, 78), 'func': (11, 100), 'ctrl': (33, 100), 'win': (55, 100), 'alt': (76, 100), 'hanja': (104, 100),
    'space': (160, 100), 'hangul': (215, 100),
    }


def click_image(img, comeback=True):
    img_xy = pyautogui.locateOnScreen(img)
    print(str(img) + " / " + str(img_xy))
    ns_win32.mouse_click(img_xy)


def press_key(key, clk=1):
    # print("PressKeyboard: " + str(key))
    # input 'f1 ~ f12' case
    if (not key == 'func') and key[0] == 'f' and len(key) > 1:
        ns_win32.mouse_click(keyPos[0]+keyboard['func'][0], keyPos[1]+keyboard['func'][1])
        ns_win32.mouse_click(keyPos[0]+keyboard[key[1:]][0], keyPos[1]+keyboard[key[1:]][1])
        return
    for i in range(clk):
        ns_win32.mouse_click(keyPos[0] + keyboard[key][0], keyPos[1] + keyboard[key][1])


if __name__ == '__main__':
    press_key('g')
