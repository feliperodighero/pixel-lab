import io

import streamlit as st
from PIL import Image

from operations.brightness import decrease_brightness, increase_brightness

st.title("PixelLab - Manipulando Imagens")

uploaded_image = st.file_uploader("Escolha uma imagem", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)

    st.image(image, caption="Imagem Original", use_container_width=True)

    increase_brightness_value = st.slider("Ajuste o brilho", min_value=0, max_value=255, value=0)
    decrease_brightness_value = st.slider("Ajuste o contraste", min_value=0, max_value=255, value=0)

    if increase_brightness_value != 0 or decrease_brightness_value != 0:
        if increase_brightness_value != 0:
            new_image_result = increase_brightness(image, increase_brightness_value)
        else:
            new_image_result = decrease_brightness(image, decrease_brightness_value)

        st.image(new_image_result, caption="Imagem Processada", use_container_width=True)

        img_bytes = io.BytesIO()
        new_image_result.save(img_bytes, format="JPEG")

        st.download_button(
            label="Baixar Imagem Processada",
            data=img_bytes.getvalue(),
            file_name="image_result.jpg",
            mime="image/jpeg"
        )
