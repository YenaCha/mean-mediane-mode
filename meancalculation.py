import pandas as pd
df = pd.read_csv('C:/Users/yena0/Downloads/Python/class 104/SOCR-HeightWeight.csv')
height=df['Height(Inches)'].tolist()
sum = 0
for f in height:
    sum = sum+f
mean = sum/len(height)
print(mean)