import phonenumbers
from phonenumbers import geocoder, carrier

def get_phone_info(number):
    phone_number = phonenumbers.parse(number)
    location = geocoder.description_for_number(phone_number, "en")
    carrier_name = carrier.name_for_number(phone_number, "en")

    return location, carrier_name

phone_number = input("Enter the phone number with the country code: ")
location, carrier_name = get_phone_info(phone_number)

print("Location: ", location)
print("Service Provider: ", carrier_name)







