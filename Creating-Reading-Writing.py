import pandas as pd 
#Creating data - There are two core objects in pandas: the DataFrame and the Series
'''DataFrame'''
#DataFrame is a table. It contains an array of individual entries, each of which has a certain value. Each entry corresponds to a row and a column
sample0 = pd.DataFrame({'Yes':[50,21],'No':[131,2]})
print(sample0)
#DataFrame entries are not limited to integers. For instance, here's DataFrame whose values are strings
sample1 = pd.DataFrame({'Bob':['I am fine.','It was awful.'],'Chris':['Pretty good.','Bland.']})
print(sample1)
#The list of row labels used in a DataFrame is known as an Index. We can assign values to it by using an index parameter in our constructor:
sample2 = pd.DataFrame({'Bob':['I am fine.','It was awful.'],'Chris':['Pretty good.','Bland.']},index = ['product A','product B'])
print(sample2)
'''Series'''
#A Series, by contrast, is a sequence of data values. If a DataFrame is a table, a Series is a list. And in fact you can create one with nothing more than a list:
sample3 = pd.Series([1,2,3,4,5])
print(sample3)
#A Series is, in essence, a single column of a DataFrame. So you can assign column values to the Series the same way as before, using an index parameter. However, a Series does not have a column name, it only has one overall name:
sample4 = pd.Series([30,35,40],index=['2020 Sales','2021 Sales','2022 Sales'],name = 'Product A')
print(sample4)
'''Reading data files'''
# Comma-Separated-Values - CSV
PD_reviews = pd.read_csv('US_politicians_Twitter.csv')
print(PD_reviews.shape) #Use shape attribute to check how large the resulting DataFrame is
# 2514 records split across 10 different columns.
print(PD_reviews.head()) # Using head() command, which grabs the first five rows
#To make pandas use the column for the index (instead of creating a new one from scratch), we can specify an index_col.
PD_reviews1 = pd.read_csv('US_politicians_Twitter.csv',index_col=0)
print(PD_reviews1.head())
