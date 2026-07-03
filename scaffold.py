import os

projects = {
    "Phase_1_Basic/01_Email_Sender/email_sender.py": '''"""
Project 1: Email Sender
External Requirements: Google Account, App Password (Security -> 2-Step Verification -> App Passwords)
"""
from email.message import EmailMessage
import smtplib
import ssl

email_sender = 'your_email@gmail.com'
email_password = 'your_app_password'
email_receiver = 'receiver@example.com'
subject = 'Test Subject'
body = 'Test Body'

em = EmailMessage()
em['From'], em['To'], em['Subject'] = email_sender, email_receiver, subject
em.set_content(body)

context = ssl.create_default_context()
# To test, uncomment the lines below:
# with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#     smtp.login(email_sender, email_password)
#     smtp.sendmail(email_sender, email_receiver, em.as_string())
''',

    "Phase_1_Basic/02_Word_Replacement/word_replacement.py": '''"""
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
''',

    "Phase_1_Basic/03_Basic_Calculator/calculator.py": '''"""
Project 3: Basic Calculator
External Requirements: None
"""
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b

while True:
    print("A. Addition  B. Subtraction  C. Multiplication  D. Division  E. Exit")
    choice = input("Enter your choice: ").upper()
    if choice == 'E': break
    
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    if choice == 'A': print("Result:", add(a, b))
    elif choice == 'B': print("Result:", sub(a, b))
    elif choice == 'C': print("Result:", mul(a, b))
    elif choice == 'D': print("Result:", div(a, b))
''',

    "Phase_1_Basic/04_Email_Slicer/email_slicer.py": '''"""
Project 4: Email Slicer
External Requirements: None
"""
def main():
    print("Welcome to the email slicer")
    print("")
    email_input = input("Input your email address: ")
    
    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")
    
    print("Username:", username)
    print("Domain:", domain)
    print("Extension:", extension)

if __name__ == "__main__":
    main()
''',

    "Phase_1_Basic/05_Binary_Search/binary_search.py": '''"""
Project 5: Binary Search Algorithm
External Requirements: None
"""
def binary_search(list, element):
    start, end = 0, len(list)
    steps = 0
    while start < end:
        print("Step", steps, ":", str(list[start:end]))
        steps += 1
        mid = (start + end) // 2
        if list[mid] == element:
            return mid
        elif list[mid] < element:
            start = mid + 1
        else:
            end = mid
    return -1

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
binary_search(my_list, target)
''',

    "Phase_1_Basic/06_Quiz_Program/quiz.py": '''"""
Project 6: Quiz Program
External Requirements: None
"""
quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    }
}
score = 0
for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer: ")
    if answer.lower() == value['answer'].lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong! The answer is:", value['answer'])

print(f"You got {score} out of 2 questions correctly")
''',

    "Phase_2_Intermediate/07_QR_Code_Generator/qr_generator.py": '''"""
Project 7: QR Code Generator
External Requirements: pip install qrcode Image
"""
import qrcode

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg.png")
    print("QR Code generated and saved as qrimg.png")

# generate_qrcode("https://www.google.com")
''',

    "Phase_2_Intermediate/08_Interest_Calculator/interest_calculator.py": '''"""
Project 8: Interest Payment Calculator
External Requirements: None
"""
def main():
    print("This is a monthly payment loan calculator")
    principal = float(input("Input the loan amount: "))
    apr = float(input("Input the annual interest rate: "))
    years = int(input("Input amount of years: "))
    
    monthly_interest_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-amount_of_months))
    
    print("The monthly payment for this loan is: %.2f" % monthly_payment)

if __name__ == "__main__":
    main()
''',

    "Phase_2_Intermediate/09_Password_Generator/password_generator.py": '''"""
Project 9: Random Password Generator
External Requirements: None
"""
import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_length = int(input("How long would you like your password to be? "))
    random.shuffle(characters)
    password = []
    for x in range(password_length):
        password.append(random.choice(characters))
    random.shuffle(password)
    password = "".join(password)
    print("Generated password:", password)

generate_password()
''',

    "Phase_2_Intermediate/10_Dice_Rolling/dice_roller.py": '''"""
Project 10: Dice Rolling Simulator
External Requirements: None
"""
import random

def roll_dice():
    roll = input("Roll the dice? (Yes/No): ")
    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print("dice rolled: {} and {}".format(dice1, dice2))
        roll = input("Roll again? (Yes/No): ")

roll_dice()
''',

    "Phase_2_Intermediate/11_Site_Connectivity/connectivity_checker.py": '''"""
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
''',

    "Phase_2_Intermediate/12_Currency_Converter/currency_converter.py": '''"""
Project 12: Currency Converter
External Requirements: None (using static rates for basic project)
"""
def main():
    print("This program converts US Dollars to Pounds Sterling")
    dollars = eval(input("Enter amount in dollars: "))
    pounds = dollars * 0.82 # static rate for simplicity
    print("That is", pounds, "pounds.")

main()
''',

    "Phase_2_Intermediate/13_Leap_Year_Checker/leap_year.py": '''"""
Project 13: Leap Year Checker
External Requirements: None
"""
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year")
            else:
                print("Not leap year")
        else:
            print("Leap year")
    else:
        print("Not leap year")

is_leap_year(2024)
''',

    "Phase_2_Intermediate/14_Word_Dictionary/dictionary.py": '''"""
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
''',

    "Phase_3_Advanced/15_Image_Resizer/image_resizer.py": '''"""
Project 15: Image Resizer
External Requirements: pip install Pillow
"""
from PIL import Image

def resize_image(size1, size2):
    # Ensure you have a 'test.jpg' in the directory to test this!
    try:
        image = Image.open('test.jpg')
        print(f"Current size: {image.size}")
        resized_image = image.resize((size1, size2))
        resized_image.save('test_resized.jpg')
        print("Image resized successfully.")
    except Exception as e:
        print("Error: Provide a test.jpg image in this folder to run this code.")

# resize_image(500, 500)
''',

    "Phase_3_Advanced/16_Graph_Plotter/graph_plotter.py": '''"""
Project 16: Graph Plotter
External Requirements: pip install matplotlib
"""
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [2, 4, 1]

plt.plot(x, y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('My first graph!')

# To view the plot, uncomment below:
# plt.show()
''',

    "Phase_3_Advanced/17_Rock_Paper_Scissors/rock_paper_scissors.py": '''"""
Project 17: Rock, Paper, Scissors
External Requirements: None
"""
import random

choices = ['rock', 'paper', 'scissors']
user_score = 0
computer_score = 0

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in choices:
        continue
    
    random_number = random.randint(0, 2)
    computer_pick = choices[random_number]
    print("Computer picked", computer_pick + ".")
    
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_score += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_score += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_score += 1
    elif user_input == computer_pick:
        print("Draw!")
    else:
        print("You lost!")
        computer_score += 1

print("You won", user_score, "times.")
print("The computer won", computer_score, "times.")
''',

    "Phase_3_Advanced/18_Face_Detection/face_detection.py": '''"""
Project 18: Face Detection
External Requirements: pip install opencv-python
Need a haarcascade_frontalface_default.xml file from OpenCV github.
"""
import cv2

# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# img = cv2.imread('test.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
# cv2.imshow('img', img)
# cv2.waitKey()
print("Please review external requirements to run this project.")
''',

    "Phase_3_Advanced/19_Python_Automation/automation.py": '''"""
Project 19: Python Automation (e.g., Sending Text via schedule)
External Requirements: pip install schedule
"""
import schedule
import time

def send_message():
    print("Task Executed! (Here you would add SMS logic, e.g. using Twilio)")

# schedule.every().day.at("06:00").do(send_message)
# while True:
#     schedule.run_pending()
#     time.sleep(1)
print("Automation logic prepared. Uncomment to run.")
''',

    "Phase_3_Advanced/20_Web_Scraper/scraper.py": '''"""
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
'''
}

for filepath, content in projects.items():
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as f:
        f.write(content)

print("All 20 projects have been generated!")
