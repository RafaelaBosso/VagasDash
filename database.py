import sqlite3
from pathlib import Path
from contextlib import closing

diretorio_projeto = Path(__file__).resolve().parent
caminho_banco = diretorio_projeto / "vagasdash.db"

def init_db():
    # fecha a conexão
    with closing(sqlite3.connect(caminho_banco)) as conexao:
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

def adicionar_candidatura(empresa, cargo, link_vaga, data_candidatura, status, prazo_acompanhamento, observacoes):
    with closing(sqlite3.connect(caminho_banco)) as conexao:
        with conexao:
            conexao.execute('''
                INSERT INTO candidaturas (empresa, cargo, link_vaga, data_candidatura, status, prazo_acompanhamento, observacoes)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (empresa, cargo, link_vaga, data_candidatura, status, prazo_acompanhamento, observacoes))


def listar_candidaturas():
    with closing(sqlite3.connect(caminho_banco)) as conexao:

        conexao.row_factory = sqlite3.Row
        
        lista_candidaturas = conexao.execute('''
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
        ''').fetchall()
        visualizar_candidaturas = []

    
        for candidatura in lista_candidaturas:
            uma_candidatura = {
                "ID": candidatura["id"],
                "Empresa": candidatura["empresa"],
                "Cargo": candidatura["cargo"],
                "Link da Vaga": candidatura["link_vaga"],
                "Data da Candidatura": candidatura["data_candidatura"],
                "Status": candidatura["status"],
                "Prazo de Acompanhamento": candidatura["prazo_acompanhamento"],
                "Observações": candidatura["observacoes"],
                "Criada em": candidatura["criada_em"],
            }
            visualizar_candidaturas.append(uma_candidatura)

    return visualizar_candidaturas