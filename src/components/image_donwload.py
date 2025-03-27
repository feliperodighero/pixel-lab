import io

import streamlit as st


def download_image(image):
    img_bytes = io.BytesIO()
    image.save(img_bytes, format="JPEG")

    st.download_button(
        label="Baixar Imagem Final",
        data=img_bytes.getvalue(),
        file_name="image_result.jpg",
        mime="image/jpeg",
        use_container_width=True,
    )
