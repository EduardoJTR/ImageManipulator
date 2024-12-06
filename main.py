from image import Image
import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np

image = Image('./goya.png')

plt.imshow(image.main_data)
plt.axis('off')

plt.show()