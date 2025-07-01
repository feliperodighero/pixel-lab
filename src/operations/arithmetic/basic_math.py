from PIL import Image


def multiply_image(img: Image.Image, factor: float) -> Image.Image:
    img = img.convert("RGB")
    width, height = img.size
    new_img = Image.new("RGB", (width, height))

    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            r = min(int(r * factor), 255)
            g = min(int(g * factor), 255)
            b = min(int(b * factor), 255)
            new_img.putpixel((x, y), (r, g, b))

    return new_img


def divide_image(img: Image.Image, factor: float) -> Image.Image:
    img = img.convert("RGB")
    width, height = img.size
    new_img = Image.new("RGB", (width, height))

    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            divisor = factor if factor != 0 else 1
            r = min(int(r / divisor), 255)
            g = min(int(g / divisor), 255)
            b = min(int(b / divisor), 255)
            new_img.putpixel((x, y), (r, g, b))

    return new_img
