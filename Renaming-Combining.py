import pandas as pd 
PD_reviews = pd.read_csv('US_politicians_Twitter.csv')
'''Renaming'''
# The first function we'll introduce here is rename(),which lets you change index names and/or column names. For example, to change the sex column in our dataset to gender.
PD_reviews.rename(columns={'Sex':'Gender'})
# rename() lets you rename index or column values by specifying a index or column keyword parameter, respectively. It supports a variety of input formats, but usually a Python dictionary is the most convenient.
PD_reviews.rename(index = {0:'firstEntry',1:'secondEntry'})
# You'll probably rename columns very  often, but rename index values very rarely. For that, set_index() is usually more convenient.
# Both the row index and the column index can have their own name attribute. The complimentary  rename_axis() method may be used to change these name.
PD_reviews.rename_axis('attributes',axis = 'columns').rename_axis('Entries',axis='rows')

'''Combining'''
# When performing operations on a dataset, we will sometimes need to combine different DataFrames, Series in non-trivial ways. Pandas has three core methods for doing this. In order of increasing complexity, these are concat(),join(),and merge(). Most of what merge() can do can also be done more simply with join(), so we will omit it and focus on the first two functions here.
# The simplest combining method is concat(). Given a list of elements, this function will smash those elements together along an axis.
# This is useful when we have data in different DataFrame or Series objects but having the same fields.
''' pd.concat([a,b])'''
# The middlemost combiner in terms of complexity is join(). join() lets you combine different DataFrame objects which have an index in common. 
'''left.join(right,lsuffix='',rsuffix='')'''
# The lsuffix and rsuffix parameters are necessary here because the data has the same column names in both datasets. If this wasn't true.