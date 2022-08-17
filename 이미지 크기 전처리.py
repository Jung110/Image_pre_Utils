import tensorflow as tf
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
from tensorflow.image import pad_to_bounding_box
from tensorflow.image import central_crop
from tensorflow.image import resize

import numpy as np
import os

def image_padding(img_vector, file_name):
    #padding 실시 : pad_to_bounding_box 사용 
    img_vector_pad = pad_to_bounding_box(img_vector, 
                                         int((target_height-source_height)/2), 
                                         int((target_width-source_width)/2), 
                                         target_height, 
                                         target_width)

     #이미지 형태 확인 
    print(img_vector_pad.shape)

    #이미지 확인 
    plt.imshow(img_vector_pad)
    plt.show()

    #이미지 저장 
    image.save_img(file_name, img_vector_pad)
    

#이미지의 변경할 크기 설정 
target_height = 224
target_width = 224

READ_PATH = 'c:/dataset/original'
SAVE_PATH = 'c:/dataset/resized'

#이미지 불러오기
file_list = os.listdir(READ_PATH)
for file in file_list:
    READ_PATH = f'{READ_PATH}/{file}'
    SAVE_PATH = f'{SAVE_PATH}/{file}'
    file_list = os.listdir(READ_PATH)
    for car_image  in file_list:
        img = image.load_img(f'{READ_PATH}/{car_image}')
        img_vector = image.img_to_array(img)
        img_vector = img_vector/255
        
        #현재 이미지의 크기 지정 
        source_height = img_vector.shape[0]
        source_width = img_vector.shape[1]
        
        # 원본 이미지의 가로/세로 크기가 224 미만인 경우에는 Padding 처리
        if (source_height < 224) & (source_width < 224):
            image_padding(img_vector, f'{SAVE_PATH}/{car_image}')
        # 가로 또는 세로의 크기가 224 초과일 경우에는 가로, 세로 중 큰 쪽 사이즈를 224로 맞추고 작은쪽 사이즈를 원본 이미지의 가로/세로 비율에 맞춰 리사이징
        else:
            if source_height > source_width:
                shorten_ratio = target_height / source_height
                source_height = target_height
                source_width = int(source_width * shorten_ratio)        
            elif source_width > source_height:
                shorten_ratio = target_width / source_width
                source_width = target_width
                source_height = int(source_height * shorten_ratio)
            else:
                source_height = target_height
                source_width = target_width

            #print(f'source size:({source_height},{source_width})')
            img_vector_resize = resize(img_vector, (source_height, source_width))
            image_padding(img_vector_resize, f'{SAVE_PATH}/{car_image}')

    READ_PATH = 'c:/dataset/original'
    SAVE_PATH = 'c:/dataset/resized'
