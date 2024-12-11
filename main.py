from commands import *
from im_image import IM_Image


img = IM_Image('')

def in_quotes(command: str):
    first_quote = -1
    second_quote = -1
    for i in range(len(command)):
        if first_quote == -1 and command[i] == '\'':
            first_quote = i
        elif first_quote != -1 and command[i] == '\'':
            second_quote = i
    return command[first_quote + 1:second_quote]


# Should split the arguments in a list
def split_args(command: str):
    if '\'' not in command:
        return command.split(' ')
    else:
        splited = command.split(' ')
        return [splited[0], in_quotes(command)]




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
    elif args[0] == 'crop' and len(args) == 5:
        crop(args, img)
    elif args[0] == 'flip' and len(args) == 2:
        flip(args, img)
    elif args[0] == 'rotate' and len(args) == 2:
        rotate(args, img)
    elif args[0] == 'resize' and len(args) == 3:
        resize(args, img)
    elif args[0] == 'grey':
        grey(img)
    return True



if __name__ == '__main__':
    run = True
    while run:
        command = input()
        run = handle_args(command)