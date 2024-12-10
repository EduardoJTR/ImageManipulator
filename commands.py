from im_image import IM_Image

def print_help():
    print('help                     - for help')
    print('open <\'path_to_image\'> - to open an image')
    print('check                    - to check the opened image')
    print('display                  - to display the image')
    print('cancel                   - to cancel image modification, like ctrl + z')
    print('clip <x1 y1 x2 y2>       - to crop the image')
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