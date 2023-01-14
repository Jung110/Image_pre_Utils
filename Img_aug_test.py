

from PIL import Image, ImageOps, ImageFilter


def main():
    for i in img_00: 
    im = Image.open('Stay.png').convert('RGB')
    # 색반전 
    im_inv = ImageOps.invert(im)
    # im_inv.save('test.png') # 테스트용으로  저장
     
    # 이미지 흐릇하게 필터 
    im_inv = im_inv.filter(ImageFilter.GaussianBlur(5.0))
    # grayScale(회색조로 변환)
    im_inv_L = im_inv.convert('L')
    im_inv.save('test.png')

    im.putalpha(im_inv_L)
    im.save("Stay_trans.png", "PNG")

    
# main 함수 로딩부
if __name__ == '__main__':
    main()
