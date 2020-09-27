#!/usr/bin/env python
# coding: utf-8

# In[ ]:


start = 0
total_data=0
sample_variance = 0
data = [ ]

while start < 1:
    print ("Write 0 to stop")
    value = float (input ("Give me a value: "))
    data.append (value)
    
    if value ==0: 
        start += 1
    total_data = len(data)-1
    
print(data)

suma = 0
for start in data:
        suma += start
print (suma)


sample_mean = suma/total_data
print (f"The sample mean is= {sample_mean}")


for datas in data:
    sample_variance += ((datas-sample_mean)**2)/ len(data)-1
    
print (f"The sample variance is= {sample_variance}")

standard_deviation = (sample_variance)**0.5
print ( f"The Standard Deviation is= {standard_deviation}")


# In[ ]:





# In[ ]:




