import  numpy as np
import matplotlib.image as mpimg
import math

class Image:
    file = ''

    # Main data is where modifications are made, and the version before the modification is stored in the secondary_data
    main_data = np.zeros(shape=(0, 0, 3))

    # Secondary data should work as a CTRL+Z
    secondary_data = np.zeros(shape=(0, 0, 3))

    # For easier access
    x_size = 0
    y_size = 0

    def __init__(self, path):
        self.file = path
        self.main_data = mpimg.imread(path)
        self.x_size = self.main_data.shape[1]
        self.y_size = self.main_data.shape[0]

    def store_secondary(self):
        self.secondary_data = self.main_data

    # Should receive tuples to identify the coordinates to crop the image
    def crop (self, start, end):
        self.store_secondary()
        self.main_data = self.main_data[start[0]:end[0], start[1]:end[1]]

    # V for vertical and H for horizontal
    def flip(self, direction):
        self.secondary_data = self.main_data

        if direction.lower() == 'v':
            self.main_data = np.flip(self.main_data, 0)
        elif direction.lower() == 'h':
            self.main_data = np.flip(self.main_data, 1)

    # Should receive the angle to rotate the image
    def rotate(self, angle):
        pass

    # Should receive a tuple of the new dimensions -- OBS: X first, Y second
    def resize(self, new_size):
        self.secondary_data = self.main_data

        x_factor = self.x_size / new_size[0]
        y_factor = self.y_size / new_size[1]

        y_coords = np.arange(new_size[1]) * y_factor
        x_coords = np.arange(new_size[0]) * x_factor

        y_indices = np.floor(y_coords).astype(int)
        x_indices = np.floor(x_coords).astype(int)

        resized_data = self.main_data[y_indices[:, None], x_indices[None, :], :]

        self.main_data = resized_data

    def grey(self):
        self.secondary_data = self.main_data

        # Sum all the colors, then divide by the number of color channels
        colors_sum = np.sum(self.main_data, axis=2)
        colors_sum = colors_sum / 3

        self.main_data[:,:,:] = np.stack((colors_sum, colors_sum, colors_sum), axis=2)