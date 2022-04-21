import numpy as np
import cv2
import argparse
import matplotlib.pyplot as plt
import re

def load_pfm(file):
    color = None
    width = None
    height = None
    scale = None
    data_type = None
    header = file.readline().decode('UTF-8').rstrip()

    if header == 'PF':
        color = True
    elif header == 'Pf':
        color = False
    else:
        raise Exception('Not a PFM file.')
    dim_match = re.match(r'^(\d+)\s(\d+)\s$', file.readline().decode('UTF-8'))
    if dim_match:
        width, height = map(int, dim_match.groups())
    else:
        raise Exception('Malformed PFM header.')
    # scale = float(file.readline().rstrip())
    scale = float((file.readline()).decode('UTF-8').rstrip())
    if scale < 0: # little-endian
        data_type = '<f'
    else:
        data_type = '>f' # big-endian
    data_string = file.read()
    data = np.fromstring(data_string, data_type)
    shape = (height, width, 3) if color else (height, width)
    data = np.reshape(data, shape)
    data = cv2.flip(data, 0)
    return data

if __name__ == '__main__':
    depth_path = './outputs_012/outputs_012/scan114/confidence/00000023.pfm'

    depth_image = load_pfm(open(depth_path, 'rb'))
    ma = np.ma.masked_equal(depth_image, 0.0, copy=False)
    print('value range: ', ma.min(), ma.max())


    depth_path = './outputs_012/outputs_012/scan114/depth_est/00000023.pfm'

    depth_image1 = load_pfm(open(depth_path, 'rb'))
    ma = np.ma.masked_equal(depth_image, 0.0, copy=False)
    print('value range: ', ma.min(), ma.max())
    # plt.imshow(depth_image, 'rainbow')
    # plt.show()
    # show two images side by side
    plt.subplot(1, 2, 1)
    # invert the colors for the first image
    depth_image = ma.max() - depth_image
    plt.imshow(depth_image, 'rainbow')
    plt.subplot(1, 2, 2)
    plt.imshow(depth_image1, 'rainbow')
    plt.show()