from PIL import Image
import  numpy as np
import math

class IM_Image:
    file = ''

    # Main data is where modifications are made, and the version before the modification is stored in the secondary_data
    main_data = np.zeros(shape=(0, 0, 3))

    # Secondary data should work as a CTRL+Z
    secondary_data = np.zeros(shape=(0, 0, 3))

    # For easier access
    x_size = 0
    y_size = 0

    def __init__(self, path):
        if path != '':
            self.file = path
            self.main_data = np.array(Image.open(self.file))
            self.x_size = self.main_data.shape[1]
            self.y_size = self.main_data.shape[0]


    def open(self, path):
        self.file = path
        self.main_data = np.array(Image.open(self.file))
        self.x_size = self.main_data.shape[1]
        self.y_size = self.main_data.shape[0]


    def update_main(self, new_main):
        new_main = new_main.astype('uint8')
        self.main_data = new_main
        self.x_size = self.main_data.shape[1]
        self.y_size = self.main_data.shape[0]


    def store_secondary(self):
        self.secondary_data = self.main_data


    # Should receive tuples to identify the coordinates to crop the image
    def crop (self, start, end):
        self.store_secondary()
        self.update_main(self.main_data[start[0]:end[0], start[1]:end[1]])


    # V for vertical and H for horizontal
    def flip(self, direction):
        self.store_secondary()

        if direction.lower() == 'v':
            self.update_main(np.flip(self.main_data, 0))
        elif direction.lower() == 'h':
            self.update_main(np.flip(self.main_data, 1))


    # Should receive the angle to rotate the image
    def rotate(self, angle):
        self.store_secondary()

        # Separates the coordinates of each pixel
        coords = np.zeros((self.y_size, self.x_size, 2))

        # Kind of confusing, this is separating the x and y of each pixels in pairs, in an array with shape:
        # height, width, 2
        coords[:,:,1] = np.tile(np.arange(self.main_data.shape[1]), self.main_data.shape[0]).reshape((
            self.y_size, self.x_size
        ))

        coords[:, :, 0] = np.repeat(np.arange(self.main_data.shape[0]), self.main_data.shape[1], axis=0).reshape((
            self.y_size, self.x_size
        ))

        # Transforms to the origin [0, 0], putting the image at the center
        coords[:,:,0] = coords[:,:,0] - (self.y_size / 2)
        coords[:,:,1] = coords[:,:,1] - (self.x_size / 2)

        rotated_coords = np.zeros((self.y_size, self.x_size, 2))

        # Applies the rotation matrix
        rotated_coords[:,:,0] = coords[:,:,1] * math.sin(math.radians(angle)) + coords[:,:,0] * math.cos(math.radians(angle))
        rotated_coords[:,:,1] = coords[:,:,1] * math.cos(math.radians(angle)) - coords[:,:,0] * math.sin(math.radians(angle))

        top_y_bound = rotated_coords[:,:,0].min()
        left_x_bound = rotated_coords[:, :, 1].min()

        # Transforms so the image has no negative coordinates
        rotated_coords[:,:,0] = rotated_coords[:,:,0] + -top_y_bound
        rotated_coords[:,:,1] = rotated_coords[:,:,1] + -left_x_bound

        bottom_y_bound = math.ceil(rotated_coords[:,:,0].max())
        right_x_bound = math.ceil(rotated_coords[:,:,1].max())

        # Gets the new size of the rotated image
        resized_data = np.zeros((bottom_y_bound, right_x_bound, 3))

        rows = rotated_coords[:,:,1].astype(int)
        cols = rotated_coords[:,:,0].astype(int)

        rows = np.clip(rows, 0, right_x_bound - 1)
        cols = np.clip(cols, 0, bottom_y_bound - 1)

        resized_data[cols, rows,:] = self.main_data[:,:,:]

        self.update_main(resized_data)


    # Should receive a tuple of the new dimensions -- OBS: X first, Y second
    def resize(self, new_size):
        self.store_secondary()

        x_factor = self.x_size / new_size[0]
        y_factor = self.y_size / new_size[1]

        y_coords = np.arange(new_size[1]) * y_factor
        x_coords = np.arange(new_size[0]) * x_factor

        y_indices = np.floor(y_coords).astype(int)
        x_indices = np.floor(x_coords).astype(int)

        resized_data = self.main_data[y_indices[:, None], x_indices[None, :], :]

        self.update_main(resized_data)


    def grey(self):
        self.store_secondary()

        # Sum all the colors, then divide by the number of color channels
        colors_sum = np.sum(self.main_data, axis=2)
        colors_sum = colors_sum / 3

        self.update_main(np.stack((colors_sum, colors_sum, colors_sum), axis=2))


    def reset_main_data(self):
        self.update_main(self.secondary_data)


    def show(self):
        pil_img = Image.fromarray(self.main_data)
        pil_img.show()