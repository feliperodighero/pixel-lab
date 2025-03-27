import numpy as np
from PIL import Image


def adjust_brightness(img: Image, value: int) -> Image:
    image_array = np.array(img)

    if len(image_array.shape) == 3:
        height, width, channels = image_array.shape
    elif len(image_array.shape) == 2:
        height, width = image_array.shape
        channels = 1

    new_image = image_array.copy()

    for i in range(height):
        for j in range(width):
            for k in range(channels):
                new_value = int(new_image[i, j, k]) + value
                new_image[i, j, k] = max(0, min(new_value, 255))

    return Image.fromarray(new_image.astype(np.uint8))
