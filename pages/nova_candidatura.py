import streamlit as st

from constantes import STATUS_VALIDOS

def formulario_nova_candidatura():
    # Formulário para adicionar uma nova candidatura
    with st.form("nova_candidatura", clear_on_submit=True):
        st.subheader("Adicionar nova candidatura")
        st.write("Preencha os campos abaixo (campos com * são obrigatórios):")

        # Campo: Empresa *
        empresa_form = st.text_input(
            "Empresa *",
            type="default",
            placeholder="Digite o nome da empresa",
            required=True,
        )

        # Campo: Cargo *
        cargo_form = st.text_input(
            "Cargo *",
            type="default",
            placeholder="Digite o cargo ao qual você está se candidatando",
            required=True,
        )

        # Campo: Link da vaga
        link_vaga_form = st.text_input(
            "Link da vaga", type="url", placeholder="Digite o link da vaga"
        )

        # Campo: Data da candidatura *
        data_candidatura_form = st.date_input(
            "Data da candidatura *", value=None, max_value="today", format="DD/MM/YYYY"
        )

        # Campo: Status
        status_form = st.selectbox(
            "Status",
            options=STATUS_VALIDOS,
        )

        # Campo: prazo para acompanhamento
        prazo_acompanhamento_form = st.date_input(
            "Prazo para acompanhamento", value=None, format="DD/MM/YYYY"
        )

        # Campo: Observações
        observacoes_form = st.text_area(
            "Observações",
            max_chars=500,
            placeholder="Digite observações adicionais sobre a candidatura",
        )

        # Botão de envio do formulário
        enviar = st.form_submit_button("Adicionar candidatura")

    if enviar:
        if not empresa_form.strip() or not cargo_form.strip() or not data_candidatura_form:
            st.error("Por favor, preencha todos os campos obrigatórios.")
        else:
            from database import adicionar_candidatura

            # Adiciona a candidatura ao banco de dados
            adicionar_candidatura(
                empresa=empresa_form.strip(),
                cargo=cargo_form.strip(),
                link_vaga=(link_vaga_form or "").strip() or None,
                data_candidatura=data_candidatura_form.isoformat(),
                status=status_form,
                prazo_acompanhamento=prazo_acompanhamento_form.isoformat() if prazo_acompanhamento_form else None,
                observacoes=(observacoes_form or "").strip() or None,
                )

            st.success(
                f"Candidatura para **{empresa_form}** no cargo de **{cargo_form}** adicionada com sucesso!"
            )

def main():
    st.title("VagasDash - Nova Candidatura")
    st.write(
        "Preencha o formulário abaixo para adicionar uma nova candidatura a uma vaga de emprego."
    )

    formulario_nova_candidatura()

if __name__ == "__main__":
    main()