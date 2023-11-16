import datetime
import random
import sqlite3

# Conectar ao banco de dados (substitua 'nome_do_banco.db' pelo nome do seu banco de dados)
conn = sqlite3.connect('nome_do_banco.db')
c = conn.cursor()

# Criar tabela para armazenar dados de produção de gado de corte
c.execute('''
          CREATE TABLE IF NOT EXISTS producao_gado_corte (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              data_registro TEXT,
              peso INTEGER,
              saude TEXT
          )
          ''')

# Função para adicionar um novo registro de produção de gado de corte
def adicionar_registro_producao(peso, saude):
    data_registro = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO producao_gado_corte (data_registro, peso, saude) VALUES (?, ?, ?)",
              (data_registro, peso, saude))
    conn.commit()
    print(f"Registro de produção de gado de corte adicionado.")

# Função para consultar a produção de gado de corte por período
def consultar_producao_por_periodo(data_inicial, data_final):
    c.execute("SELECT * FROM producao_gado_corte WHERE data_registro BETWEEN ? AND ?",
              (data_inicial, data_final))
    rows = c.fetchall()
    for row in rows:
        print(row)

# Exemplo de uso das funções
peso_gado = random.randint(300, 800)  # Peso do gado em quilogramas (um exemplo aleatório)
saude_gado = "Saudável"  # Condição de saúde do gado (um exemplo fixo)
adicionar_registro_producao(peso_gado, saude_gado)

# Consultar produção de gado de corte para o último mês
data_atual = datetime.datetime.now()
data_inicial = (data_atual - datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S")
data_final = data_atual.strftime("%Y-%m-%d %H:%M:%S")
consultar_producao_por_periodo(data_inicial, data_final)

# Fechar a conexão com o banco de dados
conn.close()
