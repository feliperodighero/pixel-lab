from PIL import Image
from .dilation import dilation_filter
from .erosion import erosion_filter


def closing_filter(img: Image.Image, structure_size: int = 3) -> Image.Image:
    img = img.convert("L")
    width, height = img.size
    binary = Image.new("L", (width, height))
    original = img.load()
    bin_pixels = binary .load()

    for y in range(height):
        for x in range(width):
            bin_pixels[x, y] = 255 if original[x, y] > 128 else 0

    dilated = dilation_filter(binary, structure_size)
    closed = erosion_filter(dilated, structure_size)

    return closed

