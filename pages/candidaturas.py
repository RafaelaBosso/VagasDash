import pandas as pd
import streamlit as st

from constantes import STATUS_VALIDOS
from database import listar_candidaturas

def pagina_candidaturas():
    todas_candidaturas = listar_candidaturas()

    if todas_candidaturas:
        df_candidaturas = pd.DataFrame(todas_candidaturas)

        # Converter as colunas que armazenam datas
        df_candidaturas["data_candidatura"] = pd.to_datetime(
            df_candidaturas["data_candidatura"]
        ).dt.date
        df_candidaturas["prazo_acompanhamento"] = pd.to_datetime(
            df_candidaturas["prazo_acompanhamento"]
        ).dt.date
        df_candidaturas["criada_em"] = pd.to_datetime(df_candidaturas["criada_em"])

        st.dataframe(
            df_candidaturas,
            hide_index=True,
            column_config={
                "id": st.column_config.NumberColumn(label="ID"),
                "empresa": st.column_config.TextColumn(label="Empresa"),
                "cargo": st.column_config.TextColumn(label="Cargo"),
                "link_vaga": st.column_config.LinkColumn(label="Link da Vaga"),
                "data_candidatura": st.column_config.DateColumn(label="Data da Candidatura", format="localized"),
                "status": st.column_config.SelectboxColumn(label="Status", options=STATUS_VALIDOS),
                "prazo_acompanhamento": st.column_config.DateColumn(
                    label="Prazo de Acompanhamento",
                    format="localized"
                ),
                "criada_em": st.column_config.DatetimeColumn(label="Criada em", format="localized"),
                "observacoes": st.column_config.TextColumn(label="Observações"),
            },
            alt="Tabela de Candidaturas",
        )

    else:
        st.write("Nenhuma candidatura registrada ainda.")


def main():
    st.title("Candidaturas")
    st.write("Aqui você pode visualizar todas as candidaturas registradas.")

    pagina_candidaturas()


if __name__ == "__main__":
    main()
