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
del df['BMI']

# 3
# 更新cholesterol和gluc的值为简单的0或1，即正则化
df['cholesterol'] = df['cholesterol'].apply(lambda x: 1 if x > 1 else 0)
df['gluc'] =  df['gluc'].apply(lambda x: 1 if x > 1 else 0)


# 4
def draw_cat_plot():
    # 5
    # Create a DataFrame for the cat plot using pd.melt
    df_cat = pd.melt(df, id_vars='cardio', value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])


    # 6
    #Group and reformat the data in df_cat to split it by cardio. 
    # Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    

    # 7
    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar').fig


    # 8


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    # data cleaning
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) & 
                 (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    # Generate a mask for the upper triangle and store it in the mask variable
    mask = np.triu(corr)



    # 14
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15

    sns.heatmap(corr, annot=True, fmt='.1f', linewidths=1, mask=mask, square=True, cbar_kws={'shrink': 0.5})

    # 16
    fig.savefig('heatmap.png')
    return fig
