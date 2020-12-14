# run in Your Terminal : pip install pillow
from PIL import Image

openImage = Image.open('/home/hamza/Pictures/6kw31w.png')

showImage = openImage.show()

# (left, upper, right, lower)
cropBox = (0, 0, 400, 400)
# Cropping The Image:
NewImage = openImage.crop(cropBox)

NewImage.show()


# convert Color
myNewImage = openImage.convert('L')
myNewImage.show()

# if You Need More Go To Docs
# The End
