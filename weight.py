import pandas as pd
import statistics as st
df = pd.read_csv('C:/Users/yena0/Downloads/Python/class 104/SOCR-HeightWeight.csv')
weight = df['Weight(Pounds)'].tolist()
mean = st.mean(weight)
print(mean)