import io

import matplotlib.pyplot as plt
from PIL import Image


def calculate_histogram(image: Image.Image) -> list[int]:
    image = image.convert("L")
    pixels = image.load()
    width, height = image.size
    hist = [0] * 256

    for y in range(height):
        for x in range(width):
            hist[pixels[x, y]] += 1

    return hist


def plot_histogram(hist: list[int], title: str = "Histograma") -> Image.Image:
    fig, ax = plt.subplots()
    ax.bar(range(256), hist, color="black")
    ax.set_title(title)
    ax.set_xlim(0, 255)
    ax.set_xlabel("Intensidade")
    ax.set_ylabel("Frequência")

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close(fig)

    return Image.open(buf)
