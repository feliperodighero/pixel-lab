import numpy as np
import scipy.ndimage
from PIL import Image


def max_min_mean_filters(
    image: Image.Image, kernel_size: int, mode: str
) -> Image.Image:
    image_array = np.array(image.convert("L"))
    height, width = image_array.shape
    pad = kernel_size // 2
    new_image = np.zeros_like(image_array)

    for y in range(pad, height - pad):
        for x in range(pad, width - pad):
            region = image_array[y - pad : y + pad + 1, x - pad : x + pad + 1]

            if mode == "max":
                new_image[y, x] = np.max(region)
            elif mode == "min":
                new_image[y, x] = np.min(region)
            elif mode == "mean":
                new_image[y, x] = np.mean(region)

    return Image.fromarray(new_image.astype(np.uint8))


def median_filter(image: Image.Image, kernel_size: int) -> Image.Image:
    image_array = np.array(image.convert("L"))
    height, width = image_array.shape
    pad = kernel_size // 2
    new_image = np.zeros_like(image_array)

    for y in range(pad, height - pad):
        for x in range(pad, width - pad):
            region = image_array[y - pad : y + pad + 1, x - pad : x + pad + 1]
            new_image[y, x] = np.median(region)

    return Image.fromarray(new_image.astype(np.uint8))


def order_filter(image: Image.Image, kernel_size: int, order: int) -> Image.Image:
    image_array = np.array(image.convert("L"))
    height, width = image_array.shape
    pad = kernel_size // 2
    new_image = np.zeros_like(image_array)

    for y in range(pad, height - pad):
        for x in range(pad, width - pad):
            region = image_array[y - pad : y + pad + 1, x - pad : x + pad + 1].flatten()
            region.sort()
            new_image[y, x] = region[min(order, len(region) - 1)]

    return Image.fromarray(new_image.astype(np.uint8))


def conservative_smoothing(image: Image.Image, kernel_size: int) -> Image.Image:
    image_array = np.array(image.convert("L"))
    height, width = image_array.shape
    pad = kernel_size // 2
    new_image = image_array.copy()

    for y in range(pad, height - pad):
        for x in range(pad, width - pad):
            region = image_array[y - pad : y + pad + 1, x - pad : x + pad + 1].flatten()
            min_val, max_val = np.min(region), np.max(region)
            pixel = image_array[y, x]

            if pixel < min_val:
                new_image[y, x] = min_val
            elif pixel > max_val:
                new_image[y, x] = max_val

    return Image.fromarray(new_image.astype(np.uint8))


def gaussian_filter(image: Image.Image, sigma: float) -> Image.Image:
    image_array = np.array(image.convert("L"))
    new_image = scipy.ndimage.gaussian_filter(image_array, sigma=sigma)

    return Image.fromarray(new_image.astype(np.uint8))
