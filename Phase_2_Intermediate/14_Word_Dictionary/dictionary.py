"""
Project 14: Word Dictionary
External Requirements: pip install PyDictionary
"""
from PyDictionary import PyDictionary

dictionary = PyDictionary()
while True:
    word = input("Enter a word (or empty to exit): ")
    if word == "":
        break
    # print(dictionary.meaning(word))
