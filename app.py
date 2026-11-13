
import streamlit as st

st.set_page_config(
    page_title="Estoque Fácil",
    page_icon="📦",
    layout="wide"
)

if "produtos" not in st.session_state:
    st.session_state.produtos = []

st.title("📦 Estoque Fácil")
st.subheader("Controle simples e inteligente de estoque")

st.sidebar.title("Menu")
opcao = st.sidebar.radio(
    "Selecione uma opção:",
    ["Dashboard", "Cadastrar produto", "Controle de produtos", "Alertas de estoque"]
)

produtos = st.session_state.produtos

if opcao == "Dashboard":
    st.header("Dashboard")

    total = len(produtos)
    quantidade = sum(p["quantidade"] for p in produtos)
    alertas = sum(
        1 for p in produtos
        if p["quantidade"] <= p["minimo"]
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Produtos cadastrados", total)
    col2.metric("Unidades em estoque", quantidade)
    col3.metric("Alertas de estoque", alertas)

    st.info("Bem-vindo ao Estoque Fácil! Utilize o menu lateral para controlar seus produtos.")

elif opcao == "Cadastrar produto":
    st.header("Cadastrar novo produto")

    with st.form("cadastro"):
        nome = st.text_input("Nome do produto")
        qtd = st.number_input("Quantidade inicial", min_value=0, step=1)
        minimo = st.number_input("Estoque mínimo", min_value=0, step=1)

        enviar = st.form_submit_button("Cadastrar produto")

        if enviar:
            if nome.strip():
                produtos.append({
                    "nome": nome.strip(),
                    "quantidade": int(qtd),
                    "minimo": int(minimo)
                })
                st.success("Produto cadastrado com sucesso!")
            else:
                st.error("Informe o nome do produto.")

elif opcao == "Controle de produtos":
    st.header("Controle de produtos")

    if produtos:
        for i, p in enumerate(produtos):
            st.write(f"**{p['nome']}**")
            st.write(f"Quantidade: {p['quantidade']} | Mínimo: {p['minimo']}")

            saida = st.number_input(
                f"Quantidade de saída - {p['nome']}",
                min_value=0,
                max_value=p["quantidade"],
                step=1,
                key=f"saida_{i}"
            )

            if st.button("Registrar saída", key=f"botao_{i}"):
                p["quantidade"] -= int(saida)
                st.success("Saída registrada!")
                st.rerun()

            st.divider()
    else:
        st.info("Nenhum produto cadastrado.")

elif opcao == "Alertas de estoque":
    st.header("Alertas de estoque")

    baixos = [
        p for p in produtos
        if p["quantidade"] <= p["minimo"]
    ]

    if baixos:
        for p in baixos:
            st.warning(
                f"Estoque baixo: {p['nome']} - "
                f"Quantidade disponível: {p['quantidade']}"
            )
    else:
        st.success("Nenhum produto com estoque baixo!")
