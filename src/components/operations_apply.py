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
from operations.morphological import (
    border_extraction_filter,
    closing_filter,
    dilation_filter,
    erosion_filter,
    opening_filter,
)
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
from utils.histogram import calculate_histogram, plot_histogram


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

    ops_need_second_image = (
        operation_arithmetic in ["Somar", "Subtrair", "Blending", "Média"]
        or operation_logic in ["AND", "OR", "XOR"]
    )

    if ops_need_second_image and second_image is None:
        st.error("⚠️ Esta operação requer uma segunda imagem. Por favor, envie outra imagem para continuar.")
        return first_image

    # Arithmetic Operations
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

    # Invert Operations
    if operation_invert == "Esquerda para Direita":
        new_image = flip_horizontal(new_image)
    elif operation_invert == "Cima para Baixo":
        new_image = flip_vertical(new_image)

    # Logical Operations
    if operation_logic != "Nenhuma":
        binary_image1 = convert_to_binary(first_image, threshold)
        if operation_logic == "NOT":
            new_image = logical_not(binary_image1)
        else:
            binary_image2 = convert_to_binary(second_image, threshold)
            new_image = logical_operation(binary_image1, binary_image2, operation_logic)

    # Enhancement Operations
    if operation_enhance == "Equalização de Histograma":
        new_image = histogram_equalization(first_image.convert("L"))

        original_image = first_image.convert("L")
        equalized_gray = new_image

        original_hist = calculate_histogram(original_image)
        equalized_hist = calculate_histogram(equalized_gray)

        original_hist_image = plot_histogram(original_hist, title="Histograma Original")
        equalized_hist_image = plot_histogram(equalized_hist, title="Histograma Equalizado")

        st.subheader("Comparação de Histogramas")
        col1, col2 = st.columns(2)
        with col1:
            st.image(original_hist_image, caption="Histograma Original", use_container_width=True)
        with col2:
            st.image(equalized_hist_image, caption="Histograma Equalizado", use_container_width=True)

    elif operation_enhance == "Limiarização":
        new_image = threshold_image(first_image.convert("L"), threshold)

    # Low Pass Filters
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

    # High Pass Filters
    if filter_option_high_pass != "Nenhuma":
        if filter_option_high_pass == "Prewitt":
            new_image = prewitt_filter(first_image)
        elif filter_option_high_pass == "Sobel":
            new_image = sobel_filter(first_image)
        elif filter_option_high_pass == "Laplaciano":
            new_image = laplacian_filter(first_image, kernel_type)

    # Morphological Operations
    if operation_morphology != "Nenhuma":
        if operation_morphology == "Dilatação":
            new_image = dilation_filter(first_image, structure_size)
        elif operation_morphology == "Erosão":
            new_image = erosion_filter(first_image, structure_size)
        elif operation_morphology == "Abertura":
            new_image = opening_filter(first_image, structure_size)
        elif operation_morphology == "Fechamento":
            new_image = closing_filter(first_image, structure_size)
        elif operation_morphology == "Contorno":
            new_image = border_extraction_filter(first_image, structure_size)

    return new_image
