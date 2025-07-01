import math
from PIL import Image


def max_min_mean_filters(image: Image.Image, kernel_size: int, mode: str) -> Image.Image:
    image = image.convert("L")
    width, height = image.size
    pad = kernel_size // 2

    original_pixels = image.load()

    new_img = Image.new("L", (width, height))
    new_pixels = new_img.load()

    for y in range(pad, height - pad):
        for x in range(pad, width - pad):
            neighbors = []
            for dy in range(-pad, pad + 1):
                for dx in range(-pad, pad + 1):
                    px = x + dx
                    py = y + dy
                    neighbors.append(original_pixels[px, py])

            if mode == "max":
                new_pixels[x, y] = max(neighbors)
            elif mode == "min":
                new_pixels[x, y] = min(neighbors)
            elif mode == "mean":
                media = sum(neighbors) // len(neighbors)
                new_pixels[x, y] = media

    return new_img


def median_filter(image: Image.Image, kernel_size: int) -> Image.Image:
    image = image.convert("L")
    largura, altura = image.size
    pad = kernel_size // 2

    original_pixels = image.load()

    new_img = Image.new("L", (largura, altura))
    new_pixels = new_img.load()

    for y in range(pad, altura - pad):
        for x in range(pad, largura - pad):
            neighbors = []
            for dy in range(-pad, pad + 1):
                for dx in range(-pad, pad + 1):
                    px = x + dx
                    py = y + dy
                    neighbors.append(original_pixels[px, py])

            neighbors.sort()
            median = neighbors[len(neighbors) // 2]
            new_pixels[x, y] = median

    return new_img

def order_filter(image: Image.Image, kernel_size: int, order: int) -> Image.Image:
    image = image.convert("L")
    largura, altura = image.size
    pad = kernel_size // 2

    original_pixels = image.load()
    new_img = Image.new("L", (largura, altura))
    new_pixels = new_img.load()

    for y in range(pad, altura - pad):
        for x in range(pad, largura - pad):
            neighbors = []
            for dy in range(-pad, pad + 1):
                for dx in range(-pad, pad + 1):
                    px = x + dx
                    py = y + dy
                    neighbors.append(original_pixels[px, py])

            neighbors.sort()
            index = min(order, len(neighbors) - 1)
            new_pixels[x, y] = neighbors[index]

    return new_img

def conservative_smoothing(image: Image.Image, kernel_size: int) -> Image.Image:
    image = image.convert("L")
    largura, altura = image.size
    pad = kernel_size // 2

    original_pixels = image.load()
    new_img = Image.new("L", (largura, altura))
    new_pixels = new_img.load()

    for y in range(altura):
        for x in range(largura):

            if x < pad or x >= largura - pad or y < pad or y >= altura - pad:
                new_pixels[x, y] = original_pixels[x, y]
                continue

            neighbors = []
            for dy in range(-pad, pad + 1):
                for dx in range(-pad, pad + 1):
                    px = x + dx
                    py = y + dy
                    if (dx, dy) != (0, 0):
                        neighbors.append(original_pixels[px, py])

            min_val = min(neighbors)
            max_val = max(neighbors)
            central_value = original_pixels[x, y]

            if central_value < min_val:
                new_pixels[x, y] = min_val
            elif central_value > max_val:
                new_pixels[x, y] = max_val
            else:
                new_pixels[x, y] = central_value

    return new_img

def generate_gaussian_kernel(kernel_size: int, sigma: float):
    pad = kernel_size // 2
    kernel = []
    total = 0.0

    for y in range(-pad, pad + 1):
        line = []
        for x in range(-pad, pad + 1):
            value = (1 / (2 * math.pi * sigma ** 2)) * math.exp(-(x ** 2 + y ** 2) / (2 * sigma ** 2))
            line.append(value)
            total += value
        kernel.append(line)

    for y in range(kernel_size):
        for x in range(kernel_size):
            kernel[y][x] /= total

    return kernel

def apply_kernel(image: Image.Image, kernel: list[list[float]]) -> Image.Image:
    image = image.convert("L")
    width, height = image.size
    pad = len(kernel) // 2
    original = image.load()
    new_img = Image.new("L", (width, height))
    new_pixels = new_img.load()

    for y in range(pad, height - pad):
        for x in range(pad, width - pad):
            total = 0.0
            for ky in range(len(kernel)):
                for kx in range(len(kernel[0])):
                    px = x + kx - pad
                    py = y + ky - pad
                    total += original[px, py] * kernel[ky][kx]
            new_pixels[x, y] = int(min(max(round(total), 0), 255))

    return new_img

def gaussian_filter(image: Image.Image, sigma: float) -> Image.Image:
    kernel_size = max(3, int(2 * round(3 * sigma) + 1))
    kernel = generate_gaussian_kernel(kernel_size, sigma)
    return apply_kernel(image, kernel)

