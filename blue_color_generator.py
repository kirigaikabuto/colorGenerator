# Import required image modules
from PIL import Image, ImageColor

path = "color1/"
blue_images = ["blue", "skyblue", "#4169E1", "#0892D0", "#2A52BE"]

for color in blue_images:
    for i in range(100):
        img = Image.new("RGB", (256, 256), ImageColor.getrgb(color))
        photo_name = f"{color}-{i}.png"
        img.save(path + photo_name)
