#!/usr/bin/env python
# coding: utf-8

# # Project in Pandas (Covid-19)

# We'll download this file using the urlretrieve function from the urllib.request module

# In[1]:


from urllib.request import urlretrieve
urlretrieve('https://hub.jovian.ml/wp-content/uploads/2020/09/italy-covid-daywise.csv', 
            'italy-covid-daywise.csv')


# In[2]:


import pandas as pd
covid_df = pd.read_csv('italy-covid-daywise.csv')


# In[3]:


type(covid_df)


# In[4]:


covid_df


# In[5]:


covid_df.info()


# In[6]:


covid_df.describe()


# In[7]:


covid_df.columns


# In[9]:


covid_df.shape


# In[10]:


get_ipython().system('pip install jovian --upgrade --quiet')


# In[11]:


import jovian


# In[12]:


jovian.commit(project='python-pandas-data-analysis')


# # Retrieving data from a data frame
# The first thing you might want to do is to retrieve data from this data frame e.g. the counts of a specific day or the list of values in a specific column. To do this, it might help to understand the internal representation of data in a data frame. Conceptually, you can think of a dataframe as a dictionary of lists: the keys are column names, and the values are lists/arrays containing data for the respective columns.
# 

# In[13]:


covid_df['new_cases']


# Each column is represented using a data structure called Series, which is essentially a numpy array with some extra methods and properties.
# 
# 

# In[14]:


type(covid_df['new_cases'])


# In[15]:


covid_df['new_cases'][246]


# Pandas also provides the .at method to directly retrieve at a specific row & column.

# In[16]:


covid_df.at[246,'new_cases']


# Instead of using the indexing notation [], Pandas also allows accessing columns as properties of the data frame using the . notation. However, this method only works for columns whose names do not contain spaces or special chracters.
# 
# covid_df.new_cases

# In[17]:


covid_df.new_cases


# In[22]:


cases_df = covid_df[['date','new_cases']]
cases_df


# Sometimes you might need a full copy of the data frame, in which case you can use the copy method

# In[23]:


covid_df_copy = covid_df.copy()


# The data within covid_df_copy is completely separate from covid_df, and changing values inside one of them will not affect the other.

# To access a specific row of data Pandas provides the .loc method.
# 
# 

# In[24]:


covid_df


# In[27]:


covid_df.loc[243]


# In[34]:


covid_df.loc[108:114]


# To view the first or last few rows of data, we can use the .head and .tail methods.

# In[28]:


covid_df.head(5)


# In[29]:


covid_df.tail(5)


# Notice above that while the first few values in the new_cases and new_deaths columns are 0, the corresponding values within the new_tests column are NaN. That is because the CSV file does not contain any data for the new_tests column for certain dates (you can verify this by looking into the file). It's possible that these values are missing or unknown.

# In[31]:


covid_df.at[0,'new_tests']


# We can find the first index that doesn't contain a NaN value using first_valid_index method of a series

# In[33]:


covid_df.new_tests.first_valid_index()


# The .sample method can be used to retrieve a random sample of rows from the data frame.
# 

# In[35]:


covid_df.sample(12)


# In[36]:


import jovian


# In[37]:


jovian.commit()


# # Analyzing Data from data frames
# 
# Q: What is the total number of reported cases and deaths related to Covid-19 in Italy?

# Similar to Numpy arrays, a Pandas series supports the sum method to answer these questions.

# In[127]:


total_cases = covid_df.new_cases.sum()# total number of reported cases
total_cases


# In[128]:


total_deaths = covid_df.new_deaths.sum() # total number of reported deaths
total_deaths


# In[129]:


print('The number of reported cases is {} and the number of reported deaths is {}.'.format(int(total_cases), int(total_deaths)))


# Q: What is the overall death rate (ratio of reported deats to reported cases)?

# In[130]:


death_rate = covid_df.new_deaths.sum() / covid_df.new_cases.sum()
death_rate


# In[131]:


print("The overall reported death rate in Italy is {:.2f} %.".format(death_rate*100))


# Q: What is the overall number of tests conducted? A total of 935310 tests were conducted before daily test numbers were being reported.

# In[132]:


initial_tests = 935310
total_tests = initial_tests + covid_df.new_tests.sum()
total_tests


# Q: What fraction of test returned a postive result?

# In[133]:


positive_rate = total_cases/total_tests
positive_rate


# In[134]:


print('{:.2f}% of tests in Italy led to a positive diagnosis.'.format(positive_rate*100))


# In[135]:


import jovian


# In[136]:


jovian.commit()


# # Querying and sorting rows¶
# Let's say we want only want to look at the days which had more than 1000 reported cases. We can use a boolean expression to chech which rows satisfy this criterion.

# In[137]:


high_new_cases = covid_df.new_cases > 1000
high_new_cases


# In[138]:


covid_df[high_new_cases]


# The data frame contains 72 rows, but only the first 5 & last 5 rows are displayed by default with Jupyter, for brevity. To view, all the rows, we can modify some display options.

# In[139]:


from IPython.display import display
with pd.option_context('display.max_rows', 100):
    display(covid_df[covid_df.new_cases > 1000])


# Determine the days when the ratio of cases reported to tests conducted is higher than the overall positive_rate.

# In[140]:


positive_rate
high_ratio_df = covid_df[covid_df.new_cases / covid_df.new_tests > positive_rate]
high_ratio_df


# In[141]:


covid_df['positive_rate'] = covid_df.new_cases/covid_df.new_tests
covid_df


# let's remove the positive_rate column using the drop method.

# In[142]:


covid_df.drop(columns = ['positive_rate'],inplace = False) # we uses inplace = False for temporary removal of positive_rate


# In[143]:


covid_df


# # Sorting rows using column values

# In[144]:


covid_df.sort_values('new_cases',ascending = False).head(10)


# It looks like the last two weeks of March had the highest number of daily cases. Let's compare this to the days where the highest number of deaths were recorded.

# In[145]:


import jovian
jovian.commit()


# # Working with dates

# In[146]:


covid_df.date


# The data type of date is currently object, so Pandas does not know that this column is a date. We can convert it into a datetime column using the pd.to_datetime method.

# In[147]:


covid_df['date'] = pd.to_datetime(covid_df.date)
covid_df['date']


# You can see that it now has the datatype datetime64. We can now extract different parts of the data into separate columns, using the DatetimeIndex class

# In[148]:


covid_df['year'] = pd.DatetimeIndex(covid_df.date).year
covid_df['month'] = pd.DatetimeIndex(covid_df.date).month
covid_df['day'] = pd.DatetimeIndex(covid_df.date).day
covid_df['weekday'] = pd.DatetimeIndex(covid_df.date).weekday


# In[149]:


covid_df


# Let's check the overall metrics for the month of May. We can query the rows for May, choose a subset of colums that we want to aggregate, and use the sum method of the data frame to get the sum of values in each chosen column

# In[150]:


covid_df_may = covid_df[covid_df.month == 5]
covid_df_may_metrices = covid_df_may[['new_cases','new_deaths','new_tests']]
covid_df_total = covid_df_may_metrices.sum()


# In[151]:


covid_df_total


# OR

# In[152]:


covid_df[covid_df.month == 5][['new_cases','new_deaths','new_tests']].sum()


# In[153]:


import jovian
jovian.commit()


# # Grouping and aggregation

# As a next step, we might want to summarize the daywise data and create a new dataframe with month-wise data. This is where the groupby funtion is useful. Along with a grouping, we need to specify a way to aggregate the data for each group.

# In[154]:


covid_month_df = covid_df.groupby('month')[['new_cases','new_deaths','new_tests']].sum()
covid_month_df


# Aggregation by mean

# In[155]:


covid_month_mean_df = covid_df.groupby('month')[['new_cases','new_deaths','new_tests']].mean()
covid_month_mean_df


# In[162]:


covid_df['total_cases'] = covid_df.new_cases.cumsum()
covid_df['total_deaths'] = covid_df.new_deaths.cumsum()
covid_df['total_tests'] = covid_df.new_tests.cumsum() + initial_tests


# # Merging data from multiple sources

# To determine other metrics like test per million, cases per million etc. we require more some information about the country viz. it's population. Let's download another file locations.csv which contains health-related information for different countries around the world, including Italy.

# In[163]:


urlretrieve('https://hub.jovian.ml/wp-content/uploads/2020/09/locations.csv', 
            'locations.csv')


# In[164]:


locations_df = pd.read_csv('locations.csv')
locations_df


# In[165]:


locations_df[locations_df.location == 'Italy']


# We can merge this data into our existing data frame by adding more columns. However, to merge two data frames, we need at least one common column. So let's insert a location column in the covid_df dataframe with all values set to "Italy".

# In[166]:


covid_df["location"] = 'Italy'
covid_df


# We can now add the columns from locations_df into covid_df using the .merge method.

# In[167]:


merged_df = covid_df.merge(locations_df, on='location')
merged_df


# In[168]:


merged_df['cases_per_million'] = merged_df.total_cases * 1e6 / merged_df.population
merged_df['deaths_per_million'] = merged_df.total_deaths * 1e6 / merged_df.population
merged_df['tests_per_million'] = merged_df.total_tests * 1e6 / merged_df.population
merged_df


# In[169]:


import jovian
jovian.commit()


# # Writing back to files

# In[170]:


result_df = merged_df[['date',
                       'new_cases', 
                       'total_cases', 
                       'new_deaths', 
                       'total_deaths', 
                       'new_tests', 
                       'total_tests', 
                       'cases_per_million', 
                       'deaths_per_million', 
                       'tests_per_million']]


# In[171]:


result_df


# To write the data from the data frame into a file, we can use the to_csv function.

# In[178]:


result_df.to_csv('result.csv',index = None)


# In[180]:


import jovian
jovian.commit()


# # Plotting with pandas

# In[181]:


result_df.set_index('date',inplace = True)


# In[182]:


result_df


# In[190]:


result_df.new_cases.plot(title = "New Cases",kind ='line')


# In[191]:


import jovian
jovian.commit()


# In[ ]:




