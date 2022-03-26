import pandas as pd
import statistics as st
df = pd.read_csv('C:/Users/yena0/Downloads/Python/class 104/SOCR-HeightWeight.csv')
height=df['Height(Inches)'].tolist()
weight=df['Weight(Pounds)'].tolist()
modeh = st.mode(height)
modew = st.mode(weight)
print('Height : '+str(modeh))
print('Weight : '+str(modew))