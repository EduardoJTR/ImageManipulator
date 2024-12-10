from commands import *
from im_image import IM_Image


img = IM_Image('')

# Should split the arguments in a list
def split_args(command):
    return command


def handle_args(command: str):
    args = split_args(command)

    if args[0] == 'help':
        print_help()
    elif args[0] == 'open' and len(args) > 0:
        open_img(args, img)
    elif args[0] == 'check':
        check_file(img)
    elif args[0] == 'cancel':
        cancel(img)
    elif args[0] == 'display':
        display(img)
    elif args[0] == 'exit':
        return False

    return True



if __name__ == '__main__':
    run = True
    while run:
        command = input()
        run = handle_args(command)