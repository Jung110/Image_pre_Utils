# png 파일 흰색 pixel을 투명하게 만들어 주는 코드

from PIL import Image 

img = Image.open('stay.png')
img = img.convert("RGBA")

pixdata = img.load()

width, height = img.size
for y in range(height):
    for x in range(width):
        # 만약 하얀색이면 투명하게 바꾼다. 
        if pixdata[x, y] == (255, 255, 255, 255):
            pixdata[x, y] = (255, 255, 255, 0)

img.save("img_stay.png", "PNG")
