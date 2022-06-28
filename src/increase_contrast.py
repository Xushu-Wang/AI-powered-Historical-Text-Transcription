from PIL import Image, ImageOps, ImageEnhance
import pytesseract

image = Image.open("img.jpg")

if image.mode == 'RGBA':
    r,g,b,a = image.split()
    image = Image.merge('RGB', (r,g,b))

image = ImageOps.invert(image)

contrast = ImageEnhance.Color(image)
image = contrast.enhance(2)

txt = pytesseract.image_to_string(image, config = r"--psm 6", lang='eng')

print(txt)