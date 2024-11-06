from PIL import Image, ImageDraw, ImageFont

text = """The from PIL import Image, ImageDraw, ImageFont line imports specific modules
from the Python Imaging Library (PIL), which is also known as the Pillow library in modern Python."""

output_file = "handwriting.png"

# Create an image with white background
image = Image.new("RGB", (2000, 500), (255, 255, 255))
draw = ImageDraw.Draw(image)

# handwriting-style font
try:
    font = ImageFont.truetype("great-vibes/GreatVibes-Regular.ttf", 40)
except IOError:
    font = ImageFont.load_default() 

# Add text to image
draw.text((50, 50), text, font=font, fill=(0, 0, 138))

# Save the image
image.save(output_file)