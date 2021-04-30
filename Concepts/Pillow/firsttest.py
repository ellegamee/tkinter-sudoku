from PIL import Image, ImageDraw, ImageFont, ImageTk

img = Image.new("RGB", (200, 100))
d = ImageDraw.Draw(img)
d.text((20, 20), "Hello", fill=(255, 0, 0))

img.save("test.png")
