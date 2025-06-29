import pandas as pd
from pymongo import MongoClient

# Caminho para o arquivo CSV
csv_path = 'video_games_sales.csv'

# 1. Carrega os dados
df = pd.read_csv(csv_path)

# 2. Limpa valores nulos ou problemáticos
df.dropna(subset=['name', 'platform', 'year'], inplace=True)

# 3. Converte ano para inteiro
df['year'] = df['year'].astype(int)

# 4. Conecta ao MongoDB local (ou substitua pela URI do Atlas)
client = MongoClient("mongodb+srv://SEU_USUARIO:SUA_SENHA@cluster0.4zapnmf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client['bigdata_games']
colecao = db['vendas_jogos']

# 5. Transforma o DataFrame em dicionários
dados = df.to_dict(orient='records')

# 6. Insere os dados no MongoDB
colecao.insert_many(dados)

print("✅ Dados carregados com sucesso no MongoDB!")
