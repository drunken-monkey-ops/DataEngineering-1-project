import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('~/part-00000',sep=' ',names = ['pronoun','count'])


df['count'] = df['count'].apply(lambda x: (x/df['count'].sum())*100)
labels = df['count'].round(1).astype('str') + '%'


ax = df.plot.bar(x='pronoun', y='count',color='#B33771',figsize = (10, 10), title='Percentage of pronouns',xlabel = 'pronouns', ylabel = 'percentage')


for container in ax.containers:

    ax.bar_label(container, labels=labels)
   

ax.get_figure().savefig('tweet_count.png')

print(df)
