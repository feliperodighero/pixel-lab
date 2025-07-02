from PIL import Image


def dilation_filter(img: Image.Image, structure_size: int = 3) -> Image.Image:
    img = img.convert("L")
    width, height = img.size
    pixels = img.load()

    offset = structure_size // 2

    binary = [[1 if pixels[x, y] > 128 else 0 for x in range(width)] for y in range(height)]

    dilated = [[0 for _ in range(width)] for _ in range(height)]

    for y in range(offset, height - offset):
        for x in range(offset, width - offset):
            dilate_pixel = 0
            for dy in range(-offset, offset + 1):
                for dx in range(-offset, offset + 1):
                    if binary[y + dy][x + dx] == 1:
                        dilate_pixel = 1
                        break
                if dilate_pixel == 1:
                    break

            dilated[y][x] = dilate_pixel

    new_img = Image.new("L", (width, height))
    new_pixels = new_img.load()

    for y in range(height):
        for x in range(width):
            new_pixels[x, y] = 255 if dilated[y][x] == 1 else 0

    return new_img
