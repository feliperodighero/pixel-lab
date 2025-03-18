import numpy as np
from PIL import Image


def multiply_image(img, factor):
    arr = np.array(img, dtype=np.float32)
    result = np.clip(arr * factor, 0, 255)
    return Image.fromarray(result.astype(np.uint8))


def divide_image(img, factor):
    arr = np.array(img, dtype=np.float32)
    arr[arr == 0] = 1
    result = np.clip(arr / factor, 0, 255)
    return Image.fromarray(result.astype(np.uint8))
