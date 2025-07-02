import streamlit as st
from PIL import Image

from components import (
    apply_operations,
    display_images,
    download_image,
    select_operations,
    upload_images,
)
from operations.arithmetic import adjust_brightness


st.set_page_config(page_title="PixelLab", layout="wide")
st.title("PixelLab - Manipulando Imagens")

first_uploaded_image, second_uploaded_image = upload_images()
st.divider()

if first_uploaded_image is not None:
    first_image = Image.open(first_uploaded_image).convert("RGB")
    second_image = None

    if second_uploaded_image is not None:
        second_image = Image.open(second_uploaded_image).convert("RGB")

    if second_image is not None and first_image.size != second_image.size:
        second_image = second_image.resize(first_image.size)

    images_col3 = display_images(first_image, second_image)

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Aritmética", "Inverter", "Lógica", "Realce", "Domínio Espacial", "Morfologia"])

    with tab1:
        operation_arithmetic = st.radio(
            "Aritmética:",
            (
                "Nenhuma",
                "Somar",
                "Subtrair",
                "Multiplicar",
                "Dividir",
                "Blending",
                "Média",
            ),
        )
    with tab2:
        operation_invert = st.radio(
            "Inverter:", ("Nenhuma", "Esquerda para Direita", "Cima para Baixo")
        )
    with tab3:
        operation_logic = st.radio(
            "Operações Lógicas:", ("Nenhuma", "AND", "OR", "XOR", "NOT")
        )
        threshold = st.slider("Defina o Threshold para binarização", 0, 255, 128)

    with tab4:
        operation_enhance = st.radio(
            "Realce:", ("Nenhuma", "Equalização de Histograma", "Limiarização")
        )
        threshold = st.slider("Defina o Threshold para binarização ", 0, 255, 128)

    with tab5:
        operation_spacial_domain = st.radio(
            "Passa Baixa:", ("Nenhuma", "Filtros Passa-Baixa", "Filtros Passa-Alta")
        )

        if operation_spacial_domain == "Filtros Passa-Baixa":
            filter_option_low_pass = st.radio("Escolha um filtro:", ["MAX", "MIN", "MEAN", "MEDIANA", "ORDEM", "SUAVIZAÇÃO CONSERVATIVA", "GAUSSIANO"])
            kernel_size = st.slider("Escolha o tamanho do kernel:", min_value=3, max_value=7, step=2, value=3)

            if filter_option_low_pass == "ORDEM":
                order = st.slider("Escolha o valor de ordem (0 = Mínimo, Meio = Mediana, Último = Máximo):",
                              min_value=0, max_value=kernel_size**2 - 1, value=(kernel_size**2) // 2)

            if filter_option_low_pass == "GAUSSIANO":
                sigma = st.slider("Defina o Sigma:", min_value=0.1, max_value=5.0, value=1.0, step=0.1)

        if operation_spacial_domain == "Filtros Passa-Alta":
            filter_option_high_pass = st.radio("Escolha um filtro:", ["Prewitt", "Sobel", "Laplaciano"])

            if filter_option_high_pass == "Laplaciano":
                kernel_type = st.radio("Escolha o Kernel:", ["4-neighbors", "8-neighbors"], index=0)

    with tab6:
        operation_morphology = st.radio(
            "Operações Morfológicas:", ("Nenhuma", "Dilatação", "Erosão", "Abertura", "Fechamento", "Contorno")
        )

        if operation_morphology != "Nenhuma":
            structure_size = st.slider("Tamanho do Elemento Estruturante", min_value=3, max_value=9, step=2, value=3)

    new_image_result = apply_operations(
        first_image,
        second_image,
        operation_arithmetic,
        operation_invert,
        operation_logic,
        operation_enhance,
        threshold,
        filter_option_low_pass if operation_spacial_domain == "Filtros Passa-Baixa" else "Nenhuma",
        kernel_size if operation_spacial_domain == "Filtros Passa-Baixa" else "Nenhuma",
        order if operation_spacial_domain == "Filtros Passa-Baixa" and filter_option_low_pass == "ORDEM"  else 0,
        sigma if operation_spacial_domain == "Filtros Passa-Baixa" and filter_option_low_pass == "GAUSSIANO" else 0.0,
        filter_option_high_pass if operation_spacial_domain == "Filtros Passa-Alta" else "Nenhuma",
        kernel_type if operation_spacial_domain == "Filtros Passa-Alta" and filter_option_high_pass == "Laplaciano" else "4-neighbors",
        operation_morphology,
        structure_size if operation_morphology != "Nenhuma" else 0,
    )

    st.divider()
    brightness_value = st.slider("Ajuste o brilho", min_value=-255, max_value=255, value=0)
    if brightness_value != 0:
        new_image_result = adjust_brightness(new_image_result, brightness_value)

    with images_col3:
        st.image(new_image_result, caption="Imagem Final", use_container_width=True)
        download_image(new_image_result)
