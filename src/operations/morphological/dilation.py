import numpy as np
from PIL import Image


def dilation_filter(img: Image, structure_size: int = 3) -> Image:
    image_gray = img.convert("L")
    image_array = np.array(image_gray)

    binary_image = (image_array > 128).astype(np.uint8)

    height, width = binary_image.shape
    dilated_image = np.zeros((height, width), dtype=np.uint8)

    offset = structure_size // 2

    for i in range(offset, height - offset):
        for j in range(offset, width - offset):
            if np.any(
                binary_image[i - offset : i + offset + 1, j - offset : j + offset + 1]
                == 1
            ):
                dilated_image[i, j] = 1

    return Image.fromarray((dilated_image * 255).astype(np.uint8))
