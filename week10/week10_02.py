import seaborn as sns
import pandas as pd

print(sns.get_dataset_names())
mpg = sns.load_dataset('mpg')
print(mpg.head().sort_values('mpg'))