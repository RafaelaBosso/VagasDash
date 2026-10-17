# VagasDash — Planejamento do MVP

> Nome provisório. O nome definitivo será escolhido posteriormente.

## 1. Visão geral

O VagasDash é uma aplicação web para organizar candidaturas a vagas de estágio e emprego. A aplicação centraliza informações sobre empresas, cargos, etapas dos processos seletivos e prazos de acompanhamento.

O projeto será desenvolvido como uma demonstração para portfólio, utilizando dados fictícios.

## 2. Problema e público-alvo

### Problema

Quem se candidata a várias vagas pode perder o controle das empresas, datas, etapas seletivas e retornos esperados quando essas informações ficam dispersas.

### Público-alvo

- Estudantes em busca de estágio;
- Pessoas em busca de emprego;
- Profissionais que desejam organizar seus processos seletivos.

## 3. Objetivos

- Desenvolver uma aplicação web usando Python;
- Praticar operações de cadastro, consulta, edição e exclusão;
- Armazenar dados em um banco SQLite;
- Implementar validações e regras de negócio;
- Criar filtros e indicadores;
- Importar e exportar dados CSV;
- Escrever testes automatizados;
- Documentar e publicar o projeto no GitHub.

## 4. Escopo do MVP

### Funcionalidades incluídas

1. Cadastrar candidaturas;
2. Listar, editar e excluir candidaturas;
3. Alterar o status de cada candidatura;
4. Destacar prazos de acompanhamento vencidos ou próximos;
5. Filtrar por empresa, cargo e status;
6. Exibir um dashboard com totais e distribuição por status;
7. Exportar candidaturas para CSV;
8. Importar arquivos CSV compatíveis, validando-os antes da gravação;
9. Preservar os dados entre reinicializações da aplicação.

### Fora do escopo inicial

- Login e cadastro de usuários;
- Integração com LinkedIn ou sites de emprego;
- Envio de e-mails ou mensagens;
- Recomendações por inteligência artificial;
- Aplicativo móvel;
- Sincronização entre vários usuários;
- Infraestrutura complexa de hospedagem.

## 5. Dados de uma candidatura

| Campo | Obrigatório? | Descrição |
|---|---|---|
| `id` | Sim, gerado pelo sistema | Identificador único |
| `empresa` | Sim | Nome da empresa |
| `cargo` | Sim | Nome da vaga |
| `link_vaga` | Não | Endereço do anúncio |
| `data_candidatura` | Sim | Data em que a candidatura foi enviada |
| `status` | Sim | Etapa atual do processo |
| `prazo_acompanhamento` | Não | Data planejada para verificar se houve retorno |
| `observacoes` | Não | Notas sobre a vaga ou processo |
| `criado_em` | Sim, gerado pelo sistema | Data e hora de criação do registro |

As datas serão armazenadas em formato padronizado `AAAA-MM-DD` quando representarem apenas uma data. A data de criação poderá incluir horário.

## 6. Status permitidos

- Para analisar
- Candidatura enviada
- Teste técnico
- Entrevista
- Oferta
- Recusada
- Encerrada

O MVP não exigirá que todas as candidaturas sigam uma sequência fixa de etapas.

## 7. Regras de negócio

### Cadastro e edição

- Empresa, cargo, data da candidatura e status são obrigatórios.
- O ID é gerado pelo sistema.
- Datas devem ser validadas.
- O status deve pertencer à lista permitida.
- Antes de excluir um registro, a interface deve solicitar confirmação.

### Prazos e alertas

- **Vencido:** o prazo de acompanhamento é anterior à data atual.
- **Próximo do vencimento:** o prazo é hoje ou ocorre nos próximos dois dias.
- **Sem prazo:** não foi definida uma data de acompanhamento.
- **Sem alerta:** o prazo está a mais de dois dias no futuro.
- Candidaturas com status `Oferta`, `Recusada` ou `Encerrada` não geram alertas de acompanhamento.

A regra será baseada na data local da aplicação, sem necessidade de notificações externas.

### Filtros e dashboard

- Os filtros poderão ser aplicados por empresa, cargo e status.
- Limpar os filtros exibirá novamente todos os registros.
- Os totais do dashboard serão calculados a partir dos dados armazenados.
- Uma base vazia deverá produzir indicadores iguais a zero, sem erros.

### CSV

- A exportação deverá incluir os campos documentados.
- O arquivo deverá preservar caracteres acentuados.
- A importação deverá validar cabeçalhos e valores antes de gravar os registros.
- Um arquivo inválido não deverá causar uma importação parcial acidental.
- A política exata para duplicatas e linhas inválidas será definida antes de implementar a importação.

## 8. Requisitos funcionais

| ID | Requisito |
|---|---|
| RF01 | Cadastrar candidatura |
| RF02 | Listar candidaturas |
| RF03 | Editar candidatura |
| RF04 | Excluir candidatura com confirmação |
| RF05 | Alterar status |
| RF06 | Identificar prazos vencidos e próximos |
| RF07 | Filtrar por empresa, cargo e status |
| RF08 | Exibir totais e distribuição por status |
| RF09 | Exportar dados para CSV |
| RF10 | Importar CSV após validação |

## 9. Requisitos não funcionais

| ID | Requisito |
|---|---|
| RNF01 | A interface deve ser compreensível e apresentar mensagens claras |
| RNF02 | Os dados devem persistir após reiniciar a aplicação |
| RNF03 | Os campos obrigatórios devem ser validados |
| RNF04 | Consultas SQL devem utilizar parâmetros |
| RNF05 | Interface, regras de negócio e acesso ao banco devem ser separados quando possível |
| RNF06 | A instalação deve ser documentada e reproduzível |
| RNF07 | As regras principais devem ter testes automatizados |
| RNF08 | O desenvolvimento não deve depender de serviços pagos |
| RNF09 | O repositório público deve usar dados fictícios e não conter segredos |
| RNF10 | O README deve explicar instalação, execução, funcionalidades e limitações |

## 10. Critérios de aceitação

- [ ] Um registro válido pode ser cadastrado e aparece na listagem.
- [ ] Empresa ou cargo vazio impede o cadastro e gera uma mensagem clara.
- [ ] Um registro pode ser editado e a alteração permanece após reiniciar a aplicação.
- [ ] A exclusão exige confirmação.
- [ ] Alterar o status atualiza a listagem e os indicadores.
- [ ] Prazos vencidos e próximos são identificados conforme as regras.
- [ ] Processos encerrados não geram alertas de acompanhamento.
- [ ] Os filtros retornam somente os registros correspondentes.
- [ ] Limpar os filtros restaura a listagem completa.
- [ ] Os totais do dashboard correspondem aos dados armazenados.
- [ ] O dashboard funciona quando não há registros.
- [ ] A exportação produz um CSV legível com caracteres acentuados.
- [ ] A importação valida o arquivo antes de gravar dados.
- [ ] Os testes automatizados das regras principais passam.
- [ ] Outra pessoa consegue instalar e executar o projeto seguindo a documentação.

## 11. Tecnologias previstas

- **Python:** linguagem principal;
- **Streamlit:** interface web;
- **SQLite:** armazenamento relacional;
- **pytest:** testes automatizados;
- **Git e GitHub:** versionamento e publicação;
- **CSV:** intercâmbio de dados.

As versões e dependências exatas serão registradas durante a configuração do ambiente.

## 12. Organização inicial prevista

```text
VagasDash/
├── app.py
├── database.py
├── services.py
├── requirements.txt
├── README.md
├── MVP.md
├── .gitignore
├── data/
│   └── exemplo_candidaturas.csv
└── tests/
    └── test_services.py
```

A estrutura poderá ser ajustada à medida que o projeto evoluir.

## 13. Etapas de desenvolvimento

1. Confirmar os requisitos e as regras de importação CSV;
2. Preparar o ambiente Python e o repositório Git;
3. Implementar a lógica inicial de candidaturas;
4. Integrar o SQLite;
5. Criar a interface com Streamlit;
6. Implementar alertas, filtros e dashboard;
7. Implementar importação e exportação CSV;
8. Criar e executar testes automatizados;
9. Revisar documentação e publicar o projeto.

## 14. Limitações conhecidas

- O MVP será destinado a uma demonstração individual, sem autenticação.
- Os alertas serão visuais e aparecerão quando a aplicação estiver aberta.
- Não haverá envio automático de notificações.
- A aplicação utilizará dados fictícios na demonstração pública.

## 15. Melhorias futuras possíveis

- API com FastAPI;
- Histórico de mudanças de status;
- Testes adicionais de integração;
- Melhorias de acessibilidade e interface;
- Demonstração hospedada gratuitamente, se viável;
- Importação com relatório detalhado de erros e duplicatas.

---
Documento inicial de planejamento. Atualizar conforme decisões e implementação do projeto.
