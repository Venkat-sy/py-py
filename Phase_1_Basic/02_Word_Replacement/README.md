# Project 2: Word Replacement Program

## 🎯 What are we building?
A simple interactive script that takes a sentence, asks the user what word they want to replace, asks what they want to replace it *with*, and then prints the brand new sentence.

## 🤔 Why are we building this? (When to use it)
String manipulation is the bread and butter of Python. You will use this concept when:
- Cleaning up messy data (e.g., replacing "N/A" with "0" in a spreadsheet).
- Building search-and-replace features in text editors.
- Formatting user inputs before saving them to a database.

## ⚙️ External Interventions (Setup)
None! This project runs entirely using basic Python logic. No internet connection, API keys, or external libraries required.

## 🧠 How to do it (The Game Plan)
**Step-by-Step Logic:**
1. Create a variable containing a base sentence. (e.g., `my_string = "Hi, my name is Tomi and I love Python"`)
2. Use Python's `input()` function to ask the user: "Which word do you want to replace?". Save their answer in a variable.
3. Use the `input()` function again to ask: "What do you want to replace it with?". Save this answer too.
4. Use Python's built-in string method `.replace()`. 
   - *Hint:* The syntax is `string.replace(old_word, new_word)`
5. Print the new string to the console.

## 💻 Your Turn
Open `word_replacement.py`, delete the code I provided, and try writing this from scratch. Run it in your terminal when you're ready!
