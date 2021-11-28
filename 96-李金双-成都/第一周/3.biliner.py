# coding: utf-8
# Author：Jason
# Date ：2021/11/28 10:03 上午
# Tool ：PyCharm
import numpy as np


def biliner(src_img, size):

    h, w, c = src_img.shape

    if (w, h) == size:
        return src_img.copy()
    dst_img = np.zeros((size[1], size[0], c))

    h_scale = h / size[1]
    w_scale = w / size[0]
    for i in range(h):
        for j in range(w):
            src_h = (i - 0.5) * h_scale - 0.5
            src_w = (i - 0.5) * w_scale - 0.5

            src_h1 = min(src_h + 1, h - 1)
            src_w1 = min(src_w + 1, w - 1)

            r1 = (src_w1 - j) * src_img[src_h, src_w] + (j - src_w) * src_img[src_h, src_w1]
            r2 = (src_w1 - j) * src_img[src_w, src_h1] + (j - src_w) * src_img[src_w1, src_w1]

            dst_img[i, j] = (src_h1 - i) * r1 + (i - src_h) * r2
    return dst_img