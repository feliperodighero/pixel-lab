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

    images_col3 = display_images(first_image, second_image)

    operation_arithmetic, operation_invert, operation_logic, operation_enhance = select_operations()

    new_image_result = apply_operations(first_image, second_image, operation_arithmetic, operation_invert, operation_logic, operation_enhance)

    st.divider()
    brightness_value = st.slider("Ajuste o brilho", min_value=-255, max_value=255, value=0)
    if brightness_value != 0:
        new_image_result = adjust_brightness(new_image_result, brightness_value)

    with images_col3:
        st.image(new_image_result, caption="Imagem Final", use_container_width=True)
        download_image(new_image_result)
