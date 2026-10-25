
import streamlit as st

st.set_page_config(
    page_title="VagasDash",
    page_icon="📋",
    layout="wide",
)

st.title("VagasDash")
st.write("Seu espaço para organizar candidaturas a vagas de emprego.")

if __name__ == "__main__":
    from database import init_db
    init_db()