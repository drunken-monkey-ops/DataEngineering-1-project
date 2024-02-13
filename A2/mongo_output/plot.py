import pandas as pd


list_ = [
  { 'count': 383911, 'pronoun': 'det' },
  { 'count': 23976, 'pronoun': 'hen' },
  { 'count': 18283, 'pronoun': 'denna' },
  { 'count': 1031460, 'pronoun': 'den' },
  { 'count': 267523, 'pronoun': 'hon' },
  { 'count': 597481, 'pronoun': 'han' },
  { 'count': 3227, 'pronoun': 'denne' }
]

df = pd.DataFrame(list_)

df['count'] = df['count'].apply(lambda x: (x/df['count'].sum())*100)
labels = df['count'].round(1).astype('str') + '%'


ax = df.plot.bar(x='pronoun', y='count',color='#f53b57',figsize = (10, 10), title='Percentage of pronouns',xlabel = 'pronouns', ylabel = 'percentage')


for container in ax.containers:

    ax.bar_label(container, labels=labels)


ax.get_figure().savefig('mongo_count.png')

print(df)