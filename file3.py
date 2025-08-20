country_code = {'India' : '091',
                'Australia' : '0025',
                'Nepal' : '00977'}

# search dictionary for country code of India
print("country code for India -")
print(country_code.get('India', 'not found'))


# search dictionary for country code of Japan
print("country code for Japan -")
print(country_code.get('Japan', 'not found'))