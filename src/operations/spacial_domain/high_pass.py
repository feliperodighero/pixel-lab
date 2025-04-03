import numpy as np
from PIL import Image
from scipy.ndimage import convolve


def prewitt_filter(image: Image.Image) -> Image.Image:
    image_array = np.array(image.convert("L"))
    height, width = image_array.shape
    new_image = np.zeros((height, width))

    Gx = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    Gy = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

    pad = 1
    padded_image = np.pad(image_array, pad, mode="edge")

    for y in range(height):
        for x in range(width):
            region = padded_image[y : y + 3, x : x + 3]
            gx = np.sum(Gx * region)
            gy = np.sum(Gy * region)
            new_image[y, x] = np.sqrt(gx**2 + gy**2)

    new_image = (new_image / new_image.max()) * 255
    return Image.fromarray(new_image.astype(np.uint8))


def sobel_filter(image: Image.Image) -> Image.Image:
    image_array = np.array(image.convert("L"))
    height, width = image_array.shape
    new_image = np.zeros((height, width))

    Gx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    Gy = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

    pad = 1
    padded_image = np.pad(image_array, pad, mode="edge")

    for y in range(height):
        for x in range(width):
            region = padded_image[y : y + 3, x : x + 3]
            gx = np.sum(Gx * region)
            gy = np.sum(Gy * region)
            new_image[y, x] = np.sqrt(gx**2 + gy**2)

    new_image = (new_image / new_image.max()) * 255
    return Image.fromarray(new_image.astype(np.uint8))


def laplacian_filter(img: Image, kernel_type: str = "4-neighbors") -> Image:
    image_gray = img.convert("L")
    image_array = np.array(image_gray, dtype=np.float32)

    kernels = {
        "4-neighbors": np.array(
            [[0, -1, 0], [-1, 4, -1], [0, -1, 0]], dtype=np.float32
        ),
        "8-neighbors": np.array(
            [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]], dtype=np.float32
        ),
    }

    kernel = kernels.get(kernel_type, kernels["4-neighbors"])

    filtered_image = convolve(image_array, kernel, mode="reflect")

    filtered_image = np.clip(filtered_image, 0, 255).astype(np.uint8)

    return Image.fromarray(filtered_image)
