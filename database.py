import sqlite3
from contextlib import closing
from pathlib import Path

from constantes import STATUS_VALIDOS

_STATUS_SQL = ", ".join(f'"{status}"' for status in STATUS_VALIDOS)

diretorio_projeto = Path(__file__).resolve().parent
caminho_banco = diretorio_projeto / "vagasdash.db"


def init_db():
    # fecha a conexão e transação automaticamente ao final do bloco
    with closing(sqlite3.connect(caminho_banco)) as conexao, conexao:
            conexao.execute(f"""
            CREATE TABLE IF NOT EXISTS candidaturas (
                id INTEGER PRIMARY KEY,
                empresa TEXT NOT NULL,
                cargo TEXT NOT NULL,
                link_vaga TEXT,
                data_candidatura TEXT NOT NULL
                    CHECK (date(data_candidatura) IS data_candidatura),
                status TEXT NOT NULL CHECK (status IN ({_STATUS_SQL})),
                prazo_acompanhamento TEXT
                    CHECK (prazo_acompanhamento IS NULL OR date(prazo_acompanhamento) IS prazo_acompanhamento),
                observacoes TEXT,
                criada_em TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """)


def adicionar_candidatura(
    *,
    empresa,
    cargo,
    link_vaga,
    data_candidatura,
    status,
    prazo_acompanhamento,
    observacoes,
):
    # fecha a conexão e transação automaticamente ao final do bloco
    with closing(sqlite3.connect(caminho_banco)) as conexao, conexao:
            conexao.execute(
                """
                INSERT INTO candidaturas (empresa, cargo, link_vaga, data_candidatura, status, prazo_acompanhamento, observacoes)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    empresa,
                    cargo,
                    link_vaga,
                    data_candidatura,
                    status,
                    prazo_acompanhamento,
                    observacoes,
                ),
            )


def listar_candidaturas():
    with closing(sqlite3.connect(caminho_banco)) as conexao:
        conexao.row_factory = sqlite3.Row

        lista_candidaturas = conexao.execute("""
            SELECT
            id,
            empresa,
            cargo,
            link_vaga, 
            data_candidatura, 
            status,
            prazo_acompanhamento, 
            observacoes,
            datetime(criada_em, 'localtime') AS criada_em 
            FROM candidaturas ORDER BY id DESC
        """).fetchall()
        
        candidaturas_salvas = []

        for candidatura in lista_candidaturas:
             dict_candidatura = dict(candidatura)
             candidaturas_salvas.append(dict_candidatura)

    return candidaturas_salvas
