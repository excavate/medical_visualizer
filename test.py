import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
# 计算BMI
df['BMI'] = (df['weight'] / (df['height'] / 100) ** 2).fillna(0)
df['overweight'] = df['BMI'].apply(lambda x: 1 if x > 25 else 0)

# 3
# 更新cholesterol和gluc的值为简单的0或1，即正则化
df['cholesterol'] = df['cholesterol'].apply(lambda x: 1 if x > 1 else 0)
df['gluc'] =  df['gluc'].apply(lambda x: 1 if x > 1 else 0)

df_cat = pd.melt(df, id_vars='cardio', value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])
df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

print(df_cat,type(df_cat))