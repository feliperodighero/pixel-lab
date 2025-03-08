import io

import streamlit as st
from PIL import Image

from operations.brightness import adjust_brightness

st.title("PixelLab - Manipulando Imagens")

uploaded_image = st.file_uploader("Escolha uma imagem", type=["jpg", "png", "jpeg"])

st.divider()

imges_col1, images_col2 = st.columns(2)

if uploaded_image is not None:
    image = Image.open(uploaded_image)

    with imges_col1:
        st.image(image, caption="Imagem Original", use_container_width=True)

    st.divider()

    brightness_value = st.slider("Ajuste o brilho", min_value=-255, max_value=255, value=0)

    if brightness_value != 0:
        new_image_result = adjust_brightness(image, brightness_value)

        with images_col2:
            st.image(new_image_result, caption="Imagem Processada", use_container_width=True)

        img_bytes = io.BytesIO()
        new_image_result = new_image_result.convert("RGB")
        new_image_result.save(img_bytes, format="JPEG")

        with images_col2:
            st.download_button(
                label="Baixar Imagem Processada",
                data=img_bytes.getvalue(),
                file_name="image_result.jpg",
                mime="image/jpeg",
                use_container_width=True,
            )
