from PIL import Image, ExifTags

img = Image.open("IMG_2264.jpg")
for i, j in img._getexif().items():
    if i in ExifTags.TAGS:
        print(ExifTags.TAGS[i] + " - " + str(j))