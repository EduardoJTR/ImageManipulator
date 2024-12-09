import matplotlib.pyplot as plt
from image import Image

img = Image('./goya.png')
img.grey()
plt.imshow(img.main_data)

plt.show()