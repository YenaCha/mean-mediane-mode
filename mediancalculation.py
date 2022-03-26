import pandas as pd
df = pd.read_csv('C:/Users/yena0/Downloads/Python/class 104/SOCR-HeightWeight.csv')
height=df['Height(Inches)'].tolist()
n = len(height)
if(n % 2 == 0):
    median = height[n//2]
else:
    median = (height[(n+1)//2]+height[(n-1)//2])/2
print(median)