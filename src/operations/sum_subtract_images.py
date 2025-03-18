from PIL import Image


def sum_images(img1, img2):
    pixels1 = img1.load()
    pixels2 = img2.load()
    result_img = Image.new("RGB", img1.size)
    result_pixels = result_img.load()

    for y in range(img1.height):
        for x in range(img1.width):
            r = min(pixels1[x, y][0] + pixels2[x, y][0], 255)
            g = min(pixels1[x, y][1] + pixels2[x, y][1], 255)
            b = min(pixels1[x, y][2] + pixels2[x, y][2], 255)
            result_pixels[x, y] = (r, g, b)

    return result_img


def subtract_images(img1, img2):
    pixels1 = img1.load()
    pixels2 = img2.load()
    result_img = Image.new("RGB", img1.size)
    result_pixels = result_img.load()

    for y in range(img1.height):
        for x in range(img1.width):
            r = max(pixels1[x, y][0] - pixels2[x, y][0], 0)
            g = max(pixels1[x, y][1] - pixels2[x, y][1], 0)
            b = max(pixels1[x, y][2] - pixels2[x, y][2], 0)
            result_pixels[x, y] = (r, g, b)

    return result_img
