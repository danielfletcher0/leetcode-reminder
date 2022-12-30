from bs4 import BeautifulSoup
import requests


def GetTitle(url):
    """Function for retrieving the title from the browser using BeautifulSoup"""
    link = ''.join(url)
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    title_found = False
    while not title_found:
        title = soup.find('title')
        if title:
            title = title.text.split('-')
            title_found = True
            return title[0]
        else:
            return 'Title tag not found'


def GetLink(url):
    """Function for retrieving the true link no matter if an original problem
        or from a problem list"""
    # Find the meta tag with the og:url property
    link = ''.join(url)
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    meta_tag = soup.find('meta', {'property': 'og:url'})
    # Extract the link from the content attribute
    link = meta_tag['content']
    return link

