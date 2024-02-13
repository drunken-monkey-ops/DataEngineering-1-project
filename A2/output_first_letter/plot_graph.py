import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('part-r-00000.tsv', sep='\t', names=["Character","Count"])

print(df)

plt.bar(df['Character'], df['Count'])
plt.xlabel('Letters')
plt.ylabel('Counts')
plt.title('Occurrences of Words Starting with the Same First Letter')
plt.savefig('output_first_letter-png')
