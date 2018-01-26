# coding=utf-8
import math
import operator
from functools import reduce

from PIL import Image

from .ScreenShots import *


class CompareImg(object):
    def __init__(self, device_info):
        self.device_info = device_info
        self.path = device_info["debug_path"]
        self.tmp = os.path.join(self.path, "screenshots.png")
        self.tmp_1 = os.path.join(self.path, "screenshots1.png")

    def compare(self, start_x, start_y, end_x, end_y, app, phone, img, percent=100):
        self.get_screenshot_by_custom_size(start_x, start_y, end_x, end_y)
        baseimg = r".\src\testcase\%s\page\pageImg\%s\%s.png" % (app, phone, img)
        results = self.same_as(baseimg, percent)
        print(results)
        return results

    def same_as(self, baseimg, percent):
        # 对比图片，percent值设为0，则100%相似时返回True，设置的值越大，相差越大
        image1 = Image.open(self.tmp_1)
        image2 = Image.open(baseimg)

        histogram1 = image1.histogram()
        histogram2 = image2.histogram()

        differ = math.sqrt(
            reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, histogram1, histogram2))) / len(histogram1))
        # os.remove(self.tmp)
        # os.remove(self.tmp_1)
        print(differ)
        if differ <= percent:
            return True
        else:
            return False

    def get_screenshot_by_custom_size(self, start_x, start_y, end_x, end_y):
        ScreenShots(self.device_info).screenshots()
        coord = (start_x, start_y, end_x, end_y)
        image = Image.open(self.tmp)
        newImage = image.crop(coord)  # 自定义截取范围 tuple(start_x, start_y, end_x, end_y)
        newImage.save(self.tmp_1)
