from PIL import Image


def convert_to_binary(image: Image.Image, threshold: int = 128) -> Image.Image:
    width, height = image.size
    pixels = image.load()

    binary_image = Image.new("1", (width, height))
    binary_pixels = binary_image.load()

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            gray = int(0.2989 * r + 0.587 * g + 0.114 * b)
            binary_pixels[x, y] = 255 if gray >= threshold else 0

    return binary_image


def logical_operation(
    image1: Image.Image, image2: Image.Image, operation: str
) -> Image.Image:
    width, height = image1.size
    pixels1 = image1.load()
    pixels2 = image2.load()

    new_image = Image.new("1", (width, height))
    new_pixels = new_image.load()

    for y in range(height):
        for x in range(width):
            p1 = 1 if pixels1[x, y] == 255 else 0
            p2 = 1 if pixels2[x, y] == 255 else 0

            if operation == "AND":
                new_pixels[x, y] = 255 if (p1 & p2) else 0
            elif operation == "OR":
                new_pixels[x, y] = 255 if (p1 | p2) else 0
            elif operation == "XOR":
                new_pixels[x, y] = 255 if (p1 ^ p2) else 0

    return new_image


def logical_not(image: Image.Image) -> Image.Image:
    width, height = image.size
    pixels = image.load()

    new_image = Image.new("1", (width, height))
    new_pixels = new_image.load()

    for y in range(height):
        for x in range(width):
            new_pixels[x, y] = 255 if pixels[x, y] == 0 else 0

    return new_image
