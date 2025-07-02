from PIL import Image

from .dilation import dilation_filter
from .erosion import erosion_filter


def opening_filter(img: Image.Image, structure_size: int = 3) -> Image.Image:
    img = img.convert("L")
    width, height = img.size
    binaria = Image.new("L", (width, height))
    original = img.load()
    bin_pixels = binaria.load()

    for y in range(height):
        for x in range(width):
            bin_pixels[x, y] = 255 if original[x, y] > 128 else 0

    eroded = erosion_filter(binaria, structure_size)
    opened = dilation_filter(eroded, structure_size)

    return opened

