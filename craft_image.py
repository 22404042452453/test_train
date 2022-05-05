from rembg.bg import remove
from PIL import ImageFile
import os
import shutil

ImageFile.LOAD_TRUNCATED_IMAGES = True


def new_pictures():
    if not os.path.isdir("result"):
        os.mkdir("result")
    for filenames in os.listdir('pictures'):
        if filenames[filenames.rfind('.') + 1:] in ['jpg', 'jpeg', 'png']:
            file_start = filenames
            file_end = 'new' + file_start[:-5] + '.png'
            os.chdir('pictures')

            with open(file_start, 'rb') as i:
                os.chdir('../')
                os.chdir('result')
                with open(file_end, 'wb') as o:
                    input = i.read()
                    output = remove(input)
                    o.write(output)
                    os.chdir('../')


    shutil.rmtree('pictures')
    os.chdir('result')


def main():
    new_pictures()


if '__main__' == '__name__':
    main()
