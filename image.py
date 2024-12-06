import  numpy as np
import matplotlib.image as mpimg

class Image:
    file = ''

    # Main data is where modifications are made, and the version before the modification is stored in the secondary_data
    main_data = np.zeros(shape=(0, 0, 3))

    # Secondary data should work as a CTRL+Z
    secondary_data = np.zeros(shape=(0, 0, 3))

    def __init__(self, path):
        self.file = path
        self.main_data = mpimg.imread(path)

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

    # Should receive a tuple of the new dimensions
    def resize(self, new_size):
        pass