import  numpy as np
import matplotlib.image as plt

class Image:
    file = ''
    data = np.zeros(shape=(0, 0, 3))

    def __init__(self, path):
        self.file = path
        data = plt.imread(self.file)