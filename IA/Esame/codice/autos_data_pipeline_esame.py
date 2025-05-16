import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# 1. Lettura e rinomina colonne
df_customers = pd.read_csv("Esame/dati/retail/customer.csv")
df_products = pd.read_csv("Esame/dati/retail/product.csv")
df_transactions = pd.read_csv("Esame/dati/retail/transaction.csv")

df_customers.rename(columns={"CustomerID": "Customer_ID", "Country": "Nation"}, inplace=True)
df_products.rename(columns={"StockCode": "Product_Code", "Description": "Product_Description"}, inplace=True)

# 2. Unione clienti + transazioni e scrittura su DB
df_ct = pd.merge(df_transactions, df_customers, on="Customer_ID")

# Parametri di accesso
engine = create_engine("postgresql+psycopg2://admin@pgadmin.org:admin@localhost:5000/clienti_transazioni")
df_ct.to_sql("clienti_transazioni", engine, if_exists='replace', index=False)

df_ct_db = pd.read_sql("SELECT * FROM clienti_transazioni", con=engine)

# 3. Merge con prodotti e pulizia
df_full = pd.merge(df_ct_db, df_products, on="Product_Code")
df_full['Product_Code'].replace(["POST", "C2", "D", "M"], "?", inplace=True)
df_full['Nation'] = df_full['Nation'].apply(lambda x: "?" if "," in str(x) else x)
df_full.replace("?", np.nan, inplace=True)
df_full = df_full[df_full['Product_Code'].notnull()]
mode_nation = df_full['Nation'].mode()[0]
df_full['Nation'].fillna(mode_nation, inplace=True)
df_full = df_full[df_full['Nation'] != "Unspecified"]
df_full = df_full[df_full['Nation'] != "UK"]
df_full = df_full[df_full['Quantity'] >= 0]
df_full = df_full.convert_dtypes()

# 4. Visualizzazioni
top_products = df_full.groupby('Product_Description')['InvoiceNo'].nunique().nlargest(5)
plt.figure(figsize=(10, 6))
top_products.plot(kind='bar')
plt.title("Top 5 prodotti per numero di fatture")
plt.xlabel("Prodotto")
plt.ylabel("Numero di fatture")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Esame/visual/top5_prodotti_fatture.png")

prod_per_invoice = df_full.groupby('InvoiceNo')['Product_Code'].nunique()
plt.figure(figsize=(10, 6))
prod_per_invoice.plot(kind='hist', bins=20)
plt.title("Distribuzione numero prodotti per fattura")
plt.xlabel("Numero prodotti distinti")
plt.ylabel("Frequenza")
plt.tight_layout()
plt.savefig("Esame/visual/distribuzione_prodotti_fattura.png")