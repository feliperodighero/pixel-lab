import streamlit as st


def display_images(first_image, second_image=None):
    imges_col1, images_col2, images_col3 = st.columns(3)

    with imges_col1:
        st.image(first_image, caption="Primeira Imagem", use_container_width=True)

    if second_image:
        second_image = second_image.resize(first_image.size)
        with images_col2:
            st.image(second_image, caption="Segunda Imagem", use_container_width=True)

    return images_col3
