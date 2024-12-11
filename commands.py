from im_image import IM_Image

def print_help():
    print('help                     - for help')
    print('open <\'path_to_image\'> - to open an image')
    print('check                    - to check the opened image')
    print('display                  - to display the image')
    print('cancel                   - to cancel image modification, like ctrl + z')
    print('crop <x1 y1 x2 y2>       - to crop the image')
    print('flip <H>                 - to flip in horizontal, use V to flip in vertical')
    print('rotate <angle>           - to rotate the image at a certain angle')
    print('resize <width height>    - to resize the image image')
    print('grey                     - to greyscale the image')


def open_img(command, img: IM_Image):

    img.open(command[1])


def check_file(img: IM_Image):
    print(img.file)


def display(img: IM_Image):
    img.show()


def cancel(img: IM_Image):
    img.reset_main_data()

def crop(command, img: IM_Image):
    img.crop((int(command[1]), int(command[2])), (int(command[3]), int(command[4])))

def flip(command, img: IM_Image):
    img.flip(command[1])

def rotate(command, img: IM_Image):
    img.rotate(float(command[1]))

def resize(command, img: IM_Image):
    img.resize((int(command[1]), int(command[2])))

def grey(img:IM_Image):
    img.grey()