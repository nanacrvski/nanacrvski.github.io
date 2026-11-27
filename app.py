import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Calculadora de Regra de Três",
    page_icon="🌸",
    layout="centered"
)

# Cores e aparência do site
st.markdown("""
<style>
.stApp {
    background-color: #fff0f6;
}

h1, h2, h3 {
    color: #d63384;
}

.stButton > button {
    background-color: #e7549b;
    color: white;
    border-radius: 10px;
    border: none;
}

.stButton > button:hover {
    background-color: #c9367d;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# Título do site
st.title("🌸 Calculadora de Regra de Três")
st.write("Bem-vindo(a)! Escolha o tipo de cálculo que deseja realizar.")

# Escolha do tipo de regra de três
tipo = st.selectbox(
    "Qual cálculo deseja fazer?",
    ["Regra de Três Simples", "Regra de Três Composta"]
)

# REGRA DE TRÊS SIMPLES
if tipo == "Regra de Três Simples":

    st.subheader("💗 Regra de Três Simples")
    st.write("Preencha os três valores conhecidos.")

    a = st.number_input("Valor A", min_value=0.000001, value=2.0)
    b = st.number_input("Valor B", min_value=0.000001, value=4.0)
    c = st.number_input("Valor C", min_value=0.000001, value=5.0)

    st.write("Montando a proporção:")
    st.latex(r"\frac{A}{B} = \frac{C}{X}")

    if st.button("Calcular resultado"):

        x = (b * c) / a

        st.success(f"O resultado é: {x:.2f}")

        st.write("### Resolução passo a passo:")
        st.write(f"1. Multiplicamos B por C: {b} × {c} = {b*c}")
        st.write(f"2. Dividimos o resultado por A: {b*c} ÷ {a}")
        st.write(f"3. Resultado final: X = {x:.2f}")


# REGRA DE TRÊS COMPOSTA
else:

    st.subheader("🌷 Regra de Três Composta")
    st.write("Use uma grandeza principal e duas outras grandezas.")

    a = st.number_input(
        "Valor inicial da grandeza principal",
        min_value=0.000001,
        value=2.0
    )

    b = st.number_input(
        "Primeira grandeza - valor inicial",
        min_value=0.000001,
        value=4.0
    )

    c = st.number_input(
        "Primeira grandeza - valor final",
        min_value=0.000001,
        value=8.0
    )

    d = st.number_input(
        "Segunda grandeza - valor inicial",
        min_value=0.000001,
        value=3.0
    )

    e = st.number_input(
        "Segunda grandeza - valor final",
        min_value=0.000001,
        value=6.0
    )

    relacao1 = st.selectbox(
        "A primeira grandeza é:",
        ["Diretamente proporcional", "Inversamente proporcional"]
    )

    relacao2 = st.selectbox(
        "A segunda grandeza é:",
        ["Diretamente proporcional", "Inversamente proporcional"]
    )

    if st.button("Calcular resultado"):

        fator1 = c / b

        if relacao1 == "Inversamente proporcional":
            fator1 = b / c

        fator2 = e / d

        if relacao2 == "Inversamente proporcional":
            fator2 = d / e

        x = a * fator1 * fator2

        st.success(f"O resultado é: {x:.2f}")

        st.write("### Resolução passo a passo:")

        st.write(f"1. Valor inicial: {a}")

        st.write(f"2. Primeiro fator: {fator1:.2f}")

        st.write(f"3. Segundo fator: {fator2:.2f}")

        st.write(
            f"4. Multiplicamos: {a} × {fator1:.2f} × {fator2:.2f}"
        )

        st.write(f"5. Resultado final: X = {x:.2f}")

# Rodapé
st.markdown("---")
st.markdown(
    "<center>Feito com 💗 usando Python</center>",
    unsafe_allow_html=True
)

