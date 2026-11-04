import streamlit as st

from constantes import STATUS_VALIDOS

st.set_page_config(
    page_title="VagasDash - Nova Candidatura",
    page_icon="👤",
    layout="wide",
)

st.title("VagasDash - Nova Candidatura")
st.write(
    "Preencha o formulário abaixo para adicionar uma nova candidatura a uma vaga de emprego."
)

# Formulário para adicionar uma nova candidatura
with st.form("nova_candidatura", clear_on_submit=True):
    st.subheader("Adicionar nova candidatura")
    st.write("Preencha os campos abaixo (campos com * são obrigatórios):")

    # Campo: Empresa *
    empresa = st.text_input(
        "Empresa *",
        type="default",
        placeholder="Digite o nome da empresa",
        required=True,
    )

    # Campo: Cargo *
    cargo = st.text_input(
        "Cargo *",
        type="default",
        placeholder="Digite o cargo ao qual você está se candidatando",
        required=True,
    )

    # Campo: Link da vaga
    link_vaga = st.text_input(
        "Link da vaga", type="url", placeholder="Digite o link da vaga"
    )

    # Campo: Data da candidatura *
    data_candidatura = st.date_input(
        "Data da candidatura *", value=None, max_value="today", format="DD/MM/YYYY"
    )

    # Campo: Status
    status = st.selectbox(
        "Status",
        options=STATUS_VALIDOS,
    )

    # Campo: prazo para acompanhamento
    prazo_acompanhamento = st.date_input(
        "Prazo para acompanhamento", value=None, format="DD/MM/YYYY"
    )

    # Campo: Observações
    observacoes = st.text_area(
        "Observações",
        max_chars=500,
        placeholder="Digite observações adicionais sobre a candidatura",
    )

    # Botão de envio do formulário
    enviar = st.form_submit_button("Adicionar candidatura")

    if enviar:
        if not empresa.strip() or not cargo.strip() or not data_candidatura:
            st.error("Por favor, preencha todos os campos obrigatórios.")
        else:
            from database import adicionar_candidatura

            # Adiciona a candidatura ao banco de dados
            adicionar_candidatura(
                empresa.strip(),
                cargo.strip(),
                (link_vaga or "").strip() or None,
                data_candidatura.isoformat(),
                status,
                prazo_acompanhamento.isoformat() if prazo_acompanhamento else None,
                (observacoes or "").strip() or None,
            )

            st.success(
                f"Candidatura para **{empresa}** no cargo de **{cargo}** adicionada com sucesso!"
            )
