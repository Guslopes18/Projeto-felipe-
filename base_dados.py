import pandas as pd 

teste_csv = pd.read_csv('tabela_carro_atual.csv')
teste_df = pd.DataFrame(teste_csv)
print(teste_df)
