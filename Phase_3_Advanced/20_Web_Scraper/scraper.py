"""
Project 20: Web Scraper
External Requirements: pip install requests bs4
"""
import requests
from bs4 import BeautifulSoup

def scrape_github_avatar(github_username):
    url = f'https://github.com/{github_username}'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    profile_image = soup.find('img', {'alt': 'Avatar'})['src']
    print(f"Profile image URL for {github_username}: {profile_image}")

# scrape_github_avatar("tomitokko")
