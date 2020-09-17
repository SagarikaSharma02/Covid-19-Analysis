#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Run the next line to install Pandas
get_ipython().system('pip install pandas --upgrade')


# In[6]:


import pandas as pd


# In this assignment, we're going to analyze an operate on data from a CSV file. Let's begin by downloading the CSV file.

# In[7]:


from urllib.request import urlretrieve

urlretrieve('https://hub.jovian.ml/wp-content/uploads/2020/09/countries.csv', 
            'countries.csv')


# Let's load the data from the CSV file into a Pandas data frame.

# In[8]:


countries_df = pd.read_csv('countries.csv')


# In[9]:


countries_df


# **Q: How many countries does the dataframe contain?**
# 
# Hint: Use the `.shape` method.

# In[10]:


num_countries = countries_df.shape[0]


# In[11]:


print('There are {} countries in the dataset'.format(num_countries))


# **Q: Retrieve a list of continents from the dataframe?**
# 
# *Hint: Use the `.unique` method of a series.*

# In[13]:


continents = countries_df.continent.unique()


# In[14]:


continents


# **Q: What is the total population of all the countries listed in this dataset?**

# In[16]:


total_population = countries_df.population.sum()


# In[17]:


print('The total population is {}.'.format(int(total_population)))


# **Q: (Optional) What is the overall life expectancy across in the world?**
# 
# *Hint: You'll need to take a weighted average of life expectancy using populations as weights.*

# In[19]:


weighted_sum = (countries_df.population * countries_df.life_expectancy).sum()


# In[20]:


weighted_average = weighted_sum / countries_df.population.sum()
print ('The overall life expectancy across the world is {:.3f}'.format(weighted_average))


# **Q: Create a dataframe containing 10 countries with the highest population.**
# 
# *Hint: Chain the `sort_values` and `head` methods.*

# In[22]:


most_populous_df = countries_df.sort_values('population', ascending=False).head(10)


# In[23]:


most_populous_df


# **Q: Add a new column in `countries_df` to record the overall GDP per country (product of population & per capita GDP).**
# 
# 

# In[26]:


countries_df['gdp'] = countries_df.population * countries_df.gdp_per_capita


# In[29]:


countries_df


# **Q: (Optional) Create a dataframe containing 10 countries with the lowest GDP per capita, among the counties with population greater than 100 million.**

# In[31]:


df = countries_df[countries_df.population > 1e8].sort_values('gdp_per_capita', ascending=True).head(10)


# In[32]:


df


# **Q: Create a data frame that counts the number countries in each continent?**
# 
# *Hint: Use `groupby`, select the `location` column and aggregate using `count`.*

# In[34]:


country_counts_df = countries_df.groupby('continent')['location'].count()


# In[35]:


country_counts_df


# **Q: Create a data frame showing the total population of each continent.**
# 
# *Hint: Use `groupby`, select the population column and aggregate using `sum`.*

# In[37]:


continent_populations_df = countries_df.groupby('continent')['population'].sum()


# In[38]:


continent_populations_df


# Let's download another CSV file containing overall Covid-19 stats for various countires, and read the data into another Pandas data frame.

# In[40]:


urlretrieve('https://hub.jovian.ml/wp-content/uploads/2020/09/covid-countries-data.csv', 
            'covid-countries-data.csv')


# In[41]:


covid_data_df = pd.read_csv('covid-countries-data.csv')


# In[42]:


covid_data_df


# **Q: Count the number of countries for which the `total_tests` data is missing.**
# 
# *Hint: Use the `.isna` method.*

# In[43]:


total_tests_missing = covid_data_df.total_tests.isna().sum()
total_tests_missing


# In[44]:


print("The data for total tests is missing for {} countries.".format(int(total_tests_missing)))


# Let's merge the two data frames, and compute some more metrics.
# 
# **Q: Merge `countries_df` with `covid_data_df` on the `location` column.**
# 
# *Hint: Use the `.merge` method on `countries_df`.

# In[46]:


combined_df = countries_df.merge(covid_data_df, on='location')


# In[47]:


combined_df


# **Q: Add columns `tests_per_million`, `cases_per_million` and `deaths_per_million` into `combined_df`.**

# In[49]:


combined_df['tests_per_million'] = combined_df['total_tests'] * 1e6 / combined_df['population']


# In[50]:


combined_df['cases_per_million'] = combined_df['total_cases'] * 1e6 / combined_df['population']


# In[51]:


combined_df['deaths_per_million'] = combined_df['total_deaths'] * 1e6 / combined_df['population']


# In[52]:


combined_df


# **Q: Create a dataframe with 10 countires that have highest number of tests per million people.**

# In[54]:


highest_tests_df = combined_df.sort_values('tests_per_million', ascending=False).head(10)


# In[55]:


highest_tests_df


# **Q: Create a dataframe with 10 countires that have highest number of positive cases per million people.**

# In[57]:


highest_cases_df = combined_df.sort_values('cases_per_million', ascending=False).head(10)


# In[58]:


highest_cases_df


# **Q: Create a dataframe with 10 countires that have highest number of deaths cases per million people?**

# In[60]:


highest_deaths_df = combined_df.sort_values('deaths_per_million', ascending=False).head(10)


# In[61]:


highest_deaths_df


# **Q: Count number of countries that feature in both the lists of "highest number of tests per million" and "highest number of cases per million".**

# In[63]:


total_count = highest_tests_df.location.isin(highest_cases_df.location).sum()

print ('The total count of the countries is {}'.format(total_count))


# **Q: Count number of countries that feature in both the lists "20 countries with lowest GDP per capita" and "20 countries with the lowest number of hospital beds per thousand population". Only consider countries with a population higher than 10 million while creating the list.**

# In[112]:


lowest_gdp_df = countries_df[countries_df.population > 1e7].sort_values('gdp_per_capita', ascending=True).head(20)
lowest_gdp_df


# In[113]:


lowest_hospital_beds_df = countries_df[countries_df.population>1e7].sort_values('hospital_beds_per_thousand', ascending=True).head(20)
lowest_hospital_beds_df


# In[115]:


total_count = lowest_gdp_df.location.isin(lowest_hospital_beds_df.location).sum()
print ('The total count is {}'.format(total_count))


# In[ ]:




