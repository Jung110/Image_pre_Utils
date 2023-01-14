# Image_utils

---



```python
def find_specific_format_file(file_dir , file_format):
```

- file_dir 경로에 있는 파일중 file_format 형식을 가지는 파일의 경로 리스트를 반환

---



```python
def replace_class(  file_path, 
                    save_dir_name, 
                    old_txt ,
                    new_txt , 
                    sep = ' ',
                    check = False):
```

- file_path 에 있는 데이터 클래스를 저장하는 파일을 sep를 기준으로 읽어 old_txt 인 클래스를 new_txt값으로 바꾸어 준다.

- 그 후 해당 파일을 save_dir_name에 저장한다.

- check 여부에 따라 해당 과정을 출력할 수 있다.

---



```python
def make_save_path(file_path,save_dir_name):
```

- file_path 경로에 save_dir_name의 경로가 없는 경우  save_dir_name 생성하는 함수

---



```python
def replace_class_in_dir(file_dir ,
                         file_format,
                         save_dir_name,old_txt, 
                         new_txt , 
                         sep = ' ' , 
                         check = False):
```

- file_path 에 있는 데이터 클래스를 저장하는 파일을 sep를 기준으로 읽어 old_txt 인 클래스를 new_txt값으로 바꾸어 준다.

- 그 후 해당 파일을 save_dir_name에 저장한다.

- check 여부에 따라 해당 과정을 출력할 수 있다.

----

```python
def compare_each_format_count(format1 : str,
                             format2 : str,
                             path : str) -> None:
```

- 각각 format1, format2 형식인 이름은 같고 format만 다른 파일의 이름을 추출

- 위를 이용하여 어노테이션이 없는 이미지 데이터나 어노테이션만 있는 이미지 데이터를 알아낼 수 있다. 

---



```python
def frame_cut(top_dir: str,
              format_name: str,
              frame_count: int):
```

- top_dir에 있는 format_name형식의 동영상 파일을 frame_count 프레임 마다 하나씩 이미지로 저장 

---



```python
class Annotation_Converter
```

- json형식으로 되어있는 영상의 어노테이션을 프레임 별 자른 이미지의 어노테이션으로 변경

---

---


