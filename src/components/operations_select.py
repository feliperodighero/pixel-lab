import streamlit as st


def select_operations():
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Aritmética", "Inverter", "Lógica", "Realce", "Domínio Espacial"])

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
    with tab4:
        operation_enhance = st.radio(
            "Realce:", ("Nenhuma", "Equalização de Histograma", "Limiarização")
        )

    with tab5:
        operation_spacial_domain = st.radio(
            "Passa Baixa:", ("Nenhuma", "Filtros Passa-Baixa")
        )

        if operation_spacial_domain == "Filtros Passa-Baixa":
            filter_option = st.radio("Escolha um filtro:", ["MAX", "MIN", "MEAN"])
            kernel_size = st.slider("Escolha o tamanho do kernel:", min_value=3, max_value=7, step=2, value=3)

    return operation_arithmetic, operation_invert, operation_logic, operation_enhance
