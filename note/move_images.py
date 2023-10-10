'''
노션에서 붙여넣은 마크다운 파일 바꾸는 프로그램

'''


import os.path
import os
import re

MD_FILE_PATH = './2023-10-06.md'
NOTE_FILE_PATH = 'note'


os.chdir(NOTE_FILE_PATH)
files = os.getcwd()
print('현재 경로:',files)
print('바꿀 파일:', MD_FILE_PATH)
enter = input('현재 경로가 맞으면 y를 입력하세요: ')
if enter == "y" or enter == 'Y':

    # image.png -> image-0.png 
    if 'image.png' in os.listdir(files):
        os.rename('image.png', 'image-0.png')

    # 하위로 이동해서 시작번호 알아오기
    os.chdir('note_image')
    note_image_dir = os.getcwd()
    image_files = sorted(os.listdir(note_image_dir))
    start = int((image_files[-1].replace('.png', '')).split('-')[1]) + 1

    # 위로 이동해서 바꾸기
    # 이미지 파일만 모으기
    made_images = [x for x in os.listdir(files) if '.png' in x]
    os.chdir('..')
    # print(made_images)
    for i, x in enumerate(made_images):
        os.rename(f"./{x}", f"./note_image/image-{start+i}.png")

    # 마크다운 파일 변경
    p = re.compile('image.*[.]png')
    new_file = ''
    print(start)
    with open(MD_FILE_PATH, 'r', encoding='utf-8') as f:
        lines  = f.readlines()
        i = 0
        for l in lines:
            m = p.search(l)
            if m:
                print(f"\t{m.group()}이 note_image/image-{start+i}.png로 변경되었습니다.")
                tmp = l.replace(m.group(), f"note_image/image-{start+i}.png")
                new_file += tmp
                i += 1
            else:
                new_file += l

    with open(MD_FILE_PATH, 'w', encoding='utf-8') as f:
        f.write(new_file)
    print('정상적으로 완료되었습니다.')
else:
    print('종료되었습니다.')