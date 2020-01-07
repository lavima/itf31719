from skimage import io

# Assigment 1
image = io.imread("lena.png")

# Assignment 2
height, width, _ = image.shape
center_vertical = height // 2
center_horizontal = width // 2

subimage1 = image[0:center_vertical,0:center_horizontal]
subimage2 = image[0:center_vertical,center_horizontal:width]

#io.imshow, io.show
