import ns_win32


# relative coordinates for the window
keyboard = {
    'esc': (10, 56), '`': (32, 56), '1': (54, 56), '2': (76, 56), '3': (98, 56), '4': (120, 56), '5': (142, 56),
    '6': (164, 56), '7': (186, 56), '8': (208, 56), '9': (230, 56), '0': (252, 56), '-': (274, 56), '=': (296, 56),
    'backspace': (328, 56), 'tab': (15, 78), 'q': (44, 78), 'w': (66, 78), 'e': (88, 78), 'r': (110, 78),
    't': (132, 78), 'y': (154, 78), 'u': (176, 78), 'i': (198, 78), 'o': (220, 78), 'p': (242, 78), '[': (264, 78),
    ']': (286, 78), '\\': (308, 78), 'del': (333, 78), 'caps': (20, 100), 'a': (56, 100), 's': (78, 100), 'd': (100, 100),
    'f': (122, 100), 'g': (144, 100), 'h': (166, 100), 'j': (188, 100), 'k': (210, 100), 'l': (232, 100), ';': (254, 100),
    "'": (276, 100), 'enter': (315, 100), 'shift': (26, 122), 'z': (66, 122), 'x': (88, 122), 'c': (110, 122), 'v': (132, 122),
    'b': (154, 122), 'n': (176, 122), 'm': (198, 122), ',': (220, 122), '.': (242, 122), '/': (264, 122),
    'r_shift': (324, 122), 'func': (11, 144), 'ctrl': (33, 144), 'win': (55, 144), 'alt': (76, 144), 'hanja': (104, 144),
    'space': (160, 144), 'hangul': (215, 144),
    }


# init OnScreenKeyboard
# C:\Windows\System32\osk.exe
# def init_keyboard():
keyPos = ns_win32.window_set('화상 키보드', (1355, 885), size=(576, 173))


def config_keyboard():
    keyPos = ns_win32.window_set('화상 키보드')


# click OnScreenKeyboard
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
    pass
