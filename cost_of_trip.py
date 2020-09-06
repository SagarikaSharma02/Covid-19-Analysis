#!/usr/bin/env python
# coding: utf-8

# # Exercise

# You're planning a leisure trip (vacation) and you need to decide which city you want to visit. You have shortlisted 4 cities, and identified the cost of the return flight, daily hotel cost and a weekly car rental cost (a car has to be rented for full weeks, even if you return the car before a week ends).
# 
# 
# Answer the following questions using the data above:
# 
# If you're planning a 1-week long trip, which city should you visit to spend the least amount of money?
# 
# How does the answer to the previous question change if you change the duration of the trip to 4 days, 10 days or 2 weeks?
# 
# If your total budget for the trip is $1000, which city should you visit to maximize the duration of your trip? Which city should you visit if you want to minimize the duration?
# 
# How does the answer to the previous question change if your budget is $600, $2000 or $1500?
# 
# Hint: To answer these questions, it will help to define a function cost_of_trip with relevant inputs like flight cost, hotel rate, car rental rate and duration of the trip. You may find the math.ceil function useful for calculating the total cost of car rental.

# City                   Return Flight ($)	          Hotel per day($)	                Weekly Car Rental ($)
# Paris	               200	                              20	                           200
# London	               250	                              30	                           120
# Dubai	               370	                              15	                           80
# Mumbai	               450	                              10	                           70

# In[9]:


import math

def cost_of_trip(flight_cost,hotel_rate,car_rental,duration_of_the_trip):
    total_cost_of_car_rental = car_rental*(math.ceil(duration_of_the_trip/7))
    total_cost = flight_cost + hotel_rate*duration_of_the_trip + total_cost_of_car_rental
    
    return total_cost
    


# In[10]:


duration_of_the_trip = int(input("enter duration of trip"))
cp = cost_of_trip(200,20,200,duration_of_the_trip)
cl = cost_of_trip(250,30,120,duration_of_the_trip)
cd = cost_of_trip(370,15,80,duration_of_the_trip)
cm = cost_of_trip(450,10,70,duration_of_the_trip)
print(cp,cl,cd,cm)


# # Another Way

# In[7]:


paris = {'flight':200 , 'hotel':20 , 'car':200}
london = {'flight':250 , 'hotel':30 , 'car':120}
dubai = {'flight':370 , 'hotel':15 , 'car':80}
mumbai = {'flight':450 , 'hotel':10 , 'car':70}


# In[8]:


def cost_of_trip(city,duration):
    num_weeks = math.ceil(duration/7)
    return city['flight'] + city['hotel']*duration + city['car']*num_weeks


# In[6]:


for duration in range(1,25):
    print("{} days".format(duration))
    for city in [paris,london,dubai,mumbai]:
        print(cost_of_trip(city,duration))
    


# In[ ]:




