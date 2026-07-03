"""
Project 11: Site Connectivity Checker
External Requirements: urllib module (Built-in)
"""
import urllib.request as urllib

def main(url):
    print("Checking connectivity...")
    response = urllib.urlopen(url)
    print("Connected to", url, "successfully")
    print("The response code was:", response.getcode())

# main("https://www.google.com")
