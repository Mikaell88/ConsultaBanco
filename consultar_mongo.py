from pymongo import MongoClient

# Conexão (com sua URI atualizada)
client = MongoClient("mongodb+srv://mikaelsby:mk123456@cluster0.4zapnmf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Seleciona o banco e a coleção
db = client['bigdata_games']
colecao = db['vendas_jogos']

# Consulta todos os documentos (retorna um cursor)
#resultados = colecao.find()

#for documento in resultados:
#    print(documento)

#filtro = {"year": 2015}
#resultados = colecao.find(filtro)

#for doc in resultados:
#    print(doc)


#resultados = colecao.find().limit(5)

#for doc in resultados:
#    print(doc)

#jogo = colecao.find_one({"name": "New Super Mario Bros. Wii"})
#print(jogo)


#filtro = {"year": 2015, "platform": "PS4"}
#for doc in colecao.find(filtro):
#    print(doc)

