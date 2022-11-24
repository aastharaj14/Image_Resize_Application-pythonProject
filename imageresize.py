# Importing Image class from PIL module
from PIL import Image

# Opens a image in RGB mode
im = Image.open(r"C:\Users\Aastharaj\Desktop\image.jpg")

# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size

# Setting the points for cropped image
left = 50
top = height / 2
right = 300
bottom = 3 * height / 2

# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop((left, top, right, bottom))
newsize = (500, 500)
im1 = im1.resize(newsize)
# Shows the image in image viewer
im1.show()
