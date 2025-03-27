from PIL import Image


def blend_images(image1: Image.Image, image2: Image.Image, alpha: float) -> Image.Image:
    width, height = image1.size
    pixels1 = image1.load()
    pixels2 = image2.load()

    new_image = Image.new("RGB", (width, height))
    new_pixels = new_image.load()

    for y in range(height):
        for x in range(width):
            r1, g1, b1 = pixels1[x, y]
            r2, g2, b2 = pixels2[x, y]

            r_new = int(alpha * r1 + (1 - alpha) * r2)
            g_new = int(alpha * g1 + (1 - alpha) * g2)
            b_new = int(alpha * b1 + (1 - alpha) * b2)

            new_pixels[x, y] = (r_new, g_new, b_new)

    return new_image


def average_images(image1: Image.Image, image2: Image.Image) -> Image.Image:
    width, height = image1.size
    pixels1 = image1.load()
    pixels2 = image2.load()

    new_image = Image.new("RGB", (width, height))
    new_pixels = new_image.load()

    for y in range(height):
        for x in range(width):
            r1, g1, b1 = pixels1[x, y]
            r2, g2, b2 = pixels2[x, y]

            r_new = (r1 + r2) // 2
            g_new = (g1 + g2) // 2
            b_new = (b1 + b2) // 2

            new_pixels[x, y] = (r_new, g_new, b_new)

    return new_image
