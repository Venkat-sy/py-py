# Project 1: Email Sender

## 🎯 What are we building?
A Python script that logs into your email account and automatically sends an email to a recipient of your choice.

## 🤔 Why are we building this? (When to use it)
In the real world, automation is huge. You might use this to:
- Automatically email yourself a report every morning.
- Send a notification when a server goes down.
- Email users a "Welcome" message when they sign up for your app.

## ⚙️ External Interventions (Setup)
Because of security, Google (and other email providers) won't let a Python script log in with just your normal password. We need an **App Password**.

**Action Required:**
1. Go to your **Google Account** settings on the web.
2. Navigate to **Security**.
3. Make sure **2-Step Verification** is turned ON.
4. Search for **App Passwords** in the search bar.
5. Create a new App Password (name it something like "Python Setup").
6. Google will give you a 16-character password (e.g., `abcd efgh ijkl mnop`). 
7. **Save this password**. You will use it in your Python script instead of your real password.

## 🧠 How to do it (The Game Plan)
You do not need to install anything! Python comes with built-in tools for this:
- `smtplib`: The protocol used to send emails across the internet.
- `email.message`: A tool to format the email properly (Subject, To, From, Body).

**Step-by-Step Logic:**
1. Import `EmailMessage` from `email.message`, and import `smtplib` and `ssl`.
2. Create variables for:
   - Your email address.
   - Your 16-character app password.
   - The recipient's email address.
3. Create an `EmailMessage()` object. Set its `['From']`, `['To']`, and `['Subject']` fields. Use the `.set_content("your message here")` method to add the body text.
4. Create a secure context using `ssl.create_default_context()`.
5. Use `smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)` to connect to Google's mail server securely.
6. Use the `.login()` method with your email and app password.
7. Use the `.sendmail()` method to send it off!

## 💻 Your Turn
Open `email_sender.py`, delete the spoiler code I wrote earlier, and try to write it yourself following the Steps above. If you get stuck on the exact syntax, ask me!
