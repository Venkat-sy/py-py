"""
Project 12: Currency Converter
External Requirements: None (using static rates for basic project)
"""
def main():
    print("This program converts US Dollars to Pounds Sterling")
    dollars = eval(input("Enter amount in dollars: "))
    pounds = dollars * 0.82 # static rate for simplicity
    print("That is", pounds, "pounds.")

main()
