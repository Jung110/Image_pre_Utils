# png 파일 흰색 pixel을 투명하게 만들어 주는 코드
# https://stackoverflow.com/questions/765736/using-pil-to-make-all-white-pixels-transparent
# 이미지 경계 smoothing해주는 예제
# https://note.nkmk.me/en/python-pillow-putalpha/
# 이미지 흑백 반전 (inversion)시키기 예제
# https://note.nkmk.me/en/python-pillow-invert/


# png 이미지 파일 흰색 배경 투명하게 만들기 파이썬 코드
# 원본 이미지를 반전시킨 흑백 이미지를 투명도(alpha값)로 활용

from PIL import Image, ImageOps, ImageFilter


def main():
    for i in img_00: 
    im = Image.open('Stay.png').convert('RGB')
    im_inv = ImageOps.invert(im)
    # im_inv.save('test.png')

    # Image boundary Gaussian blurring 
    im_inv = im_inv.filter(ImageFilter.GaussianBlur(5.0))
    im_inv_L = im_inv.convert('L')
    im_inv.save('test.png')

    # 이미지 픽셀에 투명화 적용
    # alpha = 0(검정): 투명, alpha = 255(흰색): 불투명, 128: 반투명
    im.putalpha(im_inv_L)
    im.save("Stay_trans.png", "PNG")

    
# main 함수 로딩부
if __name__ == '__main__':
    main()
