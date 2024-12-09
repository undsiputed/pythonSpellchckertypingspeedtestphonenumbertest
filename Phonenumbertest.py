import requests

def check_dnc(phone_number):
    url = f"https://telemarketing.donotcall.gov/data/phones/{phone_number}"
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False

phone_number = input("Enter the phone number: ")
if check_dnc(phone_number):
    print("The phone number is on the National Do Not Call Registry.")
else:
    print("The phone number is not on the National Do Not Call Registry.")