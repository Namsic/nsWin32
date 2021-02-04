import sys, traceback, os


# import module
from ns_win32 import Mouse, Keyboard, Event


def run(filename):
    # open file
    try:
        f = open(filename)
        source = f.read()
        f.close
    except:
        print("Error: cannot open file\n")
        return False

    # run python script
    try:
        exec(source)
        print('ok')
    except Exception:
        log = traceback.format_exc().strip().split('\n')
        line_num = log[-2].split(', ')[1][-1]
        print('Error: cannot run source file')
        print('  line {}, '.format(line_num) + source.strip().split('\n')[int(line_num)-1])
        print('  ' + log[-1] + '\n')
        return False
    return True


if __name__ == "__main__":
    if len(sys.argv) > 1:
        run(' '.join(sys.argv[1:]))
    else:
        _path = input('filePath: ')
        content = [
            '@echo off',
            os.getcwd() + '\\nsBuilder.exe ' + _path,
            'pause'
            ]
        f = open(_path + '_Run.bat', 'w')
        f.write('\n'.join(content))
        f.close()
