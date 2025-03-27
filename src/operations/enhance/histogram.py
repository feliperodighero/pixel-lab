from PIL import Image


def histogram_equalization(image: Image.Image) -> Image.Image:
    width, height = image.size
    pixels = image.load()

    hist = [0] * 256
    for y in range(height):
        for x in range(width):
            hist[pixels[x, y]] += 1

    cdf = [0] * 256
    cdf[0] = hist[0]
    for i in range(1, 256):
        cdf[i] = cdf[i - 1] + hist[i]

    min_cdf = min([v for v in cdf if v > 0])
    total_pixels = width * height

    equalized_map = [
        (cdf[i] - min_cdf) * 255 // (total_pixels - min_cdf) for i in range(256)
    ]

    new_image = Image.new("L", (width, height))
    new_pixels = new_image.load()
    for y in range(height):
        for x in range(width):
            new_pixels[x, y] = equalized_map[pixels[x, y]]

    return new_image
