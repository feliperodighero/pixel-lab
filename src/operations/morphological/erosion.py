from PIL import Image

def erosion_filter(img: Image.Image, structure_size: int = 3) -> Image.Image:
    img = img.convert("L")
    width, height = img.size
    pixels = img.load()

    offset = structure_size // 2

    binary = [[1 if pixels[x, y] > 128 else 0 for x in range(width)] for y in range(height)]
    eroded = [[1 for _ in range(width)] for _ in range(height)]

    for y in range(offset, height - offset):
        for x in range(offset, width - offset):
            erode_pixel = 1
            for dy in range(-offset, offset + 1):
                for dx in range(-offset, offset + 1):
                    if binary[y + dy][x + dx] == 0:
                        erode_pixel = 0
                        break
                if erode_pixel == 0:
                    break

            eroded[y][x] = erode_pixel

    new_img = Image.new("L", (width, height))
    new_pixels = new_img.load()

    for y in range(height):
        for x in range(width):
            new_pixels[x, y] = 255 if eroded[y][x] == 1 else 0

    return new_img
