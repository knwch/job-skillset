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
df_category = pd.read_csv('exports/category_skill.csv')
df_job = pd.read_csv('exports/job_skill.csv')

# +
import requests
import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)



# -

# # Import prepared data directly to database

# ---

# ## Connect to MongoDB

# +
from pymongo import MongoClient

# build a new client instance of MongoClient
mongo_client = MongoClient('localhost', 27017)

# connect database
db = mongo_client.skillguider
# -

# drop collections before import new data
db['skills'].drop()
db['categories'].drop()
db['jobs'].drop()

# ---

# ## Import all skills to database

# ### Preparing data

# +
df_all_skill = pd.concat([df_category, df_job], axis=0)

df_all_skill = df_all_skill.drop(['sum', 'count', 'priority', 'job', 'category'], axis=1).drop_duplicates().reset_index(drop=True)
df_all_skill = df_all_skill.rename(columns={'skill': 'title'})
df_all_skill.loc[df_all_skill.index[:], 'title'] = df_all_skill['title'].str.capitalize()

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    display(df_all_skill)
# -

df_keyword_old = pd.read_csv('exports/keyword.csv')
df_keyword_new = pd.merge(df_keyword_old, df_all_skill, on='title', how='right').replace(np.nan, '', regex=True)
df_keyword_new.to_csv('exports/keyword.csv', index=False)

skill_json = df_keyword_new.to_json('exports/temp/all_skills.json', orient='records', default_handler=str)

# +
with open('exports/temp/all_skills.json') as f:
    data = json.load(f)

db['skills'].insert_many(data)
# -

# ---

# ## Import categories to database

# ### Preparing data

cursor = db['skills'].find({})
df_skill_with_id = pd.DataFrame(list(cursor), columns = ['_id', 'title'])

df_skill_with_id = df_skill_with_id.rename(columns={'title': 'skill'})
df_skill_with_id.loc[df_skill_with_id.index[:], 'skill'] = df_skill_with_id['skill'].str.lower()
df_skill_with_id

df_category_skill = df_category.drop(['sum', 'count'], axis=1).reset_index(drop=True)

df_merge_category = pd.merge(df_category_skill, df_skill_with_id, on='skill').sort_values(by=['category', 'skill'], ascending=False).reset_index(drop=True)
df_merge_category = df_merge_category.drop(['skill'], axis=1).rename(columns={'_id': 'skill_id', 'category': 'title'})
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    display(df_merge_category)

# ### Convert to json file on collection format

columns = df_merge_category.columns.difference(['title'])
category_json = df_merge_category.groupby(['title'])[columns].apply(lambda x: x.to_dict('r')).reset_index(name='skillset').to_json('exports/temp/categories.json', orient='records', default_handler=str)

# ### Insert json data to MongoDB

# +
with open('exports/temp/categories.json') as f:
    data = json.load(f)

db['categories'].insert_many(data)
# -

# ---

# ## Import jobs to database

# ### Preparing data

cursor = db['categories'].find({})
df_category_with_id = pd.DataFrame(list(cursor), columns = ['_id', 'title'])
df_category_with_id = df_category_with_id.rename(columns={'title': 'category'})

df_job_skill = df_job.drop(['sum'], axis=1).reset_index(drop=True)

df_merge_job = pd.merge(df_job_skill, df_skill_with_id, on='skill')
df_merge_job = df_merge_job.rename(columns={'_id': 'skill_id'})

df_merge_job = pd.merge(df_merge_job, df_category_with_id, on='category').sort_values(by=['job', 'skill'], ascending=False).reset_index(drop=True)
df_merge_job = df_merge_job.rename(columns={'_id': 'category_id'})

df_merge_job = df_merge_job.drop(['skill', 'category'], axis=1).rename(columns={'job': 'title'})

df_merge_job['description'] = '' 
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    display(df_merge_job.head())

# ### Convert to json file on collection format

columns = df_merge_job.columns.difference(['title', 'category_id', 'description'])
job_json = df_merge_job.groupby(['title', 'category_id', 'description'])[columns].apply(lambda x: x.to_dict('r')).reset_index(name='skillset').to_json('exports/temp/jobs.json', orient='records', default_handler=str)

# ### Insert json data to MongoDB

# +
with open('exports/temp/jobs.json') as f:
    data = json.load(f)

db['jobs'].insert_many(data)
# -

mongo_client.close()


