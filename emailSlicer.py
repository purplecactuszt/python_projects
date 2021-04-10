email = input("Email Address: ").strip()

atSign = email.index('@')

username = email[:atSign]
domainName = email[atSign+1:]

print('\nEmail is: ',email)
print('Username is: ',username)
print('Domain name is: ',domainName)
