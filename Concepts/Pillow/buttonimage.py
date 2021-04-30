from PIL import Image, ImageDraw, ImageFont, ImageTk

img = Image.new("RGB", (33, 33))
d = ImageDraw.Draw(img)
font = ImageFont.truetype("calibri.ttf", 30)
d.text((9, 3), "7", fill=(255, 255, 255), font=font)

img.save("button.png")
