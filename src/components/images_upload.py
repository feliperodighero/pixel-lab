import streamlit as st


def upload_images():
    upload_col1, upload_col2 = st.columns(2)
    with upload_col1:
        first_uploaded_image = st.file_uploader(
            "Escolha uma imagem", type=["jpg", "png", "jpeg", "bmp", "tiff", "tif"]
        )
    with upload_col2:
        second_uploaded_image = st.file_uploader(
            "Escolha outra imagem", type=["jpg", "png", "jpeg", "bmp", "tiff", "tif"]
        )

    return first_uploaded_image, second_uploaded_image
