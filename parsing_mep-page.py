import requests
from bs4 import BeautifulSoup

class MEP:
    # A member of european parliament
    def __init__(self, url):
        self.html = requests.get(url)
        self.soup = BeautifulSoup(self.html.content, 'html.parser')
        self.name = self.soup.find(class_="sln-member-name").text.title()
        self.eu_party = self.soup.find(class_="erpl_title-h3 mt-1").text
        self.country, self.party = [x.strip() for x in self.soup.find(class_='erpl_title-h3 mt-1 mb-1').text.split('-')]
        self.birthday = (self.soup.find(class_="sln-birth-date")).string.strip()
        self.birthplace =(self.soup.find(class_="sln-birth-place")).string.strip()
        
    def social(self):
        # Gets social media accounts
        # Issue: email is corrupted
        some = self.soup.find("div", class_="erpl_social-share-horizontal d-flex flex-row align-items-center justify-content-center")
        some_dict = {}
        for tag in some.find_all('a'):
            key = tag.find(class_="sr-only").text
            value = tag.get('href')
            some_dict[key] = value
        return some_dict
