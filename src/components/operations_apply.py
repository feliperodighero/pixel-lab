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
from operations.morphological import dilation_filter, erosion_filter
from operations.spacial_domain import (
    conservative_smoothing,
    gaussian_filter,
    laplacian_filter,
    max_min_mean_filters,
    median_filter,
    order_filter,
    prewitt_filter,
    sobel_filter,
)


def apply_operations(
        first_image,
        second_image,
        operation_arithmetic,
        operation_invert,
        operation_logic,
        operation_enhance,
        threshold,
        filter_option_low_pass,
        kernel_size,
        order,
        sigma,
        filter_option_high_pass,
        kernel_type,
        operation_morphology,
        structure_size,
    ):
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

    if filter_option_low_pass != "Nenhuma":
        if filter_option_low_pass == "MAX":
            new_image = max_min_mean_filters(first_image, kernel_size, filter_option_low_pass.lower())
        elif filter_option_low_pass == "MIN":
            new_image = max_min_mean_filters(first_image, kernel_size, filter_option_low_pass.lower())
        elif filter_option_low_pass == "MEAN":
            new_image = max_min_mean_filters(first_image, kernel_size, filter_option_low_pass.lower())
        elif filter_option_low_pass == "MEDIANA":
            new_image = median_filter(first_image, kernel_size)
        elif filter_option_low_pass == "ORDEM":
            new_image = order_filter(first_image, kernel_size, order)
        elif filter_option_low_pass == "SUAVIZAÇÃO CONSERVATIVA":
            new_image = conservative_smoothing(first_image, kernel_size)
        elif filter_option_low_pass == "GAUSSIANO":
            new_image = gaussian_filter(first_image, sigma)

    if filter_option_high_pass != "Nenhuma":
        if filter_option_high_pass == "Prewitt":
            new_image = prewitt_filter(first_image)
        elif filter_option_high_pass == "Sobel":
            new_image = sobel_filter(first_image)
        elif filter_option_high_pass == "Laplaciano":
            new_image = laplacian_filter(first_image, kernel_type)

    if operation_morphology != "Nenhuma":
        if operation_morphology == "Dilatação":
            new_image = dilation_filter(first_image, structure_size)
        elif operation_morphology == "Erosão":
            new_image = erosion_filter(first_image, structure_size)

    return new_image