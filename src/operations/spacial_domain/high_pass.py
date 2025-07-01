import math
from PIL import Image


def prewitt_filter(image: Image.Image) -> Image.Image:
    image = image.convert("L")
    width, height = image.size
    original = image.load()

    Gx = [[-1, 0, 1],
          [-1, 0, 1],
          [-1, 0, 1]]

    Gy = [[-1, -1, -1],
          [ 0,  0,  0],
          [ 1,  1,  1]]

    new_img = Image.new("L", (width, height))
    new_pixels = new_img.load()

    max_grad = 0
    gradients = [[0 for _ in range(width)] for _ in range(height)]

    for y in range(1, height - 1):
        for x in range(1, width - 1):
            total_gx = 0
            total_gy = 0
            for i in range(3):
                for j in range(3):
                    px = x + j - 1
                    py = y + i - 1
                    pixel = original[px, py]
                    total_gx += Gx[i][j] * pixel
                    total_gy += Gy[i][j] * pixel

            grad = int(math.sqrt(total_gx ** 2 + total_gy ** 2))
            gradients[y][x] = grad
            max_grad = max(max_grad, grad)

    for y in range(height):
        for x in range(width):
            valor = int(gradients[y][x] / max_grad * 255) if max_grad > 0 else 0
            new_pixels[x, y] = valor

    return new_img



def sobel_filter(image: Image.Image) -> Image.Image:
    image = image.convert("L")
    width, height = image.size
    original = image.load()

    Gx = [[-1, 0, 1],
          [-2, 0, 2],
          [-1, 0, 1]]

    Gy = [[-1, -2, -1],
          [ 0,  0,  0],
          [ 1,  2,  1]]

    new_img = Image.new("L", (width, height))
    new_pixels = new_img.load()

    max_grad = 0
    gradients = [[0 for _ in range(width)] for _ in range(height)]

    for y in range(1, height - 1):
        for x in range(1, width - 1):
            total_gx = 0
            total_gy = 0
            for i in range(3):
                for j in range(3):
                    px = x + j - 1
                    py = y + i - 1
                    pixel = original[px, py]
                    total_gx += Gx[i][j] * pixel
                    total_gy += Gy[i][j] * pixel

            grad = int(math.sqrt(total_gx ** 2 + total_gy ** 2))
            gradients[y][x] = grad
            max_grad = max(max_grad, grad)

    for y in range(height):
        for x in range(width):
            value = int(gradients[y][x] / max_grad * 255) if max_grad > 0 else 0
            new_pixels[x, y] = value

    return new_img


def laplacian_filter(img: Image.Image, kernel_type: str = "4-neighbors") -> Image.Image:
    img = img.convert("L")
    width, height = img.size
    original = img.load()

    if kernel_type == "8-neighbors":
        kernel = [
            [-1, -1, -1],
            [-1, 8, -1],
            [-1, -1, -1],
        ]
    else:
        kernel = [
            [0, -1, 0],
            [-1, 4, -1],
            [0, -1, 0],
        ]

    pad = 1
    new_img = Image.new("L", (width, height))
    new_pixels = new_img.load()

    for y in range(pad, height - pad):
        for x in range(pad, width - pad):
            total = 0
            for ky in range(3):
                for kx in range(3):
                    px = x + kx - pad
                    py = y + ky - pad
                    pixel = original[px, py]
                    total += kernel[ky][kx] * pixel

            total = max(0, min(255, total))
            new_pixels[x, y] = int(total)

    for y in range(height):
        for x in range(width):
            if x < pad or x >= width - pad or y < pad or y >= height - pad:
                new_pixels[x, y] = original[x, y]

    return new_img
