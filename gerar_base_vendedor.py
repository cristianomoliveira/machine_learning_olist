import pandas as pd

file = "data/olist/olist_order_items_dataset.csv"
data = pd.read_csv(file)
out = open('data/out/seller_data.txt', 'w')

#print(data)

novo = data.sort_values('seller_id') \
        .groupby('seller_id')['order_id'] \
        .count() \
        .reset_index(name='count') \
        .sort_values(['count'], ascending=False) \
        .head(10)



cod_maior = novo["seller_id"].iloc[0]
n_vendas = novo["count"].iloc[0]
print("O maior vendedor é: ", str(cod_maior), " com o total de vendas: ", n_vendas)

principal = data[data['seller_id'] == cod_maior]
#print(principal)


principal.to_csv('data/out/main_seller.csv', index=False)