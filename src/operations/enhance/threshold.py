from PIL import Image


def threshold_image(image: Image.Image, threshold: int) -> Image.Image:
    width, height = image.size
    pixels = image.load()

    new_image = Image.new("1", (width, height))
    new_pixels = new_image.load()

    for y in range(height):
        for x in range(width):
            new_pixels[x, y] = 255 if pixels[x, y] >= threshold else 0

    return new_image
