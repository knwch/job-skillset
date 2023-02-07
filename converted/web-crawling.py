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

# Import dependencies
from bs4 import BeautifulSoup
import requests
from urllib.parse import quote
import pandas as pd


class GoogleSpider(object):
    def __init__(self):
        """Crawl Google search results

        This class is used to crawl Google's search results using requests and BeautifulSoup.
        """
        super().__init__()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:79.0) Gecko/20100101 Firefox/79.0',
#             'Host': 'www.medium.com',
#             'Referer': 'https://www.medium.com/'
        }

    def __get_source(self, url: str) -> requests.Response:
        """Get the web page's source code

        Args:
            url (str): The URL to crawl

        Returns:
            requests.Response: The response from URL
        """
        return requests.get(url, allow_redirects=True)

    def scrap(self, urls: []) -> list:
        """Search Google

        Args:
            query (str): The query to search for

        Returns:
            list: The search results
        """
        
        df_result = pd.DataFrame(columns = [
                'url',
                'title', 
                'description', 
                'image', 
                'published_date',
                'author',
                'section',
                'type',
              ])
        
        for url in urls:

            # Get response
            response = self.__get_source(url)
            # Initialize BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            # Get the result containers
            result_containers = soup.findAll('head')
            # Final results list
            results = []
            # Loop through every container
            for container in result_containers:

                if container.find('og:title'):
                    title = container.find('og:title').text
                elif container.find('title'):
                    title = container.find('title').text
                else:
                    title = ''

                if container.find('meta', {"property":"og:description"}):
                    description = container.find('meta', {"property":"og:description"})['content']
                else:
                    description = ''

                if container.find('meta', {"property":"og:image"}):
                    image = container.find('meta', {"property":"og:image"})['content']
                else:
                    image = ''

    #             if container.find('meta', {"property":"og:author"}):
    #                 author = container.find('meta', {"property":"og:author"})['content']
    #             else:
    #                 author = ''
    
                if container.find('meta', {"property":"article:published_time"}):
                    published_time = container.find('meta', {"property":"article:published_time"})['content']
                else:
                    published_time = ''

                if container.find('meta', {"property":"article:author"}):
                    article_author = container.find('meta', {"property":"article:author"})['content']
                else:
                    article_author = ''

                if container.find('meta', {"property":"article:section"}):
                    section = container.find('meta', {"property":"article:section"})['content']
                else:
                    section = ''

                if container.find('meta', {"property":"og:type"}):
                    _type = container.find('meta', {"property":"og:type"})['content']
                else:
                    _type = ''

                new_result = {
                    'url': url,
                    'title': title,
                    'description': description,
                    'image': image,
    #                 'author': author,
                    'published_date': published_time,
                    'author': article_author,
                    'section': section,
                    'type': _type,
                }

                df_result = df_result.append(new_result, ignore_index=True)

        return df_result


# +
urls = []
df_url = pd.read_excel('exports/urls.xlsx', index_col=0).reset_index()

for index in df_url.index:
    urls.append(df_url['url'][index])
# -

if __name__ == '__main__':
    df = GoogleSpider().scrap(urls)

df['published_date'] = pd.to_datetime(df['published_date'], format='%Y-%m-%d %H:%M:%S', utc=True).dt.strftime('%d/%m/%Y')

df

df.to_excel('exports/url-specific.xlsx', index=False)


