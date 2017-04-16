# coding:utf-8
import math
import operator

from PIL import Image

TEMP_FILE =


def same_as(load_image, percent):
    # 对比图片，percent值设为0，则100%相似时返回True，设置的值越大，相差越大
    image1 = Image.open(TEMP_FILE)
    image2 = load_image

    histogram1 = image1.histogram()
    histogram2 = image2.histogram()

    differ = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, \
                                                     histogram1, histogram2))) / len(histogram1))
    if differ <= percent:
        return True
    else:
        return False
