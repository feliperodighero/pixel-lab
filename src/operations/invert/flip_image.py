from PIL import Image


def flip_horizontal(image: Image.Image) -> Image.Image:
    width, height = image.size
    pixels = image.load()

    new_image = Image.new("RGB", (width, height))
    new_pixels = new_image.load()

    for y in range(height):
        for x in range(width):
            new_pixels[width - x - 1, y] = pixels[x, y]

    return new_image


def flip_vertical(image: Image.Image) -> Image.Image:
    width, height = image.size
    pixels = image.load()

    new_image = Image.new("RGB", (width, height))
    new_pixels = new_image.load()

    for y in range(height):
        for x in range(width):
            new_pixels[x, height - y - 1] = pixels[x, y]

    return new_image
