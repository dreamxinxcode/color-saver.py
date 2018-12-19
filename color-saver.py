from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

hex = input("Enter hex: ")
image = Image.new("RGB", (500, 500), hex)
image.paste(hex, [0,0,image.size[0],image.size[1]])

draw = ImageDraw.Draw(image)
font = ImageFont.truetype("UBraille.ttf", 16)
draw.text((20, 20),"Sample Text",(0,0,255),font=font)

image.save(hex + ".png")
