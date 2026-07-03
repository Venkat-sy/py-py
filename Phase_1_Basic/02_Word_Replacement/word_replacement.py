"""
Project 2: Word Replacement Program
External Requirements: None
"""
def replace_word():
    base_str = "Hi guys, I am learning Python, and Python is great."
    print(f"Original string: {base_str}")
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word replacement: ")
    print(base_str.replace(word_to_replace, word_replacement))

if __name__ == "__main__":
    replace_word()
