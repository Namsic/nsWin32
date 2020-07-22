from PIL import Image
import numpy as np


def extract_binary(num, start=0, end=8):
    res = 0
    for i in range(start, end):
        res += num & (1 << (7-i))
    return res >> (7-i)


def split_binary(num, part_len, n):
    res = np.zeros(n)
    for i in range(n):
        res[i] = extract_binary(num, i*part_len, i*part_len+part_len)
    return res


def hide_image(base_img_arr, target_img_arr, loss):
    t_height, t_width = target_img_arr.shape[:2]

    for row in range(t_height):
        for column in range(t_width):
            for color in range(3):
                base_img_arr[row, column, color] -= base_img_arr[row, column, color] % (1 << loss)
                base_img_arr[row, column, color] += extract_binary(target_img_arr[row, column, color], end=loss)
    Image.fromarray(base_img_arr).save('hide.png')


def seek_image(img_arr, loss):
    i_height, i_width = img_arr.shape[:2]
    for row in range(i_height):
        for column in range(i_width):
            for color in range(3):
                img_arr[row, column, color] = extract_binary(img_arr[row, column, color], 8-loss) << (8-loss)
    Image.fromarray(img_arr).save('seek.png')


if __name__ == '__main__':
    print('1: hide image\n2: seek image')
    if input('>>> ') == '1':
        path = input('base image: ')
        b_img = Image.open(path)
        print(b_img.width, '*', b_img.height)
        
        path = input('target image: ')
        t_img = Image.open(path)

        l = int(input('loss: '))

        print('ing..')
        hide_image(np.array(b_img), np.array(t_img), l)
    else:
        path = input('image: ')
        l = int(input('loss: '))
        
        seek_image(np.array(Image.open(path)), l)
