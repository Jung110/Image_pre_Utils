# png 파일 흰색 pixel을 투명하게 만들어 주는 코드
# https://stackoverflow.com/questions/765736/using-pil-to-make-all-white-pixels-transparent
# 이미지 경계 smoothing해주는 예제
# https://note.nkmk.me/en/python-pillow-putalpha/


from PIL import Image 

img = Image.open('stay.png')
img = img.convert("RGBA")

pixdata = img.load()

width, height = img.size
for y in range(height):
    for x in range(width):
        if pixdata[x, y] == (255, 255, 255, 255):
            pixdata[x, y] = (255, 255, 255, 0)

img.save("img_stay.png", "PNG")
