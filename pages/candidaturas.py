from constantes import STATUS_VALIDOS
from database import listar_candidaturas
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="VagasDash - Candidaturas",
    page_icon="👥",
    layout="wide",
)

def pagina_candidaturas():
    todas_candidaturas = listar_candidaturas()

    if todas_candidaturas:
        df_candidaturas = pd.DataFrame(todas_candidaturas)

        # Converter as colunas que armazenam datas
        df_candidaturas["Data da Candidatura"] = pd.to_datetime(df_candidaturas["Data da Candidatura"]).dt.date
        df_candidaturas["Prazo de Acompanhamento"] = pd.to_datetime(df_candidaturas["Prazo de Acompanhamento"]).dt.date
        df_candidaturas["Criada em"] = pd.to_datetime(df_candidaturas["Criada em"])

        st.dataframe(
            df_candidaturas, 
            hide_index=True, 
            column_config={
                "ID": st.column_config.NumberColumn(),
                "Link da Vaga": st.column_config.LinkColumn(),
                "Data da Candidatura": st.column_config.DateColumn(format="localized"),
                "Status": st.column_config.SelectboxColumn(options=STATUS_VALIDOS),
                "Prazo de Acompanhamento": st.column_config.DateColumn(format="localized"),
                "Criada em": st.column_config.DatetimeColumn(format="localized"),
            }, 
            alt="Tabela de Candidaturas")

    else:
        st.write("Nenhuma candidatura registrada ainda.")


def main():
    st.title("Candidaturas")
    st.write("Aqui você pode visualizar todas as candidaturas registradas.")

    pagina_candidaturas()

if __name__ == "__main__":
    main()