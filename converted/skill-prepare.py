# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import pandas as pd
import numpy as np
df = pd.read_csv('dataset/marketing_sample_for_naukri_com-jobs__20190701_20190830__30k_data.csv')

#
# # Dataset Preparation
#

# ### Drop unused columns

df = df.drop(['Uniq Id', 
              'Crawl Timestamp', 
              'Job Salary', 
              'Job Experience Required', 
              'Location', 
              'Functional Area', 
              'Industry'], axis=1)

#
# ### Drop rows which are not the "Programming & Design" category
# note that, "category" = "role" in dataset
#

# +
df = df.drop(df[(df['Role Category'] != 'Programming & Design')].index)

### After that, drop "Role Category" column
df = df.drop('Role Category', axis=1)
df = df.dropna()
# -

#
# ### Trim and split Job Title, Key Skills
#

df['Job Title'] = df['Job Title'].str.strip()
df['Key Skills'] = df['Key Skills'].str.strip()
df['Key Skills'] = df['Key Skills'].str.split("|")

### Display all categories
df['Role'].unique()

# +
### reset dataframe index after everything done
df = df.reset_index(drop=True)

df.head()
# -

#
# ## Initial values
#

# +
roles = ['Testing Engineer',
         'System Analyst',
         'Technical Architect',
         'Software Developer',
         'Graphic/Web Designer',
         'Project Lead',
         'Team Lead/Technical Lead',
#          'Release Manager',
         'Product Manager',
         'Database Architect/Designer']

categories = ['Data', 
              'Developer', 
              'Tester', 
              'Designer', 
              'Manager', 
              'Analyst',
              'Support']

Data = ['Data Engineer',
        'Data Scientist',
        'Data Architect',
        'Data Analyst',
        'Database Administrator',
        'Machine Learning']

Developer = ['Software Engineer',
             'Devops',
             'Backend',
             'Frontend',
             'Full stack',
             'iOS',
             'Android']

Tester = ['Software Tester',
          'Quality Assurance Engineer']

Designer = ['UX/UI Designer',
            'Graphic Designer']

Manager = ['Product Owner',
           'Project Manager']

Analyst = ['System Analyst',
           'Business Analyst']

Support = ['Application Support',
           'Technical Support',
           'Customer Support']

forbidden_skills = ['development',
                    'design',
                    'web',
                    'css3',
                    'html5',
                    'operations',
                    'management',
                    'project leader',
                    'architect',
                    'architecture',
                    'testing',
                    'software',
                    'tools',
                    'quality',
                    'support',
                    'application',
                    'applications',
                    'developer',
                    'technical',
                    'automation',
                    'graphics',
                    'phd',
                    'email',
                    'apple',
                    'research',
                    'iphone',
                    'ipad']


# -

# ## Extract Key Skills function
# count skills by given set of "Key Skills" in job's dataframe

# +
#
##
### input like this -> extractSkill(dataframe['Key Skills'])
##
#

def extractSkill(df):

    # ### trim each Key Skill in each Title
    vowel = []
    for x in df:
        for i in range(len(x)):
            vowel.append(x[i].strip().lower())

    ### Counting elements
    elements_count = {}
    # iterating over the elements for frequency
    for element in vowel:
        # checking whether it is in the dict or not
        if element in elements_count:
            # incerementing the count by 1
            elements_count[element] += 1
        else:
            # setting the count to 1
            elements_count[element] = 1
        
    elements_count = dict(sorted(elements_count.items(), key=lambda item: item[1], reverse=True))

#     # printing the elements frequencies
#     for key, value in elements_count.items():
#         print(f"{key}: {value}")
        
    return elements_count



# -

# ## Replace and Remove Skills function
# input: dataframe with "skill" and "sum" columns

def cleanSkillKeywords(df):
    df = df.drop(df[(df['sum'] == 1)].index)
    
    df.loc[(df['skill'] == "Programming"), "skill"] = "coding"
    
    df.loc[(df['skill'] == "test automation"), "skill"] = "automation testing"
    
    df.loc[(df['skill'] == "data scientist"), "skill"] = "data science"
    
    df.loc[(df['skill'] == "data analyst"), "skill"] = "data analysis"
    
    df.loc[(df['skill'] == "asp") | 
           (df['skill'] == ".net") | 
           (df['skill'] == "asp.net mvc"), "skill"] = "asp.net"
    
    df.loc[(df['skill'] == "natural language processing"), "skill"] = "nlp"
    
    df.loc[(df['skill'] == "advanced analytics") | 
           (df['skill'] == "analytical") | 
           (df['skill'] == "analyst"), "skill"] = "analytics"
    
    df.loc[(df['skill'] == "front end") | (df['skill'] == "frontend"), "skill"] = "frontend development"
    
    df.loc[(df['skill'] == "backend"), "skill"] = "backend development"

    
    df.loc[(df['skill'] == "web technologies") | 
           (df['skill'] == "web application development") | 
           (df['skill'] == "web application"), "skill"] = "web development"
    
    df.loc[(df['skill'] == "ios"), "skill"] = "ios development"
    
    df.loc[(df['skill'] == "android") | 
           (df['skill'] == "android application development") | 
           (df['skill'] == "android application"), "skill"] = "android development"
    
    df.loc[(df['skill'] == "mobile") | 
           (df['skill'] == "mobile application") | 
           (df['skill'] == "mobile development") | 
           (df['skill'] == "mobile applications"), "skill"] = "mobile application development"
    
    df.loc[(df['skill'] == "user interface designing") | 
           (df['skill'] == "ui") | 
           (df['skill'] == "ui designer") | 
           (df['skill'] == "user interface") |
           (df['skill'] == "user interface designer"), "skill"] = "ui designing"
    
    df.loc[(df['skill'] == "ux designer") | 
           (df['skill'] == "ux") | 
           (df['skill'] == "user experience"), "skill"] = "ux designing"
    
    df.loc[(df['skill'] == "graphic designer"), "skill"] = "graphic designing"
    
    df.loc[(df['skill'] == "product manager"), "skill"] = "product management"
        
    df.loc[(df['skill'] == "project manager") |            
           (df['skill'] == "it project management"), "skill"] = "project management"
    
    df.loc[(df['skill'] == "agile scrum"), "skill"] = "scrum"
        
    df.loc[(df['skill'] == "agile development"), "skill"] = "agile"
    
    df.loc[(df['skill'] == "system analyst"), "skill"] = "system analysis"
    
    df.loc[(df['skill'] == "business analyst"), "skill"] = "business analysis"
    
    df.loc[(df['skill'] == "it"), "skill"] = "information technology"
    
    df.loc[(df['skill'] == "monitoring"), "skill"] = "monitoring tools"
    
    df = df[~df['skill'].isin(forbidden_skills)]
    
    df = df.groupby('skill')['sum'].agg(['sum']).sort_values(by=['sum'], ascending=False).reset_index() 
    
    return df

# ## Match between Jobs function
# method: set or sort<br>
# percent: integer (0 -> 100)

# +
from fuzzywuzzy import fuzz

def matchJobs(title, method, percent):
    
    def get_ratio_token_set(df):
        df_column = df['Job Title']
        return fuzz.token_set_ratio(title, df_column)
    
    def get_ratio_token_sort(df):
        df_column = df['Job Title']
        return fuzz.token_sort_ratio(title, df_column)

    if method == "set":
        match_data = df[df.apply(get_ratio_token_set, axis=1) >= percent]
    elif method == "sort":
        match_data = df[df.apply(get_ratio_token_sort, axis=1) >= percent]
        
    return match_data


# -

#
# # Job Skills
#

# #### example of matching

df_match = matchJobs(title="Customer Support", method="set", percent=90)
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    display(df_match)

# +
list_match = extractSkill(df_match['Key Skills'])
df_recommend = pd.DataFrame(list_match.items(), columns = ['skill', 'sum'])
df_recommend = cleanSkillKeywords(df_recommend)

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    display(df_recommend)


# -

# ### Init priority for each skill

def getJobsPriority(df):
    mean = df['sum'].mean()

    df.loc[(df['sum'] >= mean), "priority"] = "High"
    df.loc[(df['sum'] <= mean), "priority"] = "Normal"
    
    return df


# ## Jobs skillset

# +
df_all_job_skill = pd.DataFrame(columns = ['skill'])

for category in categories:
    for job in eval(category):

        df_match = matchJobs(title=job, method="set", percent=90)
        
        list_match = extractSkill(df_match['Key Skills'])
        df_recommend = pd.DataFrame(list_match.items(), columns = ['skill', 'sum']) 
        df_recommend = cleanSkillKeywords(df_recommend)
        
        df_recommend = df_recommend.head(10)
        
        df_recommend = getJobsPriority(df_recommend)
        
        df_recommend.loc[df_recommend.index[:], 'job'] = job
        df_recommend.loc[df_recommend.index[:], 'category'] = category

        ### push to all skill dataframe for export
        df_all_job_skill = df_all_job_skill.append(df_recommend)
# -

df_all_job_skill.to_csv('exports/job_skill.csv', index=False)
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    display(df_all_job_skill)

#
# # Category Skill
#

# +
df_all_category_skill = pd.DataFrame(columns = ['skill'])
df_category_skill = pd.DataFrame(columns = ['skill', 'sum'])

for category in categories:
    for job in eval(category):
    
        df_match = matchJobs(title=job, method="set", percent=90)

        list_match = extractSkill(df_match['Key Skills'])
        df_cat = pd.DataFrame(list_match.items(), columns = ['skill', 'sum']) 
        df_cat = df_cat.drop(df_cat[(df_cat['sum'] == 1)].index)
        df_cat = cleanSkillKeywords(df_cat)
        df_cat = df_cat.groupby('skill')['sum'].agg(['sum']).reset_index() 
        df_category_skill = df_category_skill.append(df_cat)

    df_category_skill = df_category_skill.groupby('skill')['sum'].agg(['sum','count']).sort_values(by=['count', 'sum'], ascending=False).reset_index()
    df_category_skill = df_category_skill.drop(df_category_skill[(df_category_skill['count'] == 1)].index)
    df_category_skill = df_category_skill.head(6)
    
    df_category_skill.loc[df_category_skill.index[:], 'category'] = category
    
    ### push to all skill dataframe for export
    df_all_category_skill = df_all_category_skill.append(df_category_skill)
# -

df_all_category_skill.to_csv('exports/category_skill.csv', index=False)
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    display(df_all_category_skill)


