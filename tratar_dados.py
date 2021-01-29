import pandas as pd

#file = "data/olist/olist_order_items_dataset.csv"
file = "data/out/main_seller.csv"
#out = open('data/out/data.txt', 'w')
out = open('data/out/seller_data.txt', 'w')
data = pd.read_csv(file, usecols=['order_id','product_id'])
#print(type(data))
#print(data.head(10))
#print(data.count())
#print(data.describe())
#print(data.info())
#print(data["product_id"])

count = 0
total_linha = 0
line = ''
#print(data['order_id'][0])

for index, r in data.iterrows():
 
    if (count > 0):
        if ((r['order_id'] == order_id_prev) and (count > 1) and (product_id_prev != r['product_id'])):
            #print(count, ' - ', r['order_id'], order_id_prev, ' igual')
            line = line + ' ' + r['product_id']
            total_linha += 1
            #print(line)
        else:
            #print(count, ' - ', r['order_id'], ' diferente')

            if(total_linha > 1):
                print(line)
                out.write(line + '\n')
            

            order_id_prev = r['order_id']
            product_id_prev = r['product_id']
            line = r['product_id']
            total_linha = 1
            #print(line)
    else:
        order_id_prev = data['order_id'][0]
        line = data['product_id'][0]
        
        print('iniciou')

    count += 1    
    #print( r['order_id'], r['product_id'])
    #count += 1



print('TOTAL: ', count)
out.close()

