phone_number = '38050123459'
valid_phone_number = phone_number.isdigit() and len(phone_number) == 12 and phone_number[0:3] == '380'

print(valid_phone_number)

