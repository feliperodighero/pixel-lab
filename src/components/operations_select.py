import streamlit as st


def select_operations():
    tab1, tab2, tab3, tab4 = st.tabs(["Aritmética", "Inverter", "Lógica", "Realce"])

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

    return operation_arithmetic, operation_invert, operation_logic, operation_enhance
