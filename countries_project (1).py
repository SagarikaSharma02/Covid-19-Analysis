#!/usr/bin/env python
# coding: utf-8

# In[1]:


import jovian
jovian.commit(project='pandas-practice-assignment-19', environment=None)


# In[2]:


import pandas as pd


# In[3]:


from urllib.request import urlretrieve
urlretrieve('https://hub.jovian.ml/wp-content/uploads/2020/09/countries.csv', 
            'countries.csv')


# In[4]:


countries_df = pd.read_csv('countries.csv')


# In[5]:


countries_df


# Q: How many countries does the dataframe contain ?

# In[6]:


num_countries = countries_df.shape[0]


# In[7]:


print('There are {} countries in the dataset'.format(num_countries))


# In[16]:


jovian.commit(project='pandas-practice-assignment-19', environment=None)


# Q: Retrieve a list of continents from the continents?

# In[17]:


continents = countries_df['continent'].unique()
continents


# Q: what is the total population of all the countries listed in this dataset?

# In[18]:


total_population = countries_df['population'].sum()


# In[19]:


print('The total population is {} .'.format(int(total_population)))


# Q: What is the over all life expectancy across in the world ?

# Q: What is the overall life expectancy across the globe?

# In[20]:


overall_life_expectancy = (countries_df['population']*countries_df['life_expectancy']).sum()/countries_df['population'].sum()


# In[21]:


print('The overall life expectancy across the globe is {}.'.format(overall_life_expectancy))


# In[22]:


jovian.commit(project='pandas-practice-assignment-19', environment=None)


# Q: Top 10 countries with the highest population?

# In[23]:


most_populous_df = countries_df.sort_values('population',ascending = False).head(10)


# In[24]:


most_populous_df


# Q: Add a new column in countries_df to record the overall GDP per country(product of population and per capita GDP)

# In[25]:


jovian.commit(project='pandas-practice-assignment-19', environment=None)


# Q: Create a dataframe containing 10 countries with the lowest GDP per capita, among the counties with population greater than 100 million.

# In[26]:


new_df = countries_df.sort_values('gdp_per_capita',ascending = True)


# In[27]:


new_df[new_df['population']>100].head(10)


# Q: create a data frame that counts the number of countries in each continent?

# In[28]:


country_count_df = countries_df.groupby('continent')['location'].count()
country_count_df


# Let's download another CSV file containing overall Covid-19 stats for various countires, and read the data into another Pandas data frame

# In[29]:


urlretrieve('https://hub.jovian.ml/wp-content/uploads/2020/09/covid-countries-data.csv', 
            'covid-countries-data.csv')


# In[30]:


covid_data_df = pd.read_csv('covid-countries-data.csv')


# In[31]:


covid_data_df


# Q: Merge countries_df with covid_data_df on the location column.

# In[32]:


combined_df = covid_data_df.merge(countries_df,on = 'location')


# In[33]:


combined_df


# Q: Add columns tests_per_million, cases_per_million and deaths_per_million into combined_df.

# In[34]:


combined_df['tests_per_million'] = combined_df['total_tests'] * 1e6 / combined_df['population']
combined_df['cases_per_million'] = combined_df['total_cases'] * 1e6 / combined_df['population']
combined_df['deaths_per_million'] = combined_df['total_deaths'] * 1e6 / combined_df['population']


# In[35]:


combined_df


# Q: Create a dataframe with 10 countires that have highest number of tests per million people.

# In[36]:


highest_tests_df = combined_df.sort_values('tests_per_million',ascending = False).head(10)
highest_tests_df


# In[37]:


highest_cases_df = combined_df.sort_values('cases_per_million',ascending = False).head(10)
highest_cases_df


# In[38]:


highest_deaths_df = combined_df.sort_values('deaths_per_million',ascending = False).head(10)
highest_deaths_df


# Q:Count number of countries that feature in both the lists of "highest number of tests per million" and "highest number of cases per million".

# In[39]:


new_df = highest_tests_df.merge(highest_cases_df,on = 'location')
new_df


# There are 2 countries that are in both highest_tests and highest_cases

# Q: Count number of countries that feature in both the lists "20 countries with lowest GDP per capita" and "20 countries with the lowest number of hospital beds per thousand population". Only consider countries with a population higher than 10 million while creating the list.

# In[40]:


new_df = countries_df[countries_df['population']>10**6]
new_df


# In[41]:


new1_df= new_df.sort_values('gdp_per_capita',ascending = True).head(20)
new1_df


# In[42]:


new2_df = new_df.sort_values('hospital_beds_per_thousand',ascending = True).head(20)
new2_df


# In[43]:


new3_df = new1_df.merge(new2_df,on = 'location')
new3_df


# There are in total 10 countries that feature in both the lists "20 countries with lowest GDP per capita" and "20 countries with the lowest number of hospital beds per thousand population" and have population greater than 10 million.

# In[44]:


import jovian
jovian.commit(project='pandas-practice-assignment-19', environment=None)


# In[45]:


combined_df.set_index('population',inplace = True)
combined_df


# In[ ]:





# In[ ]:




