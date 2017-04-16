# coding:utf-8
import math
import operator

from PIL import Image
from data.Database import *
from src.utils.ReadConf import *


class DiffImg(object):
    def result(self, temp_file, original, comparison):
        self.TEMP_FILE = temp_file
        self.get_screenshot_by_custom_size(tuple(conf_Toast["%s" % comparison]))
        results = self.same_as(r"./screenshots/ORIGINAL_PICTURE/%s" % original, 100)
        return results

    def same_as(self, load_image, percent):
        # 对比图片，percent值设为0，则100%相似时返回True，设置的值越大，相差越大
        image1 = Image.open(r"./screenshots/tmp.png")
        image2 = Image.open(load_image)

        histogram1 = image1.histogram()
        histogram2 = image2.histogram()

        differ = math.sqrt(
            reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, histogram1, histogram2))) / len(histogram1))
        # os.remove(r"./screenshots/tmp.png")
        if differ <= percent:
            return True
        else:
            return False

    def get_screenshot_by_custom_size(self, coord):
        image = Image.open(self.TEMP_FILE)
        newImage = image.crop(coord)  # 自定义截取范围 tuple(start_x, start_y, end_x, end_y)
        newImage.save(r"./screenshots/tmp.png")
