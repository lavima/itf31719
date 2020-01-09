import sys
import numpy
from skimage import io,util

# Read in image
image = io.imread("M101.jpg")

#io.imshow(image)
#io.show()

# Decide how many images
num = int(sys.argv[1])
noised_images = []
for i in range(num):
  noised_images.append(util.random_noise(image,mode='gaussian',var=0.05))
  #io.imshow(noised_images[i])
  #io.show()

# Sum the images together and divide by the number of images
averaged_image = sum(noised_images)/num

# Show the result
io.imshow(averaged_image)
io.show()

  

