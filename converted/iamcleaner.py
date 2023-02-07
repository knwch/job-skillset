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

# +
import numpy as np
import pandas as pd
import datetime
from dateutil.parser import parse
import tldextract

month_dict = {
    "ม.ค.": "Jan",
    "ก.พ.": "Feb",
    "มี.ค.": "Mar", 
    "เม.ย.": "Apr",
    "พ.ค.": "May",
    "มิ.ย.": "Jun",    
    "ก.ค.": "Jul",
    "ส.ค.": "Aug",
    "ก.ย.": "Sep",
    "ต.ค.": "Oct",
    "พ.ย.": "Nov",
    "ธ.ค.": "Dec",
}
# -

dataframe = pd.read_excel('exports/cse-keywords.xlsx', index_col=0).reset_index()
dataframe.head()

dataframe

# +
# for index in dataframe.index:

#     if pd.isnull(dataframe['title'][index]):
#        continue
#     else:        
#         if(pd.isnull(dataframe['meta_site_name'][index])):
#             dataframe['meta_site_name'][index] = tldextract.extract(dataframe['cse_url'][index]).domain.capitalize()
            
# dataframe.to_excel('exports/cse-keywords-cleaned.xlsx', index=False)

# +
dataframe_new = dataframe

dataframe_new["title"] = np.nan
dataframe_new["description"] = np.nan
dataframe_new["image"] = np.nan
# dataframe_new["date"] = np.nan

# dataframe_new['meta_article_published_time'] = pd.to_datetime(dataframe_new['meta_article_published_time'], format='%Y-%m-%d %H:%M:%S', utc=True).dt.strftime('%d/%m/%Y')

# +
def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try: 
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False
    
for index in dataframe_new.index:
    
    if pd.isnull(dataframe_new['cse_title'][index]):
       continue
    
    else:
    
        if(pd.isnull(dataframe_new['meta_title'][index])):
            dataframe_new['title'][index] = dataframe_new['cse_title'][index]
        else:
            dataframe_new['title'][index] = dataframe_new['meta_title'][index]

        if(pd.isnull(dataframe_new['meta_description'][index])):
            dataframe_new['description'][index] = dataframe_new['cse_description'][index]
        else:
            dataframe_new['description'][index] = dataframe_new['meta_description'][index]
            
        if(pd.isnull(dataframe_new['meta_site_name'][index])):
            dataframe_new['meta_site_name'][index] = tldextract.extract(dataframe_new['cse_url'][index]).domain.capitalize()

        if(pd.isnull(dataframe_new['meta_image'][index])):
            dataframe_new['image'][index] = dataframe_new['cse_image'][index]
        else:
            dataframe_new['image'][index] = dataframe_new['meta_image'][index]
            if(dataframe_new['image'][index][0] == '/' and dataframe_new['image'][index][1] == '/'):
                dataframe_new['image'][index] = dataframe_new['image'][index].replace("//", "https://")

#         if(pd.isnull(dataframe_new['meta_article_published_time'][index])):
#             date = dataframe_new['cse_description'][index].split(' ... ')[0]
#             for word, initial in month_dict.items():
#                 date = date.replace(word, initial)
#             if is_date(date):
#                 dataframe_new['date'][index] = date
#             else:
#                 dataframe_new['date'][index] = np.nan
#         else:
#             dataframe_new['date'][index] = dataframe_new['meta_article_published_time'][index]
        
# dataframe_new['date'] = pd.to_datetime(dataframe_new['date']).dt.strftime('%d/%m/%Y')      
        

# +
# dataframe_export = dataframe_new[['keyword', 
# #                                 'keyword_th',
#                                 'title', 
#                                 'description', 
#                                 'cse_url', 
#                                 'image', 
#                                 'date', 
#                                 'meta_article_author',
#                                 'meta_author',
#                                 'meta_section',
#                                 'meta_tag',
#                                 'meta_site_name',
#                                 'meta_type']]

dataframe_export_course = dataframe_new[['keyword',
                                        'title', 
                                        'description', 
                                        'cse_url', 
                                        'image', 
                                        'meta_site_name',
                                        'meta_type',
                                        'udemy_category', 
                                        'udemy_instructor', 
                                        'udemy_price']]
# -

dataframe_export.head()

dataframe_export_course.to_excel('exports/cse-keywords-cleaned.xlsx', index=False)

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    display(dataframe_export)


