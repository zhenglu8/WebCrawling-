#!/usr/bin/env python
# coding: utf-8

# In[33]:


from bs4 import BeautifulSoup
import requests
import csv


# In[34]:


source = requests.get('https://sg.jobsdb.com/j?sp=homepage&q=&l=Singapore').text
soup = BeautifulSoup(source, 'lxml')

print(soup.prettify())


# In[35]:


job = soup.find('div', class_='job-container result sponsored-job sponsored-top')
print(job.prettify())


# In[36]:


#Get company's name
companyNameContainer = job.find('span', class_='job-company')

companyName = companyNameContainer.text
print(companyName)


# In[37]:


#Get company's title
companyLocationContainer = job.find('span', class_='job-location')

companyLocation = companyLocationContainer.text
print(companyLocation)


# In[38]:


#Get job's title
jobTitleContainer = job.find('h3')

jobTitle = jobTitleContainer.text
print(jobTitle)


# In[39]:


#Get job's salary
jobSalaryContainer = job.find('div', class_='job-salary-badge badge')

jobSalary = jobSalaryContainer.text
print(jobSalary)


# In[48]:


csv_file = open('jobsDB_firstPage', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Company Name', 'Company Location', 'Jon Title', 'Job Salary'])


# In[49]:


for job in soup.find_all('div', class_='job-container result sponsored-job sponsored-top'):
    companyNameContainer = job.find('span', class_='job-company')
    companyName = companyNameContainer.text
    print(companyName)
    
    companyLocationContainer = job.find('span', class_='job-location')
    companyLocation = companyLocationContainer.text
    print(companyLocation)
    
    jobTitleContainer = job.find('h3')
    jobTitle = jobTitleContainer.text
    print(jobTitle)
    
    try:
        jobSalaryContainer = job.find('div', class_='job-salary-badge badge')
        jobSalary = jobSalaryContainer.text
    except Exception as e:
        jobSalary = None
        
    print(jobSalary)
    
    print()
    
    csv_writer.writerow([companyName, companyLocation, jobTitle, jobSalary])
    


# In[50]:


for job in soup.find_all('div', class_='job-container result organic-job'):
    companyNameContainer = job.find('span', class_='job-company')
    companyName = companyNameContainer.text
    print(companyName)
    
    companyLocationContainer = job.find('span', class_='job-location')
    companyLocation = companyLocationContainer.text
    print(companyLocation)
    
    jobTitleContainer = job.find('h3')
    jobTitle = jobTitleContainer.text
    print(jobTitle)
    
    try:
        jobSalaryContainer = job.find('div', class_='job-salary-badge badge')
        jobSalary = jobSalaryContainer.text
    except Exception as e:
        jobSalary = None
        
    print(jobSalary)
    
    print()
    
    csv_writer.writerow([companyName, companyLocation, jobTitle, jobSalary])
    


# In[51]:


for job in soup.find_all('div', class_='job-container result sponsored-job sponsored-bottom'):
    companyNameContainer = job.find('span', class_='job-company')
    companyName = companyNameContainer.text
    print(companyName)
    
    companyLocationContainer = job.find('span', class_='job-location')
    companyLocation = companyLocationContainer.text
    print(companyLocation)
    
    jobTitleContainer = job.find('h3')
    jobTitle = jobTitleContainer.text
    print(jobTitle)
    
    try:
        jobSalaryContainer = job.find('div', class_='job-salary-badge badge')
        jobSalary = jobSalaryContainer.text
    except Exception as e:
        jobSalary = None
        
    print(jobSalary)
    
    print()
    
    csv_writer.writerow([companyName, companyLocation, jobTitle, jobSalary])
    
csv_file.close()


# In[ ]:





# In[ ]:




