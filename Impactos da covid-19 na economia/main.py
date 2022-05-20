import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

#O dataset possui dois arquivos, um raw_data e um transformed_data
data = pd.read_csv("dataset/transformed_data.csv")
data2 = pd.read_csv("dataset/raw_data.csv")
#print(data)

#print(data.head()) # método head mostra algumas amostras do dataset
#print(data2.head())

data["COUNTRY"].value_counts()
data["COUNTRY"].value_counts().mode()