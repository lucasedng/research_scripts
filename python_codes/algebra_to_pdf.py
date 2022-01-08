# pip install -U scikit-image
# pip install Pillow
# pip install opencv-python
# pip install FPDF


from PIL import Image
from io import BytesIO
from os import listdir, remove, mkdir
from os.path import isdir
from fpdf import FPDF
from requests import get
from numpy import array
from cv2 import subtract, split, imwrite
from cv2 import countNonZero, imread



# check if one of the final images is useless
def check_an_image_is_white(image: Image) -> bool:

    white_image_response = get('https://gcdn.pbrd.co/images/stE3OXWK76mr.jpg')
    image_from_url = Image.open(BytesIO(white_image_response.content))
    white_image_on_array = array(image_from_url)

    original_image = imread(f'{image}')
    duplicate_image = original_image[36:866, 36:866]
    difference = subtract(white_image_on_array, duplicate_image)
    blue, green, red = split(difference)

    return (
        True
        if countNonZero(blue) == 0
        and countNonZero(green) == 0
        and countNonZero(red) == 0
        else False
    )


# cuts the lesson image into small images and saves them
def cut_the_image_into_small_blocks(
    image: Image,
    width: int,
    height: int,
    i_index: int,
    j_index: int
) -> None:

    original_image = imread(image)
    cropped_image = original_image[
        width-902:width,
        height-902:height
    ]

    imwrite(f'saved_pic\{i_index}.{j_index}.jpg', cropped_image)

    return None


# saves only the images with the content of the lesson
def save_useful() -> None:

    if not isdir('saved_pic'):
        mkdir('saved_pic')

    for i_index in range(2):
        for j_index in range(11):
            cut_the_image_into_small_blocks(
                'algebra_class.jpg', 902*(i_index+1), 902*(j_index+1),
                i_index, j_index
            )
            if check_an_image_is_white(f'saved_pic\{i_index}.{j_index}.jpg'):
                remove(f'saved_pic\{i_index}.{j_index}.jpg')

    return None


# does exactly what it says
def download_algebra_class() -> None:

    img_data = get(
        'https://i.ibb.co/PjVkpwd/Aula-22-15-12-2021.jpg'
    ).content

    with open('algebra_class.jpg', 'wb') as handler:
        handler.write(img_data)


# turn a collection of .jpgs into a .pdf file
def convert_to_pdf() -> None:

    image_list = [x for x in listdir('saved_pic')]
    cover = open(f'saved_pic\{image_list[0]}')
    width, height = cover.size
    pdf = FPDF(unit="pt", format=[width, height])
    pdf.set_auto_page_break(0)

    for image in image_list:
        pdf.add_page()
        pdf.image(f'saved_pic\{image}', 10, 10)

    pdf.output("algebra_class.pdf")

    return None


def main():
    
    download_algebra_class()
    save_useful()
    convert_to_pdf()


if __name__ == "__main__":
    main()
