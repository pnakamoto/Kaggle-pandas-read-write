import pandas as pd
pd.set_option('display.max_rows', 5)
from learntools.core import binder; binder.bind(globals())
from learntools.pandas.creating_reading_and_writing import *
print("Setup complete.")

# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruits.
fruits = pd.DataFrame([[30, 21]], columns=['Apples', 'Bananas'])

# Check your answer
q1.check()
fruits

Apples	Bananas
0	30	21

# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruit_sales.
fruit_sales = pd.DataFrame({'Apples':[35, 41], 'Bananas':[21, 34]},
                 index=['2017 Sales', '2018 Sales'])

# Check your answer
q2.check()
fruit_sales


Apples	Bananas
2017 Sales	35	21
2018 Sales	41	34

quantities = ['4 cups', '1 cup', '2 large', '1 can']
items = ['Flour', 'Milk', 'Eggs', 'Spam']
recipe = pd.Series(quantities, index=items, name='Dinner')

# Check your answer
q3.check()

reviews = pd.read_csv('../input/wine-reviews/winemag-data_first150k.csv', index_col=0)

# Check your answer
q4.check()
reviews

reviews = pd.read_csv('../input/wine-reviews/winemag-data_first150k.csv', index_col=0)

# Check your answer
q4.check()
reviews

animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
animals


Cows	Goats
Year 1	12	22
Year 2	20	19

# Your code goes here
animals.to_csv("cows_and_goats.csv")
# Check your answer
q5.check()
