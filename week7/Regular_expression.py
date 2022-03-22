import re

with open('../../data/addresses.txt') as f:
    addresses = f.read()

all_names = re.compile(r'')
all_phones = re.compile(r'\d{2} \d{2} \d{2} \d{2}')
all_zip_and_names = re.compile(r'(\d{4}) ([a-zA-ZæøåÆØÅ0-9 ]+)')

all_phone_match = all_phones.findall(addresses)

all_zip_and_names_match = all_zip_and_names.findall(addresses)

#print(all_phone_match)

for zip in all_zip_and_names_match:
    print(zip[0])

for zip in all_zip_and_names_match:
    print(zip[0],zip[1])

