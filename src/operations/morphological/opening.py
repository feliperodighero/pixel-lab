import numpy as np
from PIL import Image

from .dilation import dilation_filter
from .erosion import erosion_filter


def opening_filter(img: Image, structure_size: int = 3) -> Image:
    image_array = np.array(img.convert("L"))
    binary_image = (image_array > 128).astype(np.uint8) * 255
    binary_pil = Image.fromarray(binary_image.astype(np.uint8))

    eroded = erosion_filter(binary_pil, structure_size)
    opened = dilation_filter(eroded, structure_size)
    return opened
