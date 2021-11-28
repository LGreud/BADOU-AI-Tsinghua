# coding: utf-8
# Author：Jason
# Date ：2021/11/25 10:35 下午
# Tool ：PyCharm

import numpy as np


def nearest(src_img, size: tuple):

    h, w, c = src_img.shape
    if (w, h) == size:
        return src_img.copy()
    dst_img = np.zeros((size[1], size[0], c))

    h_scale = h / size[1]
    w_scale = w / size[0]

    for i in range(size[1]):
        for j in range(size[0]):
            src_h = int(i / h_scale)
            src_h = min(src_h, h)
            src_w = int(j / w_scale)
            src_w = min(src_w, w)
            dst_img[src_h, src_w] = src_img[src_h, src_w]

    return dst_img








