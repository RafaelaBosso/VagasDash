import sqlite3
from pathlib import Path
from contextlib import closing

def init_db():
    diretorio_projeto = Path(__file__).resolve().parent
    caminho_banco = diretorio_projeto / "vagasdash.db"

    # fecha a conexão
    with closing(sqlite3.connect(caminho_banco, autocommit=False)) as conexao:
        # fecha a transação
        with conexao:
            conexao.execute('''
            CREATE TABLE IF NOT EXISTS candidaturas (
                id INTEGER PRIMARY KEY,
                empresa TEXT NOT NULL,
                cargo TEXT NOT NULL,
                link_vaga TEXT,
                data_candidatura TEXT NOT NULL,
                status TEXT NOT NULL CHECK (status IN (
                    'Para analisar',
                    'Candidatura enviada',
                    'Teste técnico agendado',
                    'Teste técnico realizado',
                    'Entrevista agendada',
                    'Entrevista realizada',
                    'Oferta recebida',
                    'Encerrado/Não selecionado',
                    'Encerrado/Oferta recusada',
                    'Encerrado/Oferta aceita'
                )),
                prazo_acompanhamento TEXT,
                observacoes TEXT,
                criada_em TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        ''')