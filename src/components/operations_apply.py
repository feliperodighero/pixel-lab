import streamlit as st

from operations.arithmetic import (
    average_images,
    blend_images,
    divide_image,
    multiply_image,
    subtract_images,
    sum_images,
)
from operations.enhance import histogram_equalization, threshold_image
from operations.invert import flip_horizontal, flip_vertical
from operations.logical import convert_to_binary, logical_not, logical_operation


def apply_operations(first_image, second_image, operation_arithmetic, operation_invert, operation_logic, operation_enhance):
    new_image = first_image

    if operation_arithmetic == "Somar":
        new_image = sum_images(first_image, second_image)
    elif operation_arithmetic == "Subtrair":
        new_image = subtract_images(first_image, second_image)
    elif operation_arithmetic == "Multiplicar":
        factor = st.slider("Escolha o valor de multiplicação:", min_value=0.1, max_value=5.0, value=1.0)
        new_image = multiply_image(first_image, factor)
    elif operation_arithmetic == "Dividir":
        factor = st.slider("Escolha o valor de divisão:", min_value=0.1, max_value=5.0, value=1.0)
        new_image = divide_image(first_image, factor)
    elif operation_arithmetic == "Blending":
        alpha = st.slider("Escolha o valor de alpha:", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        new_image = blend_images(first_image, second_image, alpha)
    elif operation_arithmetic == "Média":
        new_image = average_images(first_image, second_image)

    if operation_invert == "Esquerda para Direita":
        new_image = flip_horizontal(new_image)
    elif operation_invert == "Cima para Baixo":
        new_image = flip_vertical(new_image)

    threshold = st.slider("Defina o Threshold para binarização", 0, 255, 128)
    if operation_logic != "Nenhuma":
        binary_image1 = convert_to_binary(first_image, threshold)
        if operation_logic == "NOT":
            new_image = logical_not(binary_image1)
        else:
            binary_image2 = convert_to_binary(second_image, threshold)
            new_image = logical_operation(binary_image1, binary_image2, operation_logic)

    if operation_enhance == "Equalização de Histograma":
        new_image = histogram_equalization(first_image.convert("L"))
    elif operation_enhance == "Limiarização":
        new_image = threshold_image(first_image.convert("L"), threshold)

    return new_image