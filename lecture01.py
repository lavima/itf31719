from skimage import io

# Assigment 1
image = io.imread("lena.png")

# Assignment 2
height, width, _ = image.shape
center_vertical = height // 2
center_horizontal = width // 2

subimage1 = image[0:center_vertical,0:center_horizontal]
subimage2 = image[0:center_vertical,center_horizontal:width]
subimage3 = image[center_vertical:height,0:center_horizontal]
subimage4 = image[center_vertical:height,center_horizontal:width]

io.imshow(image) 
io.show()
io.imshow(subimage1) 
io.show()
io.imshow(subimage2) 
io.show()
io.imshow(subimage3) 
io.show()
io.imshow(subimage4) 
io.show()

#Assigment 3
io.imsave("lena_sub1.png", subimage1)
