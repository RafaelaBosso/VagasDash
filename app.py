import streamlit as st

from database import init_db

st.set_page_config(
    page_title="VagasDash",
    layout="wide",
)


def navegacao():
    pg = st.navigation(
        [
            st.Page(pagina_inicial, title="Início", icon="🏠"),
            st.Page("pages/nova_candidatura.py", title="Nova Candidatura", icon="👤"),
            st.Page("pages/candidaturas.py", title="Candidaturas", icon="👥"),
        ],
        position="top",
    )

    pg.run()


def pagina_inicial():
    st.title("VagasDash")
    st.write("Seu espaço para organizar candidaturas a vagas de emprego.")


def main():

    init_db()

    navegacao()


if __name__ == "__main__":
    main()
