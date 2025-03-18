import io

import streamlit as st
from PIL import Image

from operations import (
    adjust_brightness,
    divide_image,
    multiply_image,
    subtract_images,
    sum_images,
)

st.title("PixelLab - Manipulando Imagens")

upload_col1, upload_col2 = st.columns(2)

with upload_col1:
    first_uploaded_image = st.file_uploader("Escolha uma imagem", type=["jpg", "png", "jpeg"])
with upload_col2:
    second_uploaded_image = st.file_uploader("Escolha outra imagem", type=["jpg", "png", "jpeg"])

st.divider()

imges_col1, images_col2, images_col3 = st.columns(3)

new_image_result = None

if first_uploaded_image is not None:
    first_image = Image.open(first_uploaded_image).convert("RGB")

    with imges_col1:
        st.image(first_image, caption="Primeira Imagem", use_container_width=True)

    if second_uploaded_image is not None:
        second_image = Image.open(second_uploaded_image).convert("RGB")
        second_image = second_image.resize(first_image.size)

        with images_col2:
            st.image(second_image, caption="Segunda Imagem", use_container_width=True)

        st.divider()

        col1, col2 = st.columns(2)

        operation_image_final = st.radio("Escolha uma operação:", ("Nenhuma", "Somar", "Subtrair", "Multiplicar", "Dividir"))

        if operation_image_final == "Somar":
            new_image_result = sum_images(first_image, second_image)
        elif operation_image_final == "Subtrair":
            new_image_result = subtract_images(first_image, second_image)
        elif operation_image_final == "Multiplicar":
            factor = st.slider("Escolha o valor de multiplicação:", min_value=0.1, max_value=5.0, value=1.0)
            new_image_result = multiply_image(first_image, factor)
        elif operation_image_final == "Dividir":
            factor = st.slider("Escolha o valor de divisão:", min_value=0.1, max_value=5.0, value=1.0)
            new_image_result = divide_image(first_image, factor)
        else:
            new_image_result = first_image

    else:
        new_image_result = first_image

    st.divider()
    brightness_value = st.slider("Ajuste o brilho", min_value=-255, max_value=255, value=0)

    if brightness_value != 0:
        new_image_result = adjust_brightness(new_image_result, brightness_value)

    with images_col3:
        st.image(new_image_result, caption="Imagem Final", use_container_width=True)

        img_bytes = io.BytesIO()
        new_image_result.save(img_bytes, format="JPEG")

        st.download_button(
            label="Baixar Imagem Final",
            data=img_bytes.getvalue(),
            file_name="image_result.jpg",
            mime="image/jpeg",
            use_container_width=True,
        )
