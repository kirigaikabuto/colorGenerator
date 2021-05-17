# Import required image modules
from PIL import Image, ImageColor

path = "color2/"
blue_images = ["#651C32", "#732039", "#E10600", "#A10500", "#C70700"]

for color in blue_images:
    for i in range(100):
        img = Image.new("RGB", (256, 256), ImageColor.getrgb(color))
        photo_name = f"{color}-{i}.png"
        img.save(path + photo_name)
