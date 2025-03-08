import numpy as np
from PIL import Image


def adjust_brightness(img: Image, value: int) -> Image:
    image_array = np.array(img)
    new_image = image_array.copy()

    height, width, channels = new_image.shape

    for i in range(height):
        for j in range(width):
            for k in range(channels):
                new_value = int(new_image[i, j, k]) + value
                new_image[i, j, k] = max(0, min(new_value, 255))

    return Image.fromarray(new_image.astype(np.uint8))
