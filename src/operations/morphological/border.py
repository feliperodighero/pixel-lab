from PIL import Image
from .erosion import erosion_filter


def border_extraction_filter(img: Image.Image, structure_size: int = 3) -> Image.Image:
    img = img.convert("L")
    width, height = img.size
    binary = Image.new("L", (width, height))
    original = img.load()
    bin_pixels = binary.load()

    for y in range(height):
        for x in range(width):
            bin_pixels[x, y] = 255 if original[x, y] > 128 else 0

    eroded = erosion_filter(binary, structure_size)

    pixels_binary = binary.load()
    pixels_eroded = eroded.load()

    border_image = Image.new("L", (width, height))
    border_pixels = border_image.load()

    for y in range(height):
        for x in range(width):
            original_val = 1 if pixels_binary[x, y] == 255 else 0
            eroded_val = 1 if pixels_eroded[x, y] == 255 else 0
            border = max(0, original_val - eroded_val)
            border_pixels[x, y] = 255 if border == 1 else 0

    return border_image
