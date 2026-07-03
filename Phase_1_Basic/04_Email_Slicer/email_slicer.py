"""
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
