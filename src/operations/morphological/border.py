import numpy as np
from .erosion import erosion_filter
from PIL import Image


def border_extraction_filter(img: Image, structure_size: int = 3) -> Image:
    image_gray = img.convert("L")
    image_array = np.array(image_gray)
    binary_image = (image_array > 128).astype(np.uint8)

    binary_pil = Image.fromarray((binary_image * 255).astype(np.uint8))
    eroded = erosion_filter(binary_pil, structure_size)
    eroded_array = np.array(eroded) // 255

    border = binary_image - eroded_array
    border = np.clip(border * 255, 0, 255).astype(np.uint8)

    return Image.fromarray(border)
