from PIL import Image, ImageDraw, ImageFont
import random
import sys
import time
import datetime

random.seed(datetime.datetime.now().time().microsecond)
print("seed is: ", random.seed)
# Set the dimensions of the image and the characters to use
width, height = 230, 80
charSet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Set the font and font size to use
font = ImageFont.truetype('arial.ttf', 40)

args = sys.argv
count = int(args[1])
image = []
draw = []

#for k in range(10):
image.append(Image.new('RGB', (width, height), (255, 255, 255)))
draw.append(ImageDraw.Draw(image[0]))

# Generate 6 random characters
captcha = ''
for i in range(6):
    # random.seed(datetime.datetime.now().time().microsecond)
    char = random.choice(charSet)
    captcha += char
    offset_low = int(args[6])
    offset_high = int(args[7])
    offsetter = random.randint(offset_low, offset_high)
    x = offsetter + i * 30
    rgb_low = int(args[4])
    rgb_high = int(args[5])
    y = random.randint(int(args[2]), int(args[3]))*10
    draw[0].text((x, y), captcha[i], fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), font=font)
    # opacity = random.randint(128, 255)  # half to full opacity

file = open("..\\fend\\src\\main\\resources\\com\\sadhu\\storage_section\\solution.txt", "w")
file.write(captcha)

# Adding some amount of noise to the penultimate image
for i in range(2000):
    x = random.randint(0, width-1)
    y = random.randint(0, height-1)
    draw[0].point((x, y), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

# Storing the image, for later retrieval by the frontend
image[0].save(f'..\\fend\\src\\main\\resources\\com\\sadhu\\just_captchas\\captcha{int(args[8])}.png')
print("Image saved at:", f'..\\fend\\src\\main\\resources\\com\\sadhu\\just_captchas\\captcha{int(args[8])}.png')
# image[0].show("Captca0")
