import numpy as np
from .dilation import dilation_filter
from .erosion import erosion_filter
from PIL import Image


def closing_filter(img: Image, structure_size: int = 3) -> Image:
    image_array = np.array(img.convert("L"))
    binary_image = (image_array > 128).astype(np.uint8) * 255
    binary_pil = Image.fromarray(binary_image.astype(np.uint8))

    dilated = dilation_filter(binary_pil, structure_size)
    closed = erosion_filter(dilated, structure_size)
    return closed
