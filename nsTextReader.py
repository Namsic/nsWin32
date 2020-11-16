import sys, traceback


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
        print('complete')
    except Exception:
        log = traceback.format_exc().strip().split('\n')
        line_num = log[-2].split(', ')[1][-1]
        print('Error: cannot run source file')
        print('  line {}, '.format(line_num) + source.strip().split('\n')[int(line_num)-1])
        print('  ' + log[-1] + '\n')
        return False
    return True


def immediate_execution():
    while True:
        filename = input("filename: ")
        if filename == 'exit':
            break        
        run(filename)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run(' '.join(sys.argv[1:]))
    else:
        print('1: 직접 실행하기')
        print('2: 실행파일 만들기')
        type = input('>>>')
        immediate_execution()
