# library imports
import pandas as pd
from  pyspark.sql import functions as F

# import data
df = pd.read_csv('survey.csv')

# drop records with no comment
df = df.dropna(subset='comments')
print(df.comments)

# basic view
print(df.describe())
